"""
Author: Hang Yan
Date created: 2023/8/15
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

#
# import tabula
# import pandas as pd
#
# # 指定输入PDF文件的路径
# pdf_path = 'input.pdf'
#
# # 指定输出XLSX文件的路径
# xlsx_path = 'output.xlsx'
#
# # 使用tabula库读取PDF文件中的表格数据
# df = tabula.read_pdf(pdf_path, pages='all')
#
# # 将每个页面的表格数据合并为一个数据框
# combined_df = pd.concat(df)
#
# # 将数据保存为XLSX文件
# combined_df.to_excel(xlsx_path, index=False)
#
# print("转换完成！")


import cv2
import numpy as np
import camelot
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path



def draw_point_on_pdf(input_path, output_path, x1, y1, x2, y2):
    # 读取输入PDF文件
    pdf = PdfFileReader(open(input_path, 'rb'))

    # 获取第一页的尺寸
    page = pdf.getPage(0)
    page_width = int(page.mediaBox.getWidth())
    page_height = int(page.mediaBox.getHeight())

    # 将PDF页面转换为图像
    dpi = 300  # 设置图像的分辨率
    scale = dpi / 72.0  # 计算缩放比例
    img_width = int(page_width * scale)
    img_height = int(page_height * scale)
    img = np.zeros((img_height, img_width, 3), np.uint8)
    cv2.putText(img, "Page 1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # 示例，添加文本到图像上

    # 在图像上绘制坐标点
    cv2.circle(img, (int(x1 * scale), int(y1 * scale)), 5, (0, 0, 255), -1)  # 绘制圆形点（红色）
    cv2.circle(img, (int(x2 * scale), int(y2 * scale)), 5, (0, 0, 255), -1)  # 绘制圆形点（红色）

    # 将图像保存为PDF文件
    output_pdf = PdfFileWriter()
    output_pdf.addPage(page)

    # 创建临时图像文件
    temp_img_path = 'temp_image.png'
    cv2.imwrite(temp_img_path, img)

    # 将图像文件添加到PDF文件
    with open(temp_img_path, 'rb') as img_file:
        output_pdf.addPage(img_file.read())

    # 保存输出PDF文件
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)


def convert_pdf_to_image(input_path, output_path, dpi=300):
    # 将PDF页面转换为图像
    images = convert_from_path(input_path, dpi=dpi)

    # 保存图像
    for i, image in enumerate(images):
        image.save(f"{output_path}_{i + 1}.png", "PNG")


def get_table_pixel(input_path):
    # 使用PdfFileReader读取PDF文件
    pdf = PdfFileReader(open(input_path, 'rb'))

    page_width = float(pdf.getPage(0).mediaBox.getWidth())
    page_height = float(pdf.getPage(0).mediaBox.getHeight())
    print(page_height, page_width)


    # 使用camelot库进行表格识别
    tables = camelot.read_pdf(input_path, flavor='stream')

    # 获取第一个表格对象
    table = tables[0]

    print(type(table.cells))
    # idx = 0
    # for cells in table.cells:
    #
    #     for cell in cells:
    #         if idx == 0:
    #             print(type(cell), cell.x1, cell.y1, cell.x2, cell.y2)
    #             y1 = float(cell.y1)
    #             y2 = float(cell.y2)
    #             draw_point_on_pdf(input_path, "output.pdf", cell.x1, cell.y1, cell.x2, cell.y2)
    #         idx += 1
    #

if __name__ == "__main__":
    input_path = 'input.pdf'
    output_path = 'output'
    convert_pdf_to_image(input_path, output_path)
    get_table_pixel(input_path)