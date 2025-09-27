################################################################################
# This file contains the functions for the sun-dic analysis.  The functions
# are used to perform local Digital Image Correlation (DIC) analysis.
##
# Author: G Venter
# Date: 2024/06/05
################################################################################

# Import libraries required by the code
import os as os
import math as m
import natsort as ns
import time
import cv2 as cv
import numpy as np
from enum import IntEnum, Enum
import skimage as sk
import ray as ray
# import numba
from sundic.util.fast_interp import interp2d
import sundic.util.datafile as dataFile
from scipy.interpolate import NearestNDInterpolator
from sundic.util.savitsky_golay import sgolay2d

# --------------------------------------------------------------------------------------------
# Constants that does not make sense to set in the settings file
# --------------------------------------------------------------------------------------------
# Define integer constants


class IntConst(IntEnum):
    ICLM_LAMBDA_0 = 100     # Initial value for lambda in IC-LM
    ICLM_CZNSSD_0 = 4       # Initial value for CZNSSD in IC-LM
    AKAZE_MIN_PNTS = 10     # Minimum number of keypoints to detect
    CNZSSD_MAX = 1000000    # Maximum value for CZNSSD - indicate point has not been set
    SUBSET_PNT_SIZE = 17    # Number of values stored for each subset
    MIN_SUBSET_SIZE = 5     # Minimum allowable subset size to use for the analysis
    MAX_NEIGHBORS = 4       # Maximum number of random neighbors to use for next point

# Define floating point constants


class FloatConst(float, Enum):
    SIZE_FACTOR = 1.5       # Factor to increase the subset size for the AKAZE detection
    # Fraction of points in subset to use for approximate CZNSSD calculation
    ZCNSSD_PNT_FRACTION = 0.5
    # This is only used to determine the starting and next points

# Define some indices into the subSetPnts array


class CompID(IntEnum):
    XCoordID = 0   # The x-coordinate of the subset center point
    YCoordID = 1   # The y-coordinate of the subset center point
    SSSizeID = 2   # The subset size
    ShapeFnID = 3   # The shape function - 0 = affine, 1 = quadratic
    CZNSSDID = 4   # The CZNSSD value for the subset
    XDispID = 5   # The x-displacement of the subset point - start of x model coefficients
    YDispID = 11  # The y-displacement of the subset point - start of y model coefficients

# Define the affine and shape function constants


class ShapeFN(IntEnum):
    AFFINE = 0      # Affine shape function
    QUADRATIC = 1   # Quadratic shape function

# --------------------------------------------------------------------------------------------
# These are two very simple utility functions to do some basic timing of operations during
# development


def _tic_():
    """
    Start the timer for measuring elapsed time.
    """
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()


def _toc_():
    """
    Prints the elapsed time since the start time for the tictoc timer.

    If the start time is not set, it prints a message indicating that the start time is not set.
    """
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() -
              startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")


# --------------------------------------------------------------------------------------------
def _getImageList_(imgSubFolder, debugLevel=0):
    """
    Construct list of images from the specified sub-folder.  The list of images is sorted in
    natural order.

    Parameters:
        - imgSubFolder (string): A string specifying the folder for loading
            planar images.
        - debugLevel (int): Specify what level of debug output is requested.

    Returns:
        - list: A list of filenames of the images loaded from the specified
            folder.  The list of images are sorted naturally.
    """
    # Setup the image folder form the specified subfolder
    image_folder = os.path.join(os.getcwd(), imgSubFolder)

    # Get the filenames (naturally sorted) of all images in the directory
    files = ns.os_sorted(os.listdir(image_folder))

    # Add the directory back into the filename and store as a list of all files
    image_set = [os.path.join(image_folder, f) for f in files]

    # Print debug messages based on debug level
    if debugLevel > 1:
        print('\nLoading images from folder: ' + image_folder)
        print('  Images loaded, image set:')
        [print('  '+img) for img in image_set]

    # Return the list of filenames
    return image_set


# --------------------------------------------------------------------------------------------
def planarDICLocal(settings, resultsFile, externalRay=False, guiThread=None):
    """
    Perform local planar (2D) Digital Image Correlation (DIC) analysis.

    This function takes a dictionary of settings as input and performs local DIC analysis
    based on the specified settings. The analysis involves processing a series of image pairs
    to obtain displacement and strain data.

    Parameters:
        - settings: A Settings object containing the settings for the DIC analysis.
        - resultsFile: The name of the file to store the results in.
        - externalRay: A boolean indicating whether to use an external ray server or not.
        - guiThread: The GUI thread object if running from the GUI, otherwise None. Used to 
                    cleanly stop the analysis if requested from the GUI.

    Returns:
        - returnData (list): A list of subSetPoint arrays. Each subSetPoint array is a
            3D matrix where the first plane contains the x-coordinates
            the second plane the y-coordinates and the remaining planes the subset size,
            shapeFn, CZNSSD value and model coefficients.  This array can be processed to
            obtain displacement and strain data and to generate graphs.

    Raises:
        - ValueError: If an invalid optimization algorithm is specified.
    """
    try:
        # Let's set a random seed for repeatable results
        np.random.seed(42)

        # Store the debug level
        debugLevel = settings.DebugLevel

        # Get the images to work with
        imgSet = _getImageList_(settings.ImageFolder, debugLevel=debugLevel)

        # Get the Region of Interest (ROI)
        ROI = _setupROI_(settings.ROI, imgSet[0], debugLevel=debugLevel)

        # Define measurement points using the settings specified in the config file
        # These are the center points of the subsets
        subSetSize = settings.SubsetSize
        stepSize = settings.StepSize
        shapeFn = settings.ShapeFunctions
        subSetPnts = _setupSubSets_(
            subSetSize, stepSize, shapeFn, ROI, imgSet[0], debugLevel=debugLevel)

        # Get the image pair information
        imgDatum = settings.DatumImage
        imgTarget = settings.TargetImage
        if imgTarget == -1:
            imgTarget = len(imgSet)-1
        imgIncr = settings.Increment
        imgPairs = int((imgTarget - imgDatum)/imgIncr)

        # Debug output if requested
        if debugLevel > 0:
            print('\nImage Pair Information :')
            print('---------------------------------')
            print('  Number of image pairs : {}'.format(imgPairs))

        # Setup serialization of the data to msgpack binary file
        df = dataFile.DataFile.openWriter(resultsFile)
        df.writeHeading(settings)

        # Initialize the parallel enviroment if required
        nCpus = settings.CPUCount
        if nCpus > 1:
            if debugLevel > 0:
                print('\nParallel Run Information :')
                print('---------------------------------')
                print('  Starting parallel run with {} CPUs'.format(nCpus))
                if externalRay:
                    print('  Using external ray server')

                # Init ray with restarts
                _safeRayInit_(externalRay, nCpus, debugLevel=debugLevel)

        # Loop through all image pairs to perform the local DIC
        returnData = []
        x_coordInit = np.copy(subSetPnts[:, :, CompID.XCoordID])
        y_coordInit = np.copy(subSetPnts[:, :, CompID.YCoordID])

        for imgPairIdx, img in enumerate(range(imgDatum, imgTarget, imgIncr)):

            # Store previous iteration displacement values
            x_dispPrev = np.copy(subSetPnts[:, :, CompID.XDispID])
            y_dispPrev = np.copy(subSetPnts[:, :, CompID.YDispID])

            # Setup the parallel run and wait for all results
            if nCpus > 1:
                # Turn of debugging temporarily
                nDebugOld = settings.DebugLevel
                settings.DebugLevel = 0

                # Setup the submatrices - match shape to image if possible
                nTotRows, nTotCols, _ = subSetPnts.shape
                mRows, mCols = _factorCPUCount_(nCpus, nTotRows/nTotCols)
                if nDebugOld > 0:
                    print("\n  Splitting matrix into {}x{} submatrices".format(
                        mRows, mCols))
                    print("")
                subMatrices = _splitMatrix_(subSetPnts, mRows, mCols)

                # Track the processes that are being submitted
                procIDs = []
                for i in range(mRows*mCols):
                    iRow, iCol = np.unravel_index(i, (mRows, mCols))
                    procIDs.append(_rmt_icOptimization_.remote(
                        settings, iRow, iCol, subMatrices[iRow][iCol], imgSet, img, guiThread=guiThread))

                    if nDebugOld > 0:
                        print("  Starting remote process for submatrix {} {}".
                              format(iRow, iCol))

                if nDebugOld > 0:
                    print("")

                # Wait for results - start pulling results from tasks as soon as they are
                # are done
                while len(procIDs):
                    done_id, procIDs = ray.wait(procIDs)

                    # Launch ray tasks with retries
                    iRow, iCol, rsltMatrix = _safeRayLaunch_(
                        done_id[0], debugLevel=nDebugOld)
                    (subMatrices[iRow][iCol])[:] = rsltMatrix
                    if nDebugOld > 0:
                        print("  Submatrix {} {} completed".format(iRow, iCol))

                # Turn debugging back on
                settings.DebugLevel = nDebugOld

            # Serial run on one processor
            else:
                # coefficients at convergence for current (i'th) image pair
                subSetPnts[:] = _icOptimization_(
                    settings, subSetPnts, imgSet, img, guiThread=guiThread)

            # Update the subset points coordinates if required - we make copies of the
            # current subset points to create a new array of subset points
            if settings.isRelativeStrategy():
                subSetPnts[:] = _updateSubSets_(x_coordInit, y_coordInit, x_dispPrev, y_dispPrev,
                                                subSetPnts)

            # Store the current subset points in the return data
            subSetPntsOut = np.copy(subSetPnts)
            subSetPntsOut[:, :, CompID.XCoordID] = x_coordInit
            subSetPntsOut[:, :, CompID.YCoordID] = y_coordInit
            returnData.append(subSetPntsOut)
            df.writeSubSetData(imgPairIdx, subSetPntsOut)

            # Make a copy for the next iteration to work with in the next iteration
            # currSubSetPnts = np.copy(currSubSetPnts)

            # The currently stored image subsetpoints are now the previous subset points
            # prevSubSetPnts = returnData[imgPairIdx]

            # Make some debug output
            if (settings.DebugLevel > 0):
                print('\n  ------------------------------------------------------')
                print('  Image pair {} processed:'.format(imgPairIdx))
                if settings.isAbsoluteStrategy():
                    print('    '+imgSet[imgDatum])
                else:
                    print('    '+imgSet[img])
                print('    '+imgSet[img+imgIncr])
                print('  ------------------------------------------------------\n')

        # Shutdown the parallel environment if required
        if settings.CPUCount > 1:
            _safeRayShutdown_(externalRay, debugLevel=debugLevel)
        # Close the file
        df.close()

        return returnData

    # Handle exceptions and shutdown ray if required
    except Exception as e:
        if settings.CPUCount > 1:
            _safeRayShutdown_(externalRay, debugLevel=debugLevel)
        raise e


