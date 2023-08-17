import cv2
import numpy as np

# 读取原始图像
# image = cv2.imread("output_1.png")

image = cv2.imread("output_1.png")

print(image)
#转换为灰度图
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# # 将图像转换为灰度图像
# gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
#
# # 对图像进行边缘检测
# edges = cv2.Canny(gray, 50, 50)
#
# # 使用霍夫直线变换检测直线
# lines = cv2.HoughLinesP(edges, 1, np.pi / 100, threshold=200, minLineLength=160, maxLineGap=5)
#
# table_borders = []
#
# # 处理检测到的直线
# if lines is not None:
#
#     for idx, line in enumerate(lines):
#         x1, y1, x2, y2 = line[0]
#         table_borders.append((x1, y1, x2, y2))
#
#         # 在图像上绘制直线
#         if x1 and x2 and y1 and y2:
#             cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
#             # 在图像上标记点和坐标
#             cv2.circle(image, (x1, y1), 5, (0, 0, 255), -1)
#             cv2.circle(image, (x2, y2), 5, (0, 0, 255), -1)
#
#             cv2.putText(image, f'({x1}, {y1})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
#                         cv2.LINE_AA)
#
#             cv2.putText(image, f'({x2}, {y2})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
#                         cv2.LINE_AA)
#
