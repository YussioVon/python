# -*-coding:utf-8 -*
# @Time : 2021/7/6 15:29
# @Author :Yussio
# @FileName : test_orc
from PIL import Image
import  pytesseract
image = Image.open('C:\\Users\\Rain Sunny\\Desktop\\222.png')
#text = pytesseract.image_to_string(image)
text = pytesseract.image_to_string(image,lang="chi_sim")
text = text.replace("“","").replace("。","")
print(text)