# --------------------------------------------------------------------------------------------
@ray.remote
def _rmt_icOptimization_(settings, iRowID, iColID, subSetPnts, imgSet, img, guiThread=None):
    """
    Perform the IC optimization for a subset of points in a parallel environment.  This is a
    very thin wrapper for the icOptimization function that allows the function to be called
    from ray and keeps track of the subMatrix indices that are being processed.

    Parameters:
        - settings (dict): The settings for the DIC analysis.
        - iRowID (int): The row index of the submatrix.
        - iColID (int): The column index of the submatrix.
        - subSetPnts (ndarray): The subset points to optimize.
        - imgSet (ndarray): The array of images.
        - img (int): The index of the image to process.
        - guiThread: The GUI thread object if running from the GUI, otherwise None. Used to
                    cleanly stop the analysis if requested from the GUI.

    Returns:
        - tuple: A tuple containing the row index, column index, and the updated subset points.
    """
    rslt = _icOptimization_(settings, np.copy(
        subSetPnts), imgSet, img, guiThread=guiThread)
    return iRowID, iColID, rslt


# --------------------------------------------------------------------------------------------
def _setupROI_(ROI, img0, debugLevel=0):
    """
    Get the Region of Interest (ROI) based on the settings provided by the user.

    Parameters:
        - ROI (int[]): An integer array of four values from the settings file.
        - img0 (str): The path to the reference image file.
        - debugLevel (int): The level of debug output to print.

    Returns:
        - ROI (int[]): An int array representing the ROI with four elements [XStart, YStart,
            XLength, YLength].
    """
    # If xLength or yLength is zero, use full image based on image size
    # of first image
    if (ROI[2] == 0 or ROI[3] == 0):

        # Read the image and determine the size
        img = readImage(img0)
        height, width = img.shape

        # Ensure starts are non-negative
        xStart = max(0, ROI[0])
        yStart = max(0, ROI[1])

        # Calculate lengths
        xLength = ROI[2] if ROI[2] != 0 else width - xStart
        yLength = ROI[3] if ROI[3] != 0 else height - yStart

        # Ensure lengths do not exceed image bounds
        xLength = min(xLength, width - xStart)
        yLength = min(yLength, height - yStart)

        # Ensure ROI is at least M pixels from edges
        M = IntConst.MIN_SUBSET_SIZE
        xStart = max(xStart, M)
        yStart = max(yStart, M)
        xLength = min(xLength, width - 2*M)
        yLength = min(yLength, height - 2*M)

        ROI = [xStart, yStart, xLength, yLength]

    # Debug print out
    if debugLevel > 0:
        print('\nROI : ')
        print('---------------------------------')
        print('  XStart  = '+str(ROI[0]))
        print('  YStart  = '+str(ROI[1]))
        print('  XLength = '+str(ROI[2]))
        print('  YLength = '+str(ROI[3]))

    return ROI


# --------------------------------------------------------------------------------------------
def _setupSubSets_(subSetSize, stepSize, shapeFn, ROI, img0, debugLevel=0):
    """
    Calculate the center points of subsets within a given region of interest (ROI) based on
    the subset size and step size.

    Parameters:
    - subSetSize (int): The size of each subset.
    - stepSize (int): The step size between subsets.
    - shapeFn (string): The order of the shape functions for each subset.
    - ROI (tuple): A tuple containing the origin coordinates (xOrigin, yOrigin)
        and the dimensions (width, height) of the ROI.
    - img0 (str): The path to the reference image file.
    - debugLevel (int): The level of debug output to print.

    Returns:
    - subSetPnts (ndarray): An array of shape (nRows, nCols, nVals) where nRows are the number
        of rows in the point grid (y-values), nCols is the number of columns (x-values) and
        nVals are the number of values stored for each point.  These are the x,y coordinates
        followed by the model coeficients.
    """
    # Read the image and determine the size
    img = readImage(img0)
    imgH, imgW = img.shape

    # Get DIC bounds to work with based on the ROI definition
    xOrigin, yOrigin, roiW, roiH = ROI
    xBound = xOrigin + roiW
    yBound = yOrigin + roiH

    # Now setup the measurement point coordidnates: defined in the reference image,
    # i.e subset centres
    y0, x0 = np.meshgrid(np.arange(yOrigin, yBound, stepSize),
                         np.arange(xOrigin, xBound, stepSize),
                         indexing='ij')

    # The number of rows and columns in the subset grid
    nRows, nCols = y0.shape

    # Allocate the memory for the subset points
    # x and y coordinates, the shape function coefficients and an analyze or not flag
    subSetPnts = np.zeros((nRows, nCols, IntConst.SUBSET_PNT_SIZE))

    # Store the x and y coordinates in the subSetPnts
    subSetPnts[:, :, CompID.XCoordID] = x0
    subSetPnts[:, :, CompID.YCoordID] = y0

    # Store the subset size
    subSetPnts[:, :, CompID.SSSizeID] = subSetSize

    # Store the shape function type
    subSetPnts[:, :, CompID.ShapeFnID] = _convertShapeFn_(shapeFn)

    # Initial values for CNZSSD and model coefficients
    subSetPnts[:, :, CompID.CZNSSDID] = IntConst.CNZSSD_MAX
    subSetPnts[:, :, CompID.XDispID:] = 0.0

    # ----------------------------------------------------------------------------------------
    # Check that the subsets are not exceeding the image bounds
    # ----------------------------------------------------------------------------------------
    autoFix = False
    autoFix = _fixSubSetSize_(subSetPnts, CompID.XCoordID, 0, imgW)
    autoFix = _fixSubSetSize_(subSetPnts, CompID.YCoordID, 0, imgH)

    # Let the user know we've automatically fixed the subset sizes
    if autoFix:
        print('WARNING: Some subset sizes were auto-fixed to fit within the image bounds. ')
        print('         This warning can be avoided by specifying an appropriate ROI.')
        if debugLevel > 0:
            print('         The subset sizes after auto-fixing are:')
            print(subSetPnts[:, :, CompID.SSSizeID])

    # Ensure that the subset size is not smaller than the minimum subset size
    subSetPnts[:, :, CompID.SSSizeID] = np.maximum(
        subSetPnts[:, :, CompID.SSSizeID], IntConst.MIN_SUBSET_SIZE)

    # Print debug output if requested
    if debugLevel > 0:
        nSubSets = nRows * nCols
        print('\nSubset Information : ')
        print('---------------------------------')
        print('         Number of subsets defined : '+str(nSubSets))
        print('     Number of rows in subset grid : '+str(nRows))
        print('  Number of columns in subset grid : '+str(nCols))

    return subSetPnts


# --------------------------------------------------------------------------------------------
def _fixSubSetSize_(subSetPnts, index, lowerBnd, upperBnd):
    """
    Check and fix the subset sizes based on the specified lower and upper image bounds.  If 
    the subset sizes are out of bounds, they are adjusted to fit within the specified bounds.
    This function is used to ensure that the subset sizes do not exceed the image bounds.

    Parameters:
        - subSetPnts (ndarray): The subset points array.
        - index (int): The index of the coordinate to check (0 for x, 1 for y).
        - lowerBnd (float): The lower bound for the subset size.
        - upperBnd (float): The upper bound for the subset size.

    Returns:
        - autoFix (bool): A boolean flag indicating if the subset sizes were auto-fixed.
    """

    # Flag to indicate if we had to auto-fix the subset sizes
    autoFix = False

    # Get the center point values
    cntVals = subSetPnts[:, :, index]

    # Check the lower bound
    M = (subSetPnts[:, :, CompID.SSSizeID] - 1) / 2
    bndLowDiff = (cntVals - M) - lowerBnd
    outOfBounds = np.where(bndLowDiff < 0)
    if outOfBounds[0].size > 0:
        autoFix = True
        subSetPnts[outOfBounds[0], outOfBounds[1], CompID.SSSizeID] = \
            subSetPnts[outOfBounds[0], outOfBounds[1], CompID.SSSizeID] + \
            2.0*bndLowDiff[outOfBounds]

    # Check the upper bound
    M = (subSetPnts[:, :, CompID.SSSizeID] - 1) / 2
    bndUppDiff = (upperBnd - (cntVals + M))
    outOfBounds = np.where(bndUppDiff < 0)
    if outOfBounds[0].size > 0:
        autoFix = True
        subSetPnts[outOfBounds[0], outOfBounds[1], CompID.SSSizeID] = \
            subSetPnts[outOfBounds[0], outOfBounds[1], CompID.SSSizeID] + \
            2.0*bndUppDiff[outOfBounds] - 2

    return autoFix


