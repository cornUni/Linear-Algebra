"""
@author: Amirfazel koozegar kaleji
@student_ID = 9931099
"""
from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    w, h, _ = img.shape
    res = np.zeros((output_width, output_height, img.shape[2]))
    for i in range(w):
        for j in range(h):
            tmp = np.dot(transform_matrix, [i, j, 1])
            i2, j2, _ = (tmp / tmp[2]).astype(int)
            if 0 <= i2 < output_width:
                if 0 <= j2 < output_height:
                    res[i2, j2] = img[i, j]
    return res


def grayScaledFilter(img):
    gray_transform_matrix = np.array([[1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3]])
    return Filter(img, gray_transform_matrix)


def crazyFilter(img):
    crazy_transform_matrix = np.array(
        [[0, 0, 1],
         [0, 0.5, 0],
         [0.5, 0.5, 0]]
    )
    inverted_crazy_matrix = np.linalg.inv(crazy_transform_matrix)
    inverted_crazy_img = Filter(img, crazy_transform_matrix)
    return inverted_crazy_img, Filter(inverted_crazy_img, inverted_crazy_matrix)


def scaleImg(img, scale_width, scale_height):
    w, h, _ = img.shape
    newW, newH = scale_width * w, scale_height * h
    res = np.zeros((newW, newH, img.shape[2]))
    for i in range(newW):
        for j in range(newH):
            res[i][j] = img[i // scale_width][j // scale_height]
    return res


def permuteFilter(img):
    permute_transform_matrix = np.array(
        [[0, 0, 1],
         [0, 1, 0],
         [1, 0, 0]]
    )
    return Filter(img, permute_transform_matrix)


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[263, 21], [592, 180], [246, 973], [623, 897]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage, invertedCrazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")
    showImage(invertedCrazyImage, title="Inverted Crazy Filter")

    scaledImage = scaleImg(warpedImage, 3, 4)
    showImage(scaledImage, title="Scaled Image")

    permuteImage = permuteFilter(warpedImage)
    showImage(permuteImage, title="Permuted Image")
