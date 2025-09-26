import cv2
import numpy as np


def filtration_box(img, filter_size):
    """Filter image noise using box blur algorithm.

    Parameters
    ----------
    img : numpy.ndarray
        Input image.
    filter_size : int
        Size of box blur filter.

    Returns
    -------
    Output image.

    """
    return cv2.blur(img, (filter_size, filter_size))


def filtration_median(img, filter_size):
    """Filter image noise using median blur algorithm.

    Parameters
    ----------
    img : numpy.ndarray
        Input image.
    filter_size : int
        Odd number - size of median filter.

    Returns
    -------
    Output image.

    """
    return cv2.medianBlur(img, filter_size)


def filtration_gauss(img, filter_size, sigma_x):
    """Filter image noise using Gaussian blur algorithm.

    Parameters
    ----------
    img : numpy.ndarray
        Input image.
    filter_size : int
        Size of Gaussian filter.
    sigma_x : float
        Gaussian kernel standard deviation in the X direction.

    Returns
    -------
    Output image.

    """
    return cv2.GaussianBlur(img, (filter_size, filter_size), sigma_x)


def apply_fft(image):
    """Apply FFT on the image.

    Parameters
    ----------
    image : 2D array
        Image to perform FFT on.

    Returns
    -------
    mag_spec : 2D array
        Normalized magnitude spectrum.
    fftcls_shift : 2D array
        Centered product of FFT.

    """
    fftcls = np.fft.fft2(image)
    fftcls_shift = np.fft.fftshift(fftcls)
    mag_spec = 20 * np.log(np.abs(fftcls_shift))
    return cv2.normalize(
        mag_spec, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U
    ), fftcls_shift


def inverse_fft(fft_shift, filter_mask=None):
    """Apply inverse FFT.

    Parameters
    ----------
    fft_shift : 2D array
        Shifted computed FFT
    filter_mask : 2D array
        2D array mask containing 255 and 0 values.

    Returns
    -------
    img_back : 2D array
        Image made by inverse FFT.

    """
    fftshift = np.copy(fft_shift)
    if filter_mask is not None:
        fftshift[filter_mask != 255] = 0

    f_ishift = np.fft.ifftshift(fftshift)
    return np.abs(np.fft.ifft2(f_ishift))


def create_filter_mask(size, rows, columns):
    """Create a filter mask specified by rows and columns.

    Specified rows and columns are set to 255, others 0.

    Parameters
    ----------
    size : tuple of int
        Tuple of two integers (height, width) defining the dimensions of the output mask.
    rows : array-like of int
        Indices of rows to set to 255.
    columns : array-like of int
        Indices of columns to set to 255.

    Returns
    -------
    filter_mask : 2D array
        2D array mask containing 255 and 0 values.

    Raises
    ------
    TypeError
        If `size` is not a tuple with 2 int values.

    """
    if not (
        isinstance(size, tuple)
        and len(size) == 2
        and all(isinstance(x, int) for x in size)
    ):
        raise TypeError("Size param must be a tuple of two integers!")

    filter_mask = np.zeros(size, dtype=np.uint8)
    filter_mask[rows] = 255
    filter_mask[:, columns] = 255

    return filter_mask


def filter_mag_spec(mag_spec, filter_mask):
    """Filter input spectrum using filter_mask image.

    Parameters
    ----------
    mag_spec : 2D ndarray
        Image with magnitude spectrum.
    filter_mask : 2D array
        Filter binary mask image containing values to keep (255) and filter out (0).

    Returns
    -------
    result : 2D ndarray
        Vizualization of spectrum after filtering.

    """
    result = np.copy(mag_spec)
    result[filter_mask != 255] = 0

    return result