# --------------------------------------------------------------------------------------------
def _updateSubSets_(x_coordInit, y_coordInit, x_dispPrev, y_dispPrev, currSubSetPnts):
    """
    Update the subset points based on the calculated displacement values as we move from one
    image pair to the next.  Only used with the incremental reference strategy.

    Parameters:
    - x_coordInit (ndarray): An array of initial x-coordinates.
    - y_coordInit (ndarray): An array of initial y-coordinates.
    - x_dispPrev (ndarray): An array of previous displacement values in the x-direction.
    - y_dispPrev (ndarray): An array of previous displacement values in the y-direction.
    - currSubSetPnts (ndarray): An array of subset points from the current image pair.

    Returns:
        - numpy.ndarray: An updated current array of subset points.
    """

    # Update the current displacements with the previous displacements to get the total
    # displacements
    currSubSetPnts[:, :, CompID.XDispID] = currSubSetPnts[:, :, CompID.XDispID] + \
        x_dispPrev
    currSubSetPnts[:, :, CompID.YDispID] = currSubSetPnts[:, :, CompID.YDispID] + \
        y_dispPrev

    # The total displacement values for the current iteration - we have to fill missing
    # data due to the potential NaN that may have occured in the displacement field
    nSubSets = currSubSetPnts.shape[0] * currSubSetPnts.shape[1]

    # Flatten arrays for missing data fill
    x_coords_flat = currSubSetPnts[:, :,
                                   CompID.XCoordID].reshape(nSubSets, order='F')
    y_coords_flat = currSubSetPnts[:, :,
                                   CompID.YCoordID].reshape(nSubSets, order='F')

    delX = currSubSetPnts[:, :, CompID.XDispID].reshape(nSubSets, order='F')
    delX = _fillMissingData_(
        x_coords_flat,
        y_coords_flat,
        currSubSetPnts[:, :, CompID.XDispID].reshape(nSubSets, order='F')
    )
    delY = _fillMissingData_(
        x_coords_flat,
        y_coords_flat,
        currSubSetPnts[:, :, CompID.YDispID].reshape(nSubSets, order='F')
    )

    # Update the subset point locations with the displacement value
    # We update the initial point locations with the total displacements up to
    # this point
    currSubSetPnts[:, :, CompID.XCoordID] = np.rint(x_coordInit + delX.reshape(
        currSubSetPnts.shape[0], currSubSetPnts.shape[1], order='F'))
    currSubSetPnts[:, :, CompID.YCoordID] = np.rint(y_coordInit + delY.reshape(
        currSubSetPnts.shape[0], currSubSetPnts.shape[1], order='F'))

    return currSubSetPnts


# --------------------------------------------------------------------------------------------
# @numba.njit
def _meshgrid_flat_2d_(x):
    """
    Generates a 3D flattened meshgrid from a 1D array.

    This function creates two 1D arrays representing the y-coordinates and 
    x-coordinates of a 3D meshgrid, flattened into 1D arrays. It is optimized 
    using Numba's `njit` for performance.

    Parameters:
        x (numpy.ndarray): A 1D array of values to generate the meshgrid from.

    Returns:
        tuple: A tuple containing two 1D numpy arrays:
            - yy (numpy.ndarray): The y-coordinates of the flattened meshgrid.
            - xx (numpy.ndarray): The x-coordinates of the flattened meshgrid.
    """
    xx = np.empty(shape=(x.size * x.size), dtype=x.dtype)
    yy = np.empty_like(xx)
    for i in range(x.size):
        for j in range(x.size):
            xx[i*x.size + j] = x[i]
            yy[i*x.size + j] = x[j]
    return yy, xx


# --------------------------------------------------------------------------------------------
def _relativeCoords_(subSetSize, fraction=1.0):
    """
    Generate relative/local coordinates of pixels within the subset.  The coordinates are
    generated based on the subset size with one point for each pixel in the subset.

    Parameters:
    - subSetSize (int): The size of the subset.
    - fraction (float): The fraction of points to randomly select for CZNSSD calculation.

    Returns:
    - tuple: A tuple containing the sampleIndices, xsi and eta coordinates as numpy arrays.
    """
    # Relative/local coordinates of pixels within the subset (the same for all subsets)
    # Create 1D coordinates
    coords = np.linspace(-0.5*(subSetSize-1), 0.5*(subSetSize-1), subSetSize)

    # Create 2D grid of coordinates using meshgrid with 'ij' indexing and flatten
    eta, xsi = np.meshgrid(coords, coords, indexing='ij')
    xsi_flat = xsi.flatten(order='F')
    eta_flat = eta.flatten(order='F')
    # eta_flat, xsi_flat = _meshgrid_flat_2d_(coords)

    # Randomly select a smaller subset of points to estimate the CZNSSD value
    # if a fraction < 1.0 is specified
    if fraction < 1.0:
        nSubSetPnts = xsi_flat.shape[0]
        nSamplePnts = min(int(fraction*nSubSetPnts), nSubSetPnts)
        sampleIndices = np.random.choice(
            nSubSetPnts, size=nSamplePnts, replace=False)
        return sampleIndices, xsi_flat[sampleIndices], eta_flat[sampleIndices]

    return None, xsi_flat, eta_flat


