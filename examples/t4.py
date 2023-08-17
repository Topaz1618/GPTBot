import math
import cv2
import numpy as np

image = cv2.imread("output_1.png")

#转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
kernel_horizontal = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 4))
dilated_image_A = cv2.dilate(binary_image, kernel_horizontal, iterations=2)

cv2.imwrite("dilated_image_A.png", dilated_image_A)
inverted_image_A = cv2.bitwise_not(dilated_image_A)
cv2.imwrite("inverted_image_A.png", inverted_image_A)

kernel_vertical = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
dilated_image_B = cv2.dilate(binary_image, kernel_vertical, iterations=2)

cv2.imwrite("dilated_image_B.png", dilated_image_B)

inverted_image_B = cv2.bitwise_not(dilated_image_B)


cv2.imwrite("inverted_image_B.png", inverted_image_B)


# Todo: 检测 A 图片的线， 检测 B 图片的线，获取坐标，在原图上划线