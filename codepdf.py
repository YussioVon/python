# -*-coding:utf-8 -*
# @Time : 2021/6/16 14:02
# @Author :Yussio
# @FileName : codepdf
import PyPDF2


def encrypt(oldpath, newpath):
    with open(oldpath, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt('0011')
        with open(newpath, 'wb') as resultPDF:
            pdfWriter.write(resultPDF)
            print('加密成功')


def disencrypt(newpath):
    with open(newpath, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        # 判断文件是否加密
        if pdfReader.isEncrypted:
            # 判断密码是否正确
            for i in range(10000):
                #生成四位数密码
                pwd=str(i).zfill(4)
                if pdfReader.decrypt(pwd):
                    print('成功了！密码是：'+pwd)
                    break
                else:
                    print('密码错误！')
        else:
            print('没有加密')

if __name__ == '__main__':
    # encrypt(r'C:\Users\Rain Sunny\Desktop\jiaoben-python-265247.pdf',r'G:\1.pdf')
    disencrypt(r'G:\1.pdf')
    # for i in range(10000):
    #     pwd = str(i).zfill(4)
    #     print(pwd)