# --------------------------------------------------------------------------------------------
def _icOptimization_(settings, subSetPnts, imgSet, img, guiThread=None):
    """
    Perform IC (inverse compositional update) optimization for image correlation.  Currently
    two optimization algorithms are supported - IC-GN (Gauss Newton) or
    IC-LM (Levenberg-Marquardt).

    Parameters:
        - settings (dict): Dictionary containing the optimization settings.
        - subSetPnts (ndarray): 3D Array of subset point information.
        - imgSet (ndarray): Array of reference images.
        - img (int): Target image - index into the imgSet array.
        - guiThread: The GUI thread object if running from the GUI, otherwise None. Used to
                    cleanly stop the analysis if requested from the GUI.

    Returns:
        - subSetPnts: 3D Array of updated subSetPnt information (shape function coefficients).

    Raises:
        - ValueError: If an invalid optimization algorithm is specified.
    """
    # Setup subset info
    nSubSets = subSetPnts.shape[0]*subSetPnts.shape[1]

    # Setup the GaussBlur parameters
    gbSize = settings.GaussianBlurSize
    gbStdDev = settings.GaussianBlurStdDev

    # The number of GQ starting points and the background cutoff value
    nBGCutOff = settings.BackgroundCutoff
    nGPPoints = settings.StartingPoints

    # Initialize the CNZSSD value to max
    subSetPnts[:, :, CompID.CZNSSDID] = IntConst.CNZSSD_MAX

    # Detect algorithm to use
    isICGN = True
    isNormalized = False

    # IC-GN algorithm
    if settings.isICGN():
        isICGN = True
        isICLM = False
        isFastICLM = False
        isNormalized = False
    # IC-LM algorithm
    elif settings.isICLM():
        isICGN = False
        isICLM = True
        isFastICLM = False
        isNormalized = True
    # Fast IC-LM algorithm - same as IC-LM but with one less interpolation per iteration
    elif settings.isFastICLM():
        isICGN = False
        isICLM = False
        isFastICLM = True
        isNormalized = True
    else:
        raise ValueError(
            'Invalid optimizationAlgorithm specified. Only supported values are: IC-GN | IC-LM | FastIC-LM')

    # Process reference and target images for current image pair
    # delF: dFdy = delF[0], dFdx = delF[1]
    # Process the two images
    imgIncr = settings.Increment
    imgDatum = settings.DatumImage
    fImgID = img
    if settings.isAbsoluteStrategy():
        fImgID = imgDatum
    gImgID = img + imgIncr
    interOrder = settings.InterpolationOrder
    F, _, delF, FMax = _processImage_(imgSet, fImgID, [gbSize, gbStdDev], interOrder,
                                      isDatumImg=True, isNormalized=isNormalized)
    G, GInter, _, _ = _processImage_(imgSet, gImgID, [gbSize, gbStdDev], interOrder,
                                     isDatumImg=False, isNormalized=isNormalized)

    # Adjust the BGCutOff value for normalized images
    if isICLM or isFastICLM:
        nBGCutOff = nBGCutOff/FMax

    # Get the starting point for the optimization
    nextPnt, subSetPnts = _getStartingPnt_(
        subSetPnts, nGPPoints, F, G, GInter, nBGCutOff)

    # Boolean array to indicate which points have been analyzed - initially all are false
    analyze = np.zeros_like(subSetPnts[:, :, CompID.XCoordID], dtype=bool)

    # Print debug info if requested
    if settings.DebugLevel > 0:
        print('\nStarting IC Optimization for Image Pair: '+str(img))
        print('---------------------------------')

    # Loop through all subset points, determine the model coefficients
    # for each subset independently - the order is determined by the next best
    # point to optimize
    for iSubSet in range(0, nSubSets):

        # Check if we need to stop the analysis - only if running from the GUI
        if guiThread is not None and guiThread.isRunning() is False:
            if settings.DebugLevel > 0:
                print('\n-----------------------------------------------------')
                print('-- Stopping analysis as requested from GUI  ---------')
                print('-----------------------------------------------------')
            break

        # Current point to work with
        iRow, iCol = nextPnt

        # Get the subset size and shapeFn for the current subset
        subSetSize = subSetPnts[iRow, iCol, CompID.SSSizeID].astype(int)
        shapeFn = subSetPnts[iRow, iCol, CompID.ShapeFnID].astype(int)

        # Get the local coordinates for a subset (based on that subset's size)
        _, xsi, eta = _relativeCoords_(subSetSize)

        # Subset centre coordinates for current subset
        x0 = int(subSetPnts[iRow, iCol, CompID.XCoordID])
        y0 = int(subSetPnts[iRow, iCol, CompID.YCoordID])

        # Intensity data for reference subset
        f, f_mean, f_tilde, dfdx, dfdy = _referenceSubSetInfo_(
            F, delF, x0, y0, subSetSize, subSetIndices=None)

        # Hessian and Jacobian operators for GuassNewton optimization routine,
        # derived from the reference subset intensity gradient data
        H, J = _getHessianInfo_(dfdx, dfdy, xsi, eta, subSetSize,
                                shapeFn, isNormalized)

        # Current subset model shape function coefficients
        shapeFnCoeffs_i = subSetPnts[iRow, iCol, CompID.XDispID:]

        # Initial estimate for the incremental update of the model coefficients
        # in the current iteration - initial estimate set to 0 for all coefficients
        deltaP = np.zeros_like(shapeFnCoeffs_i)

        # Perform optimisation routine - IC-GN or IC-LM
        iter = 0
        while iter < settings.MaxIterations:

            # Check for convergence, otherwise update the model coefficients
            if iter > 0 and _isConverged_(settings.ConvergenceThreshold, settings.NZCCThreshold,
                                          deltaP, subSetPnts[iRow, iCol, CompID.CZNSSDID]):
                break
            else:

                # Relative deformed subset coordinates, based on current
                # iteration of deformation model
                xsi_d, eta_d = _relativeDeformedCoords_(
                    shapeFnCoeffs_i, xsi, eta, shapeFn)

                # Intensity data for reference subset
                g, g_mean, g_tilde = _deformedSubSetInfo_(
                    GInter, x0, y0, xsi_d, eta_d)

                # Calculate and store the current CZNSSD value
                subSetPnts[iRow, iCol, CompID.CZNSSDID] = _calcCZNSSD_(nBGCutOff,
                                                                       f, f_mean, f_tilde, g, g_mean, g_tilde)

                # Check if CZNSSD is at maximum value - indicates point is not found
                if subSetPnts[iRow, iCol, CompID.CZNSSDID] == IntConst.CNZSSD_MAX:
                    iter = settings.MaxIterations
                    break

                # Calculate the residuals
                res = f-f_mean-(f_tilde/g_tilde)*(g-g_mean)

                # The right hand side of the update equation
                b = -np.dot(J.T, res)

                # Perform IC-GN update
                if (isICGN):

                    # Get the new deltaP from delta - hardcode the ranges in deltaP to
                    # ensure we have the correct number of coefficients that we copy
                    # over from delta
                    delta = np.squeeze(np.linalg.solve(H, b))
                    if shapeFn == ShapeFN.AFFINE:
                        deltaP = np.zeros_like(shapeFnCoeffs_i)
                        deltaP[0:3] = delta[0:3]
                        deltaP[6:9] = delta[3:]
                    elif shapeFn == ShapeFN.QUADRATIC:
                        deltaP[0:12] = delta[:]

                    # Update the model coefficients
                    shapeFnCoeffs_i[:] = _modelCoeffUpdate_(shapeFnCoeffs_i, deltaP,
                                                            shapeFn)

                elif (isFastICLM or isICLM):

                    # Initialize the df, df_mean and df_tilde values - this is all we need
                    # for the fast IC-LM algorithm
                    df = f
                    df_mean = f_mean
                    df_tilde = f_tilde

                    # For the normal IC-LM algorithm we need to actually calcualte these
                    if isICLM:
                        # Delta p deformation applied to the original image
                        xsi_df, eta_df = _relativeDeformedCoords_(
                            deltaP, xsi, eta, shapeFn)

                        f, f_mean, f_tilde, _, _ = _referenceSubSetInfo_(
                            F, None, x0, y0, subSetSize, subSetIndices=None)

                    # Get he current CZNSSD value
                    cznssd = _calcCZNSSD_(nBGCutOff, df, df_mean, df_tilde,
                                          g, g_mean, g_tilde)

                    # Initialize the lambda and cznssd_0 values
                    if iter == 0:
                        cznssd_0 = IntConst.ICLM_CZNSSD_0
                        lam = (IntConst.ICLM_LAMBDA_0 **
                               (cznssd/IntConst.ICLM_CZNSSD_0)) - 1.

                    # Identity matrix with lambda value on diagonals
                    lamI = lam*np.identity(H.shape[0])

                    # Solve for the normalized deltaP
                    delta = np.squeeze(np.linalg.solve((H+lamI), b))

                    # Convert to the non-normalized deltaP
                    K = 0.5*(subSetSize-1)
                    if shapeFn == ShapeFN.AFFINE:
                        M = np.diag([1., 1./K, 1./K, 1., 1./K, 1./K])
                    elif shapeFn == ShapeFN.QUADRATIC:
                        M = np.diag([1., 1./K, 1./K, 1./(K*K), 1./(K*K), 1./(K*K),
                                     1., 1./K, 1./K, 1./(K*K), 1./(K*K), 1./(K*K)])

                    delta = np.dot(M, delta)

                    # Get the new deltaP from delta - hardcode the ranges in deltaP to
                    # ensure we have the correct number of coefficients that we copy
                    # over from delta
                    if shapeFn == ShapeFN.AFFINE:
                        deltaP = np.zeros_like(shapeFnCoeffs_i)
                        deltaP[0:3] = delta[0:3]
                        deltaP[6:9] = delta[3:]
                    elif shapeFn == ShapeFN.QUADRATIC:
                        deltaP[0:12] = delta[:]

                    # Update lambda
                    if cznssd >= cznssd_0:
                        lam = 10.*lam
                    else:
                        lam = 0.1*lam

                        # Update the model coefficients
                        shapeFnCoeffs_i[:] = _modelCoeffUpdate_(shapeFnCoeffs_i, deltaP,
                                                                shapeFn)

                        # Update cznssd_0
                        cznssd_0 = cznssd

            iter += 1

        # If we do not converge the point is not found and se will add nan to the shape
        # function coefficients
        if iter == settings.MaxIterations:
            shapeFnCoeffs_i[:] = np.nan
            subSetPnts[iRow, iCol, CompID.CZNSSDID] = IntConst.CNZSSD_MAX

        # Print debug output if requested
        if settings.DebugLevel > 1:
            print("  Subset {0:6d} of {1:6d}: ID ({2:4d},{3:4d})  Iteration Cnt {4:3d}".
                  format(iSubSet, nSubSets, iRow, iCol, iter))

        elif settings.DebugLevel > 0 and iSubSet % 100 == 0:
            print("  Subset {0:6d} of {1:6d}: ID ({2:4d},{3:4d})  Iteration Cnt {4:3d}".
                  format(iSubSet, nSubSets, iRow, iCol, iter))

        # Mark the current point as analyzed
        analyze[nextPnt] = True

        # Find the next point to iterate to
        nextPnt, subSetPnts = _getNextPnt_(nextPnt, subSetPnts, analyze, F, G,
                                           GInter, nBGCutOff)

    return subSetPnts


# --------------------------------------------------------------------------------------------
def _processImage_(imgSet, img, gaussBlur, interOrder, isDatumImg, isNormalized):
    """
    Process an image to obtain DIC specific parameters.  If this is the datum image
    the gradient of the image is also calculated and no interpolation is setup.  
    Otherwise, only the image and the interpolated image is calculated.

    Paramters:
        - imgSet (list): A list of image paths.
        - img (int): The index of the image to process.
        - gaussBlur (tuple): Gauss blur size and std dev.
        - interOrder (int): The order of the interpolation to use.
        - isDatumImg (bool): Indicates whether the image is the
            reference image.
        - isNormalized (bool): Indicates whether the image should be
            normalized.

    Returns:
        tuple: A tuple containing the processed image and related data.
            - F (numpy.ndarray): The processed image.
            - F_interpolated (numpy.ndarray): The interpolated image (or the processed 
                image if isDatumImg is True).
            - delF (numpy.ndarray or None): The gradient of the image in the
                x and y directions, or None if isDatumImg is False.
            - Fmax (int): The maximum value of the image.
    """
    # Pre-blur filter parameters from settings file
    gfSize, gfStdDev = gaussBlur

    # Read the image as grayscale
    F = readImage(imgSet[img])

    # Setup the gradients, but only if this is a reference image
    delF = None
    if (isDatumImg):
        # Gradient of the image in the x and y directions
        # NOTE:  This is a gradient of noisy data and should be carefully approached
        # We tried two approaches and both seem to work quite well
        #   1. Blur the image (Gaussian Blur) and then do numpy gradient calculations
        #      The blur operation and the central difference gradients seem to work
        #      quite well to remove noise
        #   2. Use the sobel operator for gradient calculations - this is often used
        #      in image processing for edge detection and seems to work well.  The
        #      sobel operator is a convolution operation and is a bit slower than the
        #      numpy gradient calculations but is only applied once and is done BEFORE
        #      the blur operation
        #
        # Numpy gradients - if we do this, blur before gradient calculation
        # delF = np.gradient(F)
        #
        # Using the sobel operator - apply BEFORE the blur operation
        # Use a minimum kernel size for the sobel operator
        ksize = max(3, gfSize)
        sobel_div = m.pow(2., 2 * ksize - 1 - 2)
        dfy = cv.Sobel(F, ddepth=cv.CV_32F, dx=0,
                       dy=1, ksize=ksize) / sobel_div
        dfx = cv.Sobel(F, ddepth=cv.CV_32F, dx=1,
                       dy=0, ksize=ksize) / sobel_div
        delF = [dfy, dfx]

    # Blur image with gaussian filter - if specified in settings
    if (gfSize > 0):
        F = cv.GaussianBlur(F, (gfSize, gfSize), gfStdDev)

    # Normalize the image if requested
    Fmax = np.max(F)
    if isNormalized:
        F = F / Fmax
        if delF is not None:
            delF = [d / Fmax for d in delF]

    # Setup the interpolator for this image - needs to pass double precision values
    # for interpolation to work
    FInter = None
    if not isDatumImg:
        FInter = _fastInterpolation_(F.astype('double'), interOrder)

    return F, FInter, delF, Fmax


