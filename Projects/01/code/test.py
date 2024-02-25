import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cv2
#
import utils
from utils import *
width, height = 300, 400
img = utils.get_input("pic.jpg")
# img.show()
# mat = np.zeros(3)
# mat.fill(0.33)
#
# pts1 = np.float32([[263, 21], [592, 180], [246, 973], [623, 897]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# t = getPerspectiveTransform(pts1, pts2)
# warpedImage = warpPerspective(image_matrix, m, width, height)
# showWarpPerspective()
# print(m)
# arr = np.ones((3, 1))
# print(arr)
# mat = np.ones((3, 3))
# mat.fill(2)
# print(mat)
# arr = np.matmul(mat,arr)
# print(arr)

# new_image_map = {}
# minx, miny = img.shape[0], img.shape[1]
# maxx, maxy = 0, 0
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#             xy = np.array([i, j, 1], np.float64)
#             uv = np.matmul(t, xy)
#             uv = uv / uv[2]
#             minx = min(minx, uv[0])
#             maxx = max(maxx, uv[0])
#             miny = min(miny, uv[1])
#             maxy = max(maxy, uv[1])
#
#             new_image_map[int(uv[0]), int(uv[1])] = (i, j)
#
# minx, miny = int(minx), int(miny)
# maxx, maxy = int(maxx), int(maxy)
# final_img = np.zeros((maxx - minx + 1, maxy - miny + 1), dtype=np.int) \
#         if len(img.shape) == 2 else np.zeros((maxx - minx + 1, maxy - miny + 1, img.shape[2]), dtype=np.int)
#
# for k, v in new_image_map.items():
#         final_img[k[0] - minx, k[1] - miny] = img[v]

# showWarpPerspective(img)
# showWarpPerspective(final_img)



# showWarpPerspective(dst)

# transform_matrix = np.array([[1],
#                              [0],
#                              [0]])

# print(transform_matrix)
# Filter(img, gray_transform_matrix)
# img = utils.Filter(img, transform_matrix)
# utils.showImage(img, "nigger", False)
# print(img[263][21])
# print(img[263][21][1])
# print(img[263][21][2])
# print(img)
# s, h, l = img.shape
# print(s)
# print(h)
# print(l)
# arr = np.arange(12).reshape((4, 3))
# print(arr)

# gray_transform_matrix = np.zeros(3)
# gray_transform_matrix.fill(0.333)
# print(gray_transform_matrix)
# # print("before filter")
# for i in range(5):
#     for j in range(5):
#         print(gray_transform_matrix)
# img =Filter(img, gray_transform_matrix)/
#
#
# arr1 = np.ones(3)
# arr2 = np.ones(1)
# arr3 = np.ones((1, 3))
# arr4 = np.ones((3, 1))
# print(arr1)
# # print(arr2)
# print(arr3)
# print(arr3[0])
#
# print(arr3[1])
# print(arr4)
# arr1 = np.ones(3)
# arr1.fill(2)
# arr2 = np.ones((3,1))
# arr2.fill(4)
# print(arr1)
# print(arr2)
# print(arr1.dot(arr2))
# arr12 = np.array([[0, 0, 1],
#                   [0, 1, 0],
#                   [1, 0, 0]])
# img = Filter(img, arr12)
# showImage(img, "nigger", False)
# print(img[10][12])
# width, height = 300, 400
# w, h, z = img.shape
# print(w, h, z)
# newW, newH = 3*w, 4*h
# res = np.zeros((newW, newH, img.shape[2]))
# for i in range(newW):
#     for j in range(newH):
#         res[i][j] = img[i//3][j//4]
# showImage(res, "nigger2", False)
# print(138//2)
# print(139//2)
# print(140//2)

