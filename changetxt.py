# -*-coding:utf-8 -*
# @Time : 2021/6/11 14:30
# @Author :Yussio
# @FileName : changetxt.py

import os,re,mmap
def writefilename():
    filepath = os.getcwd() + '\\'
    filelist = os.listdir(filepath)
    with open('file.txt','w+') as filetxt:
        for data in filelist:
            filetxt.writelines(data + '\n')

def changelines(filepath,linecount,linecontent):
    with open(filepath,'r',encoding='UTF-8',errors='ignore') as f:
        res = f.readlines()
        res[linecontent-1] = linecount + '\n'
        with open(filepath,'w',encoding='UTF-8',errors='ignore') as f:
            f.write("".join(res))

def changelastline():
    with open('file.txt','r') as readfile:
        files = readfile.readlines()
        for filename in files:
            filename = filename.split('\n')[0]
            if re.search('PCKG',filename) is not None:
                size = os.path.getsize(filename)
                if size != 0:
                    with open(filename,'r',encoding='UTF-8',errors='ignore') as filecontent:
                        map = mmap.mmap(filecontent.fileno(),length=0,access=mmap.ACCESS_READ)
                        count = 0
                        while map.readline():
                            count += 1
                        map.close()
                        lastlinetxt = filecontent.readlines()
                        lastline = lastlinetxt[count-1]
                        if lastline == '/':
                            with open(filename,'a',encoding='UTF-8',errors='ignore') as f:
                                f.write('\n'+'SHOW ERRORS;'+'\n')
                        else:
                            print('格式正确')