# --------------------------------------------------------------------------------------------
def _getNextPnt_(currentPnt, subSetPnts, analyzed, F, G, GInter,
                 nBGCutOff):
    """
    Get the next point to analyze in the optimization algorithm.  The next point is
    selected based on updated, estimated CZNSSD values for points the current point and the
    current deformation model.

    Parameters:
        - currentPnt (tuple): The index of the current point - tuple with iRow and ICol.
        - subSetPnts (numpy.ndarray): The subSetPnts data strucutre - 3D array that contains
            coordinates of the center points and deformation model coefficients.
        - analyzed (numpy.ndarray): A boolean array indicating which points have been analyzed.
        - F (numpy.ndarray): The query image.
        - G (numpy.ndarray): The train image.
        - GInter (numpy.ndarray): The interpolated train image.
        - nBGCutOff (int): The cutoff value to detect all black backgrounds.

    Returns:
        - tuple: The iRow, iCol index of the next point to analyze.
        - numpy.ndarray: The updated subSetPnts array.
    """
    # Get the matrix position of the current point
    iRow, iCol = currentPnt
    maxRow, maxCol = subSetPnts.shape[0] - 1, subSetPnts.shape[1] - 1

    # Precompute neighbor indices
    neighbor_indices = [
        (max(0, iRow - 1), iCol),
        (min(maxRow, iRow + 1), iCol),
        (iRow, max(0, iCol - 1)),
        (iRow, min(maxCol, iCol + 1)),
        (max(0, iRow - 1), max(0, iCol - 1)),
        (max(0, iRow - 1), min(maxCol, iCol + 1)),
        (min(maxRow, iRow + 1), max(0, iCol - 1)),
        (min(maxRow, iRow + 1), min(maxCol, iCol + 1))
    ]

    neighbors = [(r, c) for r, c in neighbor_indices
                 if r is not None and c is not None and
                 not analyzed[r, c]]

    # Shuffle neighbors for randomness
    neighbors = np.random.permutation(neighbors)

    # Apply the current deformation model to the selected neighbors and calculate the resulting CZNSSD value
    # Update the CZNSSD value and the shape function parameters if the new CZNSSD value is smaller
    for iRow, iCol in neighbors[:IntConst.MAX_NEIGHBORS]:

        # Skip this point if it has already been analyzed
        if analyzed[iRow, iCol]:
            continue

        # The current point and its coordinates
        x0 = int(subSetPnts[iRow, iCol, CompID.XCoordID])
        y0 = int(subSetPnts[iRow, iCol, CompID.YCoordID])
        subSetSize = subSetPnts[iRow, iCol, CompID.SSSizeID].astype(int)
        shapeFn = subSetPnts[iRow, iCol, CompID.ShapeFnID].astype(int)

        # Local coordinats for this point
        sampleIndices, xsi, eta = _relativeCoords_(subSetSize,
                                                   fraction=FloatConst.ZCNSSD_PNT_FRACTION)

        # Impose the deformation model on the subset and get the reference and deformed
        # subset information
        xsi_d, eta_d = _relativeDeformedCoords_(
            subSetPnts[iRow, iCol, CompID.XDispID:], xsi, eta, shapeFn)

        f, f_mean, f_tilde, _, _ = _referenceSubSetInfo_(
            F, None, x0, y0, subSetSize, subSetIndices=sampleIndices)
        g, g_mean, g_tilde = _deformedSubSetInfo_(
            GInter, x0, y0, xsi_d, eta_d)

        # Get the CZNSSD value for the current point
        oldCZNSSD = subSetPnts[iRow, iCol, CompID.CZNSSDID]
        newCZNSSD = _calcCZNSSD_(nBGCutOff, f, f_mean,
                                 f_tilde, g, g_mean, g_tilde)

        # Store the CZNSSD value in the last element of the parameter vector
        if newCZNSSD < oldCZNSSD:
            subSetPnts[iRow, iCol, CompID.XDispID:] = \
                subSetPnts[currentPnt[0], currentPnt[1], CompID.XDispID:]
            subSetPnts[iRow, iCol, CompID.CZNSSDID] = newCZNSSD

    # Find the index of the best point that has not been analyzed yet using a masked
    # array to ignore the analyzed points
    cznssd_arr = subSetPnts[:, :, CompID.CZNSSDID]
    masked_cznssd = np.where(~analyzed, cznssd_arr, np.inf)
    nextPnt = np.unravel_index(np.argmin(masked_cznssd), masked_cznssd.shape)

    # Return the next point to analyze
    return nextPnt, subSetPnts


# --------------------------------------------------------------------------------------------
def _getStartingPnt_(subSetPnts, nGQPoints, F, G, GInter, nBGCutOff):
    """
    Get the starting point for the optimization algorithm.  This is done by detecting
    keypoints in a selection of subset points located at Gauss Quadrature points spread
    over the image.  The keypoints are matched and used to estimate the
    deformation from the reference to the deformed image to calcluate the CZNSSD parameter
    for each.  The point the smallest CZNSSD is selected as the starting point.  This
    should provide a good starting point for the optimization algorithm for these points.

    Parameters:
        - subSetPnts (numpy.ndarray): 3D Array of subSetPoint information - center point
            coordinates and model coefficients.
        - nGQPoints (int): The number of Gauss Quadrature points to use as starting points.
        - F (numpy.ndarray): The query image.
        - G (numpy.ndarray): The train image.
        - GInter (numpy.ndarray): The interpolated train image.
        - nBGCutOff (int): The cutoff value to detect all black backgrounds.

    Returns:
        - (iRow, iCol): The index of the best starting point.
        - subSetPnts: Updated with the deformation model coefficients for each starting point.
    """
    # Get the Gauss points
    gqPnts, _ = np.polynomial.legendre.leggauss(nGQPoints)

    # Scale the points to the desired ranges in terms of the rows and cols
    # int the subSetPnts matrix
    nRow, nCol = subSetPnts.shape[:2]
    xPnts = np.round(((nCol/2 - 1) * (1 + gqPnts))).astype(int)
    yPnts = np.round(((nRow/2 - 1) * (1 + gqPnts))).astype(int)

    # Extract the points to use in the Akaze detect
    # Do broadcasting to get all the required points not just a diagonal
    # Note: We are now using fancy indexing so we have a copy of the data in adPoints
    adPoints = subSetPnts[np.ix_(yPnts, xPnts)].copy()

    # Do the Akaze detect for all the test points and get back the parameter
    # vector
    adPoints = _akazeDetect_(adPoints, F, G)

    # Store the parameters with the CZNSSD value in the shapeFnCoeff matrix
    xcoord, ycoord = CompID.XCoordID, CompID.YCoordID
    sssize, shapeFn = CompID.SSSizeID, CompID.ShapeFnID
    xdisp = CompID.XDispID
    cznssd_idx = CompID.CZNSSDID
    it = np.nditer([adPoints[:, :, xcoord], adPoints[:, :, ycoord],
                    adPoints[:, :, sssize].astype(int),
                    adPoints[:, :, shapeFn].astype(int)], flags=['multi_index'])
    for x0, y0, subSetSize, shapeFn in it:

        # Get the local coordinates for this subset
        _, xsi, eta = _relativeCoords_(subSetSize)

        # Impose the deformation model on the subset and get the reference and deformed
        # subset information
        iRow, iCol = it.multi_index
        xsi_df, eta_df = _relativeDeformedCoords_(
            adPoints[iRow, iCol, xdisp:], xsi, eta, shapeFn)

        f, f_mean, f_tilde, _, _ = _referenceSubSetInfo_(
            F, None, int(x0), int(y0), subSetSize, subSetIndices=None)
        g, g_mean, g_tilde = _deformedSubSetInfo_(
            GInter, x0, y0, xsi_df, eta_df)

        # Get the current CZNSSD value
        cznssd = _calcCZNSSD_(nBGCutOff, f, f_mean,
                              f_tilde, g, g_mean, g_tilde)

        # Store the CZNSSD value in the last element of the parameter vector
        adPoints[iRow, iCol, cznssd_idx] = cznssd

    # Update the original data structure - remember adPoints was a copy due to fancy
    # indexing
    subSetPnts[np.ix_(yPnts, xPnts)] = adPoints

    # We can actually setup a mask to search as we do for the getNextPoint operation,
    # however it seems faster to just directly search for the minimum value and it is
    # only done once
    startIdx = np.unravel_index(
        np.argmin(subSetPnts[:, :, cznssd_idx]), subSetPnts[:, :, cznssd_idx].shape)

    return startIdx, subSetPnts


