import cv2
import numpy as np


def get_neighbors_pixel(image: np.ndarray, x: int, y: int, center: int) -> int:
    """
    Comparing local neighborhood pixel value with threshold value of centre pixel.
    Exception is required when neighborhood value of a center pixel value is null.
    i.e. values present at boundaries.

    :param image: The image we're working with
    :param x: x-coordinate of the center pixel
    :param y: The y coordinate of the pixel
    :param center: center pixel value
    :return: The value of the pixel is being returned.
    """

    value = 0

    try:
        if image[x][y] >= center:
            value = 1
    except:

        pass
    return value


def local_binary_value(image: np.ndarray, x: int, y: int) -> int:
    """
    It takes an image, an x and y coordinate, and returns the 
    decimal value of the local binary patternof the pixel 
    at that coordinate

    :param image: the image to be processed
    :param x: x coordinate of the pixel
    :param y: the y coordinate of the pixel
    :return: The decimal value of the binary value of the pixels 
    around the center pixel.
    """
    binary_value = []
    center = image[x][y]
    powers = [1, 2, 4, 8, 16, 32, 64, 128]
    decimal_val = 0

    # Starting from top right,assigning value to pixels clockwise
    binary_value.append(get_neighbors_pixel(image, x - 1, y + 1, center))
    binary_value.append(get_neighbors_pixel(image, x, y + 1, center))
    binary_value.append(get_neighbors_pixel(image, x - 1, y, center))
    binary_value.append(get_neighbors_pixel(image, x + 1, y + 1, center))
    binary_value.append(get_neighbors_pixel(image, x + 1, y, center))
    binary_value.append(get_neighbors_pixel(image, x + 1, y - 1, center))
    binary_value.append(get_neighbors_pixel(image, x, y - 1, center))
    binary_value.append(get_neighbors_pixel(image, x - 1, y - 1, center))

    # Converting the binary value to decimal.
    for i in range(len(binary_value)):
        decimal_val += binary_value[i] * powers[i]

    return decimal_val


if __name__ == "main":

    # Reading the image and converting it to grayscale.
    image = cv2.imread("../image_data/lena.jpg", cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Original Image", image)

    # Create a numpy array as the same height and width of read image
    lbp_image = np.zeros((image.shape[0], image.shape[1]))

    # Iterating through the image and calculating the 
    # local binary pattern value for each pixel.
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            lbp_image[i][j] = local_binary_value(image, i, j)

    cv2.imshow("Local Binary Pattern", lbp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
