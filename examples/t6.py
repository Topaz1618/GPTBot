import math
import cv2
import numpy as np

image = cv2.imread("output_1.png")



gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
kernel_horizontal = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 6))
dilated_image_A = cv2.dilate(binary_image, kernel_horizontal, iterations=1)

# resized_image = cv2.resize(dilated_image_A, (0, 0), fx=0.5, fy=0.5)
cv2.imwrite("dilated_image_A.png", dilated_image_A)

# inverted_image_A = cv2.imread("inverted_image_A.png", cv2.IMREAD_GRAYSCALE)

inverted_image_A = cv2.bitwise_not(dilated_image_A)
cv2.imwrite("inverted_image_A.png", inverted_image_A)

edges_A = cv2.Canny(inverted_image_A, 50, 150)
lines_A = cv2.HoughLinesP(edges_A, 1, np.pi/180, threshold=100, minLineLength=70, maxLineGap=10)


for line_A in lines_A:
    x1, y1, x2, y2 = line_A[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
cv2.imwrite("output_with_lines.png", image)