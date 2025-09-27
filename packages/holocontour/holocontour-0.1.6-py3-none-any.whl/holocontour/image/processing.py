import cv2
import numpy as np
from skimage.exposure import match_histograms


def normalize(mask, range_val=255):
    """Normalize an image to a given range."""
    return (range_val * (mask - np.min(mask)) / np.ptp(mask)).astype(np.uint8)


def find_darkest_point(image, mask):
    """Find the darkest pixel within a mask."""
    return np.unravel_index(np.argmin(image[mask]), image.shape)


def apply_histogram_matching(img, ref_path):
    """Match histogram of image to reference."""
    ref = cv2.imread(ref_path, 0)
    matched = match_histograms(img, ref)
    matched = np.clip(matched, img.min(), img.max())
    return matched.astype(img.dtype)


def get_sharpening_kernel(size: int):
    """
    Generate a sharpening kernel of given size (odd number).
    Example:
        size=3 -> [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        size=5 -> 5x5 version with cross neighbors -1
    """
    if size % 2 == 0 or size < 3:
        raise ValueError("Kernel size must be an odd integer >= 3")

    kernel = np.zeros((size, size), dtype=np.float32)

    # Put -1 in cross neighbors
    center = size // 2
    for i in range(size):
        kernel[center, i] = -1   # horizontal line
        kernel[i, center] = -1   # vertical line

    # Set center value (sum of negatives * -1 + 1)
    kernel[center, center] = -np.sum(kernel)

    return kernel


def erode_mask(mask, kernel_size=3, iterations=1):
    """
    Erodes a binary mask using an elliptical kernel.

    Parameters
    ----------
    mask : np.ndarray
        Binary mask (0 and 255 values).
    kernel_size : int
        Size of the elliptical kernel (must be odd, e.g., 3, 5, 7).
    iterations : int
        How many times erosion is applied.

    Returns
    -------
    eroded : np.ndarray
        Eroded binary mask.
    """
    # Ensure kernel size is at least 1 and odd
    kernel_size = max(1, kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1

    # Convert to uint8 0/255
    if mask.dtype == np.bool_:
        mask = mask.astype(np.uint8) * 255
    elif mask.max() <= 1:
        mask = (mask > 0).astype(np.uint8) * 255
    else:
        mask = mask.astype(np.uint8)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    eroded = cv2.erode(mask, kernel, iterations=iterations)

    return eroded > 0