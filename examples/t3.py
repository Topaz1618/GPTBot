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
    edges = cv2.Canny(gray, 50, 50)

    # 使用霍夫直线变换检测直线
    lines = cv2.HoughLinesP(edges, 1, np.pi / 100, threshold=200, minLineLength=160, maxLineGap=5)

    table_borders = []

    # 处理检测到的直线
    if lines is not None:

        for idx, line in enumerate(lines):
            x1, y1, x2, y2 = line[0]
            table_borders.append((x1, y1, x2, y2))

            # 在图像上绘制直线
            if x1 and x2 and y1 and y2:
                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

                # 在图像上标记点和坐标
                cv2.circle(image, (x1, y1), 5, (0, 0, 255), -1)
                cv2.circle(image, (x2, y2), 5, (0, 0, 255), -1)

                cv2.putText(image, f'({x1}, {y1})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
                            cv2.LINE_AA)

                cv2.putText(image, f'({x2}, {y2})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
                            cv2.LINE_AA)

    return table_borders, image


# 指定图像文件的路径
image_path = 'output_1.png'

# 检测表格边框并获取坐标信息及标记的图像
table_borders, marked_image = detect_table_borders(image_path)

# 打印表格边框的坐标信息
for idx, border in enumerate(table_borders):
    x1, y1, x2, y2 = border
    print(f"Idx: {idx} X1: {x1}, Y1: {y1}, X2: {x2}, Y2: {y2}")

# 显示标记的图像
cv2.imwrite("marked.png", marked_image)
# cv2.imshow('Marked Image', marked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()