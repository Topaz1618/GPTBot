"""
Author: Hang Yan
Date created: 2023/8/15
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""


import cv2
import numpy as np


def detect_table_borders(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图像进行边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 使用霍夫直线变换检测直线
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    table_borders = []

    # 处理检测到的直线
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            table_borders.append((x1, y1, x2, y2))

    return table_borders

# 指定图像文件的路径
image_path = 'output_1.png'

# 检测表格边框并获取坐标信息
table_borders = detect_table_borders(image_path)

# 打印表格边框的坐标信息
for border in table_borders:
    x1, y1, x2, y2 = border
    print(f"X1: {x1}, Y1: {y1}, X2: {x2}, Y2: {y2}")