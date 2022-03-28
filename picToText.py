# -*- coding: utf-8 -*-
# @Time     :2022/1/18 15:56
# @Author   :Yussio
# @File     :picToText.py
import pytesseract
from PIL import Image
import datetime

pytesseract.pytesseract.tesseract_cmd = r'G:\Application\Tesseract-OCR\tesseract.exe'
def main():
    for i in range(1, 2):
        starttime = datetime.datetime.now()
        image = Image.open(r"C:\Users\Rain Sunny\Desktop\\" + str(i) + ".png")
        text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
        endtime = datetime.datetime.now()

        print(r"计算机网络_" + str(i) + r"转换完成，耗时：" + str((endtime - starttime).seconds))

        text = text.replace(" ", "")
        with open(r"C:\Users\Rain Sunny\Desktop\\" + str(i) + ".txt", "w") as f:  # 将识别出来的文字存到本地
            # print(text)
            f.write(str(text))
main()