# --------------------------------------------------------------------------------------------
def _akazeDetect_(adPoints, F, G):
    """
    Detects keypoints and computes descriptors using the AKAZE algorithm for the specified
    subsets (in adPoints) in the given images.  The keypoints are matched and used to
    estimate the deformation from the reference to the deformed image.  This should provide
    a good starting point for the optimization algorithm for these points.

    Parameters:
        - adPoints (numpy.ndarray): The subset of points to use as starting points from the
            subSetPnts data structure.
        - F (numpy.ndarray): The query image.
        - G (numpy.ndarray): The train image.

    Returns:
        - adPoints: The adPoints updated with the estimated deformation model coefficients.
    """
    # Normalize the images to be in the range 0-255 - this is needed for
    # the AKAZE algorithm
    origTrainImg = cv.normalize(
        G, None, 0, 255, cv.NORM_MINMAX).astype('uint8')
    origQueryImg = cv.normalize(
        F, None, 0, 255, cv.NORM_MINMAX).astype('uint8')

    # Setup the akaze detector
    akaze = cv.AKAZE_create()

    # Subset data to work with
    X = adPoints[:, :, CompID.XCoordID]
    Y = adPoints[:, :, CompID.YCoordID]
    SS = adPoints[:, :, CompID.SSSizeID].astype(int)
    rows, cols = X.shape

    # Now detect the keypoints in each subset and compute the descriptors for the
    # query image and train image for all the subsets
    # Loop through all the points and perform Akaze detection for each
    for iRow in range(rows):
        for iCol in range(cols):

            # Get Subset info and reset the size factor
            x, y, subSetSize = X[iRow, iCol], Y[iRow, iCol], SS[iRow, iCol]
            sizeFactor = FloatConst.SIZE_FACTOR

            # Get the keypoints in the query image - keep increasing the subset size until
            # we have enough keypoints
            for _ in range(IntConst.AKAZE_MIN_PNTS):

                # Setup the subset bounds - we use twice the subset size to
                # increase the number of keypoints we detect
                hw = sizeFactor*(subSetSize - 1) / 2
                yMin = max(0, int(y - hw))
                yMax = min(int(y + hw), origQueryImg.shape[0])
                xMin = max(0, int(x - hw))
                xMax = min(int(x + hw), origQueryImg.shape[1])

                # Slice the query image around the current subset from F
                trainImg = origTrainImg[yMin:yMax, xMin:xMax]
                queryImg = origQueryImg[yMin:yMax, xMin:xMax]

                # Detect the keypoints and compute the descriptors
                try:
                    kpG, descG = akaze.detectAndCompute(trainImg, None)
                    kpQ, descQ = akaze.detectAndCompute(queryImg, None)
                except Exception:
                    # If we cannot detect keypoints, we will just continue to the next
                    # iteration and try with a larger subset size
                    kpG, descG = [], None
                    kpQ, descQ = [], None

                if descQ is not None and descG is not None \
                        and len(kpQ) > IntConst.AKAZE_MIN_PNTS \
                        and len(kpG) > IntConst.AKAZE_MIN_PNTS:
                    break
                sizeFactor += 1

            # Match keypoints if possible
            if descQ is None or descG is None or len(kpQ) == 0 or len(kpG) == 0:
                adPoints[iRow, iCol, CompID.XDispID:] = 0.0
                continue

            # Setup the matcher to detect keypoint matches in the query and G images
            try:
                matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
                matches = matcher.match(descQ, descG)  # query then train

                # Store the x and y coordinates of the keypoints
                nTop = len(matches)
                coordQ = np.zeros([2, nTop])
                coordG = np.zeros([2, nTop])
                for idx, m in enumerate(matches[:nTop]):
                    coordQ[:, idx] = kpQ[m.queryIdx].pt[:]
                    coordG[:, idx] = kpG[m.trainIdx].pt[:]

                # Do a ransac to find the best affine transformation based on the
                # keypoint coordinates stored in coordQ and coordG
                model_robust, _ = sk.measure.ransac((coordQ.T, coordG.T),
                                                    sk.transform.AffineTransform,
                                                    min_samples=3, residual_threshold=2,
                                                    max_trials=100)

                # Get the affine transformation homography coefficients
                adPoints[iRow, iCol, CompID.XDispID +
                         0] = model_robust.params[0][2]
                adPoints[iRow, iCol, CompID.XDispID +
                         1] = model_robust.params[0][0] - 1.0
                adPoints[iRow, iCol, CompID.XDispID +
                         2] = model_robust.params[0][1]

                adPoints[iRow, iCol, CompID.YDispID +
                         0] = model_robust.params[1][2]
                adPoints[iRow, iCol, CompID.YDispID +
                         1] = model_robust.params[1][0]
                adPoints[iRow, iCol, CompID.YDispID +
                         2] = model_robust.params[1][1] - 1.0

            except Exception:
                adPoints[iRow, iCol, CompID.XDispID:] = 0.0

    return adPoints


# --------------------------------------------------------------------------------------------
def _referenceSubSetInfo_(F, delF, x0, y0, subSetSize, subSetIndices=None):
    """
    Extracts subset information from the reference image that is needed as part of the
    optimizatn run.  This inclue the subset intensity values, the mean intensity, the
    normalized sum of squared differences, and the gradient information.

    Parameters:
    - F: numpy.ndarray
        The mother image.
    - delF: tuple of numpy.ndarray
        The gradient information of the mother image. delF[0] represents the gradient in
        the y-direction (Fy), and delF[1] represents the gradient in the x-direction (Fx).
        If None no gradient information is extracted.
    - x0: int
        The x-coordinate of the subset center.
    - y0: int
        The y-coordinate of the subset center.
    - subSetSize: int
        The size of the subset.
    - subSetIndices: numpy.ndarray or None
        An optional array of indices to select a subset of points from the full subset.
        If None, all points in the subset are used.

    Returns:
    - f: numpy.ndarray
        The reference subset intensity values extracted from the mother image.
    - f_mean: float
        The average subset intensity.
    - f_tilde: float
        The normalized sum of squared differences of the subset intensity values.
    - dfdx: numpy.ndarray
        The gradient in the x-direction (Fx) of the subset.
    - dfdy: numpy.ndarray
        The gradient in the y-direction (Fy) of the subset.
    """
    # Get the upper and lower bound that define the subset in the
    # reference image
    bound = int(0.5*(subSetSize-1))

    # Extract  reference subset intensity values, f, from mother image, F,
    f = F[y0-bound:y0+bound+1, x0-bound:x0+bound+1]
    f = f.reshape(-1, 1, order='F')
    if subSetIndices is not None:
        f = f[subSetIndices]

    # Extract the gradient information
    # Note: Fy = delF[0], Fx = delF[1]
    # Check if delF is None - this will be the case if we are
    if (delF is not None):
        dfdy = delF[0][y0-bound:y0+bound+1, x0-bound:x0+bound+1]
        dfdy = dfdy.reshape(-1, order='F')
        if subSetIndices is not None:
            dfdy = dfdy[subSetIndices]

        dfdx = delF[1][y0-bound:y0+bound+1, x0-bound:x0+bound+1]
        dfdx = dfdx.reshape(-1, order='F')
        if subSetIndices is not None:
            dfdx = dfdx[subSetIndices]
    else:
        dfdx = dfdy = 0

    # Average subset intensity, and normalised sum of squared differences
    f_mean = f.mean()
    f_tilde = np.linalg.norm(f-f_mean)

    return f, f_mean, f_tilde, dfdx, dfdy


# --------------------------------------------------------------------------------------------
def _getHessianInfo_(dfdx, dfdy, xsi, eta, subSetSize, shapeFn, isNormalized):
    """
    Calculate the Hessian matrix and Jacobian array based on the given inputs.

    Parameters:
    - dfdx (numpy.ndarray): Array of partial derivatives of the function with respect to x.
    - dfdy (numpy.ndarray): Array of partial derivatives of the function with respect to y.
    - xsi (numpy.ndarray): Array of xsi values.
    - eta (numpy.ndarray): Array of eta values.
    - subSetSize (int): Size of the subset.
    - shapeFn (int): Type of shape functions to use.
    - isNormalized (bool): Indicates whether the coordinates are normalized.

    Returns:
    - hessian (numpy.ndarray): The Hessian matrix.
    - jacobian (numpy.ndarray): The Jacobian array.
    """

    # Normalize the coordinates if requested
    if isNormalized:
        K = 0.5*(subSetSize-1)
        xsi = xsi/K
        eta = eta/K

    # Affine transformation
    if shapeFn == ShapeFN.AFFINE:
        jacobian = np.column_stack([dfdx,
                                    dfdx*xsi,
                                    dfdx*eta,
                                    dfdy,
                                    dfdy*xsi,
                                    dfdy*eta])

    elif shapeFn == ShapeFN.QUADRATIC:
        jacobian = np.column_stack([dfdx,
                                    dfdx*xsi,
                                    dfdx*eta,
                                    0.5*dfdx*xsi**2,
                                    dfdx*xsi*eta,
                                    0.5*dfdx*eta**2,
                                    dfdy,
                                    dfdy*xsi,
                                    dfdy*eta,
                                    0.5*dfdy*xsi**2,
                                    dfdy*xsi*eta,
                                    0.5*dfdy*eta**2])
    else:
        raise ValueError(
            'Invalid ShapeFunctions value. Only supported values are: Affine | Quadratic')

    # Setup the Hessian as the dot product of the Jacobian array with its transpose
    hessian = jacobian.T @ jacobian

    return hessian, jacobian


# --------------------------------------------------------------------------------------------
def _relativeDeformedCoords_(p, xsi, eta, shapeFn):
    """
    Calculates the relative deformed image subset coordinates based on the given
    shape functions at the current iteration.

    Parameters:
     - p (list): The subset warp coefficients.
     - xsi (float): The local xsi coordinate.
     - eta (float): The locla eta coordinate.
     - shapeFn (int): The type of deformation model.

    Returns:
     - tuple: The calculated xsi_d and eta_d coordinates.

    Raises:
     - ValueError: If an invalid shapeFns value is provided.
    """
    # Check for invalid models
    if np.isnan(p).any():
        xsi_d = xsi
        eta_d = eta

    # Affine model
    elif shapeFn == ShapeFN.AFFINE:
        # Displacement, stretch and shear subset in xy-coordinates (Affine):
        # Order of SFP's p[j]: 0   1   2   3   4   5   6   7   8
        #                      u   ux  uy              v   vx  vy
        xsi_d = (1+p[1])*xsi + p[2]*eta + p[0]
        eta_d = p[7]*xsi + (1+p[8])*eta + p[6]

    # Quadratic model
    elif shapeFn == ShapeFN.QUADRATIC:
        # order of SFP's p[j]: 0   1   2   3   4   5   6   7   8   9   10   11
        #                      u   ux  uy  uxx uxy uyy v   vx  vy  vxx vxy  vyy

        xsiSquared = xsi*xsi
        etaSquared = eta*eta
        xsiEta = xsi*eta

        xsi_d = 0.5*p[3]*xsiSquared + p[4]*xsiEta + 0.5 * \
            p[5]*etaSquared + (1+p[1])*xsi + p[2]*eta + p[0]
        eta_d = 0.5*p[9]*xsiSquared + p[10]*xsiEta + 0.5 * \
            p[11]*etaSquared + p[7]*xsi + (1+p[8])*eta + p[6]

    # Invalid model
    else:
        raise ValueError(
            'Invalid ShapeFunctions value. Only supported values are: Affine | Quadratic')

    return xsi_d, eta_d


