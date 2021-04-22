


'''
def conn(self):
    serverIp = ['12.99.105.184','12.99.105.185']
    serverPwd = ['123456','nbcb2017']

    for i,p in serverIp,serverPwd:
        connect(serverIp[[i],serverPwd[p])
'''
serverIp = ['12.99.105.184','12.99.105.185']
serverPwd = ['123456','nbcb2017']
serverInfo = [('12.99.105.184','123456'),('12.99.105.185','nbcb2017')]
for  i,p in serverIp,serverPwd:
        print(i+"and"+ p+'\n')
for all in serverInfo:
    print(all[0]+all[1])