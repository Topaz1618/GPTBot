"""
Author: Hang Yan
Date created: 2023/8/14
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""
import os
import pytesseract

import PyPDF2
from PIL import Image
from docx import Document
from pdf2image import convert_from_path

directory = '440113104003JC04336F00010001'


for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    # 检查文件类型
    if filename.endswith('.docx'):
        # 处理Word文档
        doc = Document(filepath)
        text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        # 打印识别结果
        print(text)

    elif filename.endswith('.png'):
        # 处理PNG图像文件
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)
        # 打印识别结果
        print(text)

    elif filename.endswith('.pdf'):
        # 处理PDF文件
        images = convert_from_path(filepath)
        for image in images:
            image_text = pytesseract.image_to_string(image)
            # 打印识别结果
            print(image_text)


# with open('宗地图.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     for page_number in range(len(pdf_reader.pages)):
#         # Extract the page text
#         page = pdf_reader.pages[page_number]
#         text = page.extract_text()
#
#         # Print the extracted text
#         print(text)
#         if "宗地图" in text:
#             print("检测结果为宗地图")


# # 打开图像文件
# image = Image.open('demo.png')
#
# # 使用Tesseract进行OCR识别
# text = pytesseract.image_to_string(image, lang='chi_sim')
#
# # 打印提取到的文字
# print(text)