# --------------------------------------------------------------------------------------------
def _deformedSubSetInfo_(GInter, x0, y0, xsi_d, eta_d):
    """
    Calculate deformed subset intensity information.  We use the same function for the
    datum and deformed image subsets.  For the datum image the interpolation function is
    just the image itself.

    Parameters:
    - GInter: A function that interpolates the intensity values from the mother
        image at sub-pixel coordinates. For the datum image this is just the image itself.
    - x0: The x-coordinate of the original subset.
    - y0: The y-coordinate of the original subset.
    - eta_d: The displacement in the y-direction of the deformed subset.
    - xsi_d: The displacement in the x-direction of the deformed subset.

    Returns:
    - g: The deformed subset intensity values.
    - g_mean: The average intensity value of the deformed subset.
    - g_tilde: The normalized sum of squared differences of the deformed subset.
    """
    # Deformed subset coordinates
    yd = y0 + eta_d
    xd = x0 + xsi_d

    # --------------------------------------------------------------
    # -- Build-in interpolation function in Python
    # g = GInter.ev(yd.reshape(nRows, 1), xd.reshape(nRows, 1))
    # --------------------------------------------------------------
    g = GInter(yd.reshape(-1, 1), xd.reshape(-1, 1))

    # Determine average intensity value of subset g,
    # and normalised sum of squared differences of subset, g_tilde
    g_mean = g.mean()
    g_tilde = np.linalg.norm(g-g_mean)

    return g, g_mean, g_tilde


# --------------------------------------------------------------------------------------------
def _isConverged_(convergenceThreshold, nzccThreshold, deltaP, nzssd):
    """
    Check if the optimizatin has converged based on the given convergence criteria,
    current data_p and shape functions.

    Parameters:
     - convergenceThreshold (float): The threshold value for convergence.
     - nzccThreshold (float): The threshold value for the nzcc value.
     - delta_p (float): The change in displacement field.
     - cnzssd (float): The current CZNSSD value.

    Returns:
     - bool: True if the optimizatin field has converged, False otherwise.
    """

    # Map the indices to use for the convergence check.  We ultimately only look at the
    # L2 norm of the two displacement components - indices 0 and 6 in the deltaP array
    idx = np.zeros(deltaP.shape, dtype=np.bool_)
    idx[0] = True
    idx[6] = True

    # Calculate the delta disp
    exitCriteria = np.linalg.norm(deltaP[idx])

    # Calculate the NZCC value
    nzcc = 1.0 - 0.5*nzssd

    # Perform the convergence check
    return (exitCriteria < convergenceThreshold) or (nzcc > nzccThreshold)


# --------------------------------------------------------------------------------------------
def _modelCoeffUpdate_(p, dp, shapeFn):
    """
    Update the model coefficients based on the results from the current Gauss Newton  or
    Levenberg-Marquardt iteration.

    Parameters:
    - p: array-like
        Current estimate of the model coefficients.
    - dp: array-like
        Update to the model coefficients.
    - shapeFns: int
        Type of shape functions to use.

    Returns:
    - subset_coefficients: array-like
        Updated model coefficients.

    Raises:
    - ValueError: If the `shapeFns` value is not 'Affine' or 'Quadratic'.
    """

    # Update the model coefficients based on the current estimate and the shape functions
    if shapeFn == ShapeFN.AFFINE:
        # w of current estimate of SFPs
        # order of SFP's P[1]: 0   1   2   3   4   5   6   7   8
        #                      u   ux  uy              v   vx  vy
        w_P = np.array([[1+p[1],   p[2], p[0]],
                        [p[7], 1+p[8], p[6]],
                        [0,      0,    1]]).astype('double')

        # w of current delta_p
        w_dP = np.array([[1+dp[1],   dp[2], dp[0]],
                         [dp[7], 1+dp[8], dp[6]],
                         [0,       0,    1]]).astype('double')

        # p coefficients compositional update matrix
        up = np.linalg.solve(w_dP, w_P)

        # extract updated coefficients from p update/up matrix
        subset_coefficients = np.array([up[0, 2],
                                        up[0, 0]-1,
                                        up[0, 1],
                                        0.,
                                        0.,
                                        0.,
                                        up[1, 2],
                                        up[1, 0],
                                        up[1, 1]-1,
                                        0.,
                                        0.,
                                        0.])

    elif shapeFn == ShapeFN.QUADRATIC:
        # order of SFP's P[j]: 0   1   2   3   4   5   6   7   8   9   10   11
        #                      u   ux  uy  uxx uxy uyy v   vx  vy  vxx vxy  vyy
        A1 = 2*p[1] + p[1]**2 + p[0]*p[3]
        A2 = 2*p[0]*p[4] + 2*(1+p[1])*p[2]
        A3 = p[2]**2 + p[0]*p[5]
        A4 = 2*p[0]*(1+p[1])
        A5 = 2*p[0]*p[2]
        A6 = p[0]**2
        A7 = 0.5*(p[6]*p[3] + 2*(1+p[1])*p[7] + p[0]*p[9])
        A8 = p[2]*p[7] + p[1]*p[8] + p[6]*p[4] + p[0]*p[10] + p[8] + p[1]
        A9 = 0.5*(p[6]*p[5] + 2*(1+p[8])*p[2] + p[0]*p[11])
        A10 = p[6] + p[6]*p[1] + p[0]*p[7]
        A11 = p[0] + p[6]*p[2] + p[0]*p[8]
        A12 = p[0]*p[6]
        A13 = p[7]**2 + p[6]*p[9]
        A14 = 2*p[6]*p[10] + 2*p[7]*(1+p[8])
        A15 = 2*p[8] + p[8]**2 + p[6]*p[11]
        A16 = 2*p[6]*p[7]
        A17 = 2*p[6]*(1+p[8])
        A18 = p[6]**2

        # entries of w for update
        dA1 = 2*dp[1] + dp[1]**2 + dp[0]*dp[3]
        dA2 = 2*dp[0]*dp[4] + 2*(1+dp[1])*dp[2]
        dA3 = dp[2]**2 + dp[0]*dp[5]
        dA4 = 2*dp[0]*(1+dp[1])
        dA5 = 2*dp[0]*dp[2]
        dA6 = dp[0]**2
        dA7 = 0.5*(dp[6]*dp[3] + 2*(1+dp[1])*dp[7] + dp[0]*dp[9])
        dA8 = dp[2]*dp[7] + dp[1]*dp[8] + dp[6] * \
            dp[4] + dp[0]*dp[10] + dp[8] + dp[1]
        dA9 = 0.5*(dp[6]*dp[5] + 2*(1+dp[8])*dp[2] + dp[0]*dp[11])
        dA10 = dp[6] + dp[6]*dp[1] + dp[0]*dp[7]
        dA11 = dp[0] + dp[6]*dp[2] + dp[0]*dp[8]
        dA12 = dp[0]*dp[6]
        dA13 = dp[7]**2 + dp[6]*dp[9]
        dA14 = 2*dp[6]*dp[10] + 2*dp[7]*(1+dp[8])
        dA15 = 2*dp[8] + dp[8]**2 + dp[6]*dp[11]
        dA16 = 2*dp[6]*dp[7]
        dA17 = 2*dp[6]*(1+dp[8])
        dA18 = dp[6]**2

        # order of SFP's P[j]: 0   1   2   3   4   5   6   7   8   9   10   11
        #                      u   ux  uy  uxx uxy uyy v   vx  vy  vxx vxy  vyy
        # w of current estimate of SFP's
        w_P = np.array([[1+A1,    A2,        A3,     A4,     A5,   A6],
                        [A7,  1+A8,        A9,    A10,    A11,  A12],
                        [A13,   A14,     1+A15,    A16,    A17,  A18],
                        [0.5*p[3],  p[4],  0.5*p[5], 1+p[1],   p[2], p[0]],
                        [0.5*p[9], p[10], 0.5*p[11],   p[7], 1+p[8], p[6]],
                        [0,     0,         0,      0,      0,    1]
                        ]).astype('double')

        # w of current deltaP
        w_dP = np.array([[1+dA1,    dA2,        dA3,     dA4,     dA5,   dA6],
                         [dA7,  1+dA8,        dA9,    dA10,    dA11,  dA12],
                         [dA13,   dA14,     1+dA15,    dA16,    dA17,  dA18],
                         [0.5*dp[3],  dp[4],  0.5*dp[5], 1+dp[1],   dp[2], dp[0]],
                         [0.5*dp[9], dp[10], 0.5*dp[11],   dp[7], 1+dp[8], dp[6]],
                         [0,      0,          0,       0,       0,     1]
                         ]).astype('double')

        # P update matrix
        up = np.linalg.solve(w_dP, w_P)
        subset_coefficients = np.array([up[3, 5],
                                        up[3, 3]-1,
                                        up[3, 4],
                                        2*up[3, 0],
                                        up[3, 1],
                                        2*up[3, 2],
                                        up[4, 5],
                                        up[4, 3],
                                        up[4, 4]-1,
                                        2*up[4, 0],
                                        up[4, 1],
                                        2*up[4, 2]])

    else:
        raise ValueError(
            'Invalid ShapeFunctions value. Only supported values are: Affine | Quadratic')

    return subset_coefficients


# --------------------------------------------------------------------------------------------
def _fastInterpolation_(image, interOrder):
    """
    Setup the interpolation model for the given image.  A special
    interpolation method is called that is optimized for interpolation
    of images (that is regular grids).  This integrator is sinificantly
    faster than the scipy methods, eg map_coordinates.

    Parameters:
    - image (ndarray): The input image to be interpolated.
    - interOrder (int): The order of the interpolation to be used.

    Returns:
    - imgInter (interp2d): The interpolation model that can be called in
        the future for interpolation.
    """
    # Image dimensions
    ny = image.shape[0]
    nx = image.shape[1]

    # Setup the interpolation model that can be called in future whenever
    # interpolation is required
    # --------------------------------------------------------------
    # -- Build in interpolator from scipy
    # X = np.arange(0, nx)
    # Y = np.arange(0, ny)
    # imgInter = RectBivariateSpline(Y, X, image, kx=3, ky=3)
    # --------------------------------------------------------------
    imgInter = interp2d([0, 0], [ny-1, nx-1], [1, 1], image,
                        k=interOrder, p=[False, False], c=[True, True], e=[1, 1])

    return imgInter


# --------------------------------------------------------------------------------------------
def _calcCZNSSD_(nBGCutOff, f, f_mean, f_tilde, g, g_mean, g_tilde):
    """
    Calculate the CZNSSD value for the given subset intensity values.

    Parameters:
        - nBGCutOff (int): The background cutoff value.
        - f (numpy.ndarray): The reference subset intensity values.
        - f_mean (float): The average intensity value of the reference subset.
        - f_tilde (float): The normalized sum of squared differences of the reference subset.
        - g (numpy.ndarray): The deformed subset intensity values.
        - g_mean (float): The average intensity value of the deformed subset.
        - g_tilde (float): The normalized sum of squared differences of the deformed subset.

    Returns:
        - float: The CZNSSD value for the given subset intensity values.
    """
    # Deal with cases where the image is all black
    if (f_mean < nBGCutOff) or (g_mean < nBGCutOff):
        return IntConst.CNZSSD_MAX

    # Otherwise calculate the CZNSSD value
    tmpArray = (f - f_mean) / f_tilde - (g - g_mean) / g_tilde
    return np.sum(tmpArray * tmpArray)


# -----------------------------------------------------------------------------
def _factorCPUCount_(n, r):
    """Calculate the two factors of integer n, that are closest to the ratio r.

    Parameters:
        n (int): The integer to be factored.
        r (float): The ratio to be used for comparison.

    Returns:
        tuple: A tuple containing the two factors of n that are closest to the ratio r.
    """

    # Check if n is an integer
    if n//1 != n:
        raise TypeError("n must be an integer.")

    # Set up variables
    i = prevF1 = prevF2 = 0
    prevDiff = m.inf

    # Find all factors of n up to the square root of n.  Then compare with
    # the given ratio r.  If the ratio is closer to r than the previous ratio
    # then save the factors.  Else break the loop.
    while i <= n:

        i = i + 1

        # Factor found
        if (n % i == 0):
            f1 = i
            f2 = n//i
            diff = m.fabs(r - f1/f2)

            # Difference is still getting smaller
            if (diff < prevDiff):
                prevDiff = diff
                prevF1 = f1
                prevF2 = f2

            # Difference is getting larger so break out
            else:
                break

    return (prevF1, prevF2)


# -----------------------------------------------------------------------------
def _splitMatrix_(matrix, rowSplit, colSplit):
    """
    Splits a matrix into submatrices based on the given number of rows and
    colums to split into.

    Args:
        matrix (numpy.ndarray): The input matrix to be split.
        rowSplit (int): The number of splits to be made along the rows.
        colSplit (int): The number of splits to be made along the columns.

    Returns:
        list: A list of submatrices obtained after splitting the input matrix.
    """
    subMatrices = []

    # Split the rows
    rows = np.array_split(matrix, rowSplit, axis=0)

    # Now loop through all the rows and split the columns
    for r in rows:
        cols = np.array_split(r, colSplit, axis=1)
        subMatrices.append(cols)

    return subMatrices


# --------------------------------------------------------------------------------------------
def _fillMissingData_(dataX, dataY, dataVal):
    """
    Fill missing data values (specificall NaN's) using linear interpolation.

    Parameters:
      - dataX (numpy.ndarray): Array of x-coordinates.
      - dataY (numpy.ndarray): Array of y-coordinates.
      - dataVal (numpy.ndarray): Array of data values.

    Returns:
      - numpy.ndarray: Array of data values with missing values filled using
        linear interpolation.
    """

    # Check if there are NaN values to interpolate
    if np.isnan(dataVal).any():

        # Get a mask for the values that are not NaN
        mask = ~np.isnan(dataVal)

        # Setup the nearest neighbour interpolator
        interp = NearestNDInterpolator(
            list(zip(dataX[mask], dataY[mask])), dataVal[mask])

        # Interpoloate all nan values
        dataVal[~mask] = interp(dataX[~mask], dataY[~mask])

    return dataVal


# ---------------------------------------------------------------------------------------------
def readImage(imgFile, normalize8Bit=False):
    """
    Read an image file and convert it to grayscale.

    Parameters:
        imgFile (str): The path to the image file.

    Returns:
        numpy.ndarray: The grayscale image.
    """
    # Read the image as is - allow for eg for 16-bit images
    try:
        img = cv.imread(imgFile, cv.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError(
                f"Image file {imgFile} not found, cannot be read or is not a valid image file.")

        # Convert to grayscale if color image - will only work with grayscale images
        if len(img.shape) == 3:
            grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        else:
            grayImg = img

    except Exception as e:
        raise RuntimeError(f"Error reading image file {imgFile}: {e}")

    # Use the full range of the image bitrange but keep the same data type
    imgDType = grayImg.dtype
    maxValue = np.iinfo(imgDType).max
    ratio = np.amax(grayImg) / maxValue
    grayImg = (grayImg/ratio).astype(imgDType)

    # # Normalize the image to be in the range 0-255 - useful for displaying the image
    if normalize8Bit:
        grayImg = cv.normalize(grayImg, None, 0, 255,
                               cv.NORM_MINMAX).astype('uint8')

    return grayImg


# ---------------------------------------------------------------------------------------------
def _safeRayInit_(externalRay, nCpus, debugLevel=0):
    """
    Initialize the ray environment with retries to make it more robust.

    Parameters:
        externalRay (bool): Whether to use an external ray instance.
        nCpus (int): The number of CPUs to use.
        debugLevel (int): The debug level for logging.

    Returns:
        ray (Ray): The initialized ray instance.
    """

    nRetry = 3  # Number of retries

    # Try to start ray with retries
    for i in range(nRetry):  # Retry a few times
        try:
            if not externalRay:
                return ray.init(num_cpus=nCpus)
            else:
                return ray.init(address="auto", ignore_reinit_error=True)
        except Exception as e:
            if debugLevel > 0:
                print(f"Ray init failed: {e}, retrying ({i+1}/{nRetry})...")
            time.sleep(2)

    raise RuntimeError(f"Ray failed to initialize after {nRetry} retries")


# ---------------------------------------------------------------------------------------------
def _safeRayLaunch_(func, debugLevel=0):
    """
    Launch a Ray task with retries to make it more robust.

    Parameters:
        func (Ray task): The Ray task to be launched.
        debugLevel (int): The debug level for logging.

    Returns:
        result (any): The result of the Ray get function.
    """

    nRetry = 3  # Number of retries

    # Try to launch the task with retries
    for i in range(nRetry):
        try:
            return ray.get(func)
        except Exception as e:
            if debugLevel > 0:
                print(
                    f"Ray task launch failed: {e}, retrying ({i+1}/{nRetry})...")
            time.sleep(1)

    raise RuntimeError(f"Ray task failed to initialize after {nRetry} retries")


# ---------------------------------------------------------------------------------------------
def _safeRayShutdown_(externalRay, debugLevel=0):
    """
    Shutdown the Ray environment with retries to make it more robust.

    Parameters:
        externalRay (bool): Whether to use an external ray instance.
        debugLevel (int): The debug level for logging.

    Returns:
        None
    """

    nRetry = 3  # Number of retries

    # Try to shutdown ray with retries
    for i in range(nRetry):
        try:
            if not externalRay:
                ray.shutdown()
            return
        except Exception as e:
            if debugLevel > 0:
                print(
                    f"Ray shutdown failed: {e}, retrying ({i+1}/{nRetry})...")
            time.sleep(1)

    print(
        f"Ray shutdown ultimately failed after {nRetry} retries. Will continue.")


# ---------------------------------------------------------------------------------------------
def _convertShapeFn_(shapeFn):
    """
    Convert the shape function to an integer value.  The argument (shapeFn) could be a scalar
    or a numpy array

    Parameters:
        shapeFn (str): The shape function as a string.

    Returns:
        int: The corresponding integer value for the shape function.
    """

    # Convert the shape function to an integer numpy array if it is a numpy array
    if isinstance(shapeFn, np.ndarray):

        retArray = 100*np.ones_like(shapeFn, dtype=int)
        retArray[shapeFn == 'Affine'] = ShapeFN.AFFINE
        retArray[shapeFn == 'Quadratic'] = ShapeFN.QUADRATIC

        # Check if there are any invalid values
        if np.any(retArray == 100):
            raise ValueError(
                'Invalid ShapeFunctions value. Only supported values are: Affine | Quadratic')

        return retArray

    # Convert the shape function to an integer value when a scalar
    else:
        if shapeFn == 'Affine':
            return ShapeFN.AFFINE
        elif shapeFn == 'Quadratic':
            return ShapeFN.QUADRATIC
        else:
            raise ValueError(
                'Invalid ShapeFunctions value. Only supported values are: Affine | Quadratic')
