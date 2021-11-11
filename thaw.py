#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/10/27 10:20
# @Author   :Yussio
# @File     :thaw.py
import web
import io
from subprocess import PIPE,Popen
urls = (
    '/index','index' ,
    '/thaw' ,'thaw' ,
)
admin = web.template.render('static/')

class index :
    def GET(self):
        try:
            return admin.index()
        finally:
            with open('error.txt','a+') as f:
                f.write('error')
class thaw:
    def POST(self):
        data = web.input(innerIP=None,in_account=None)
        innerIP = data.innerIP
        in_account = data.in_account
        sql  = "update ebank.im_usr a set a.user_pwd=a.user_authpwd,a_usr_stt='0',a.usr_lastchangepwd=to_char(sysdata,'yyyyMMddhhhmmss') where a.usr_id='{in_account}'"
        sql = sql.format(in_account=in_account.zfill(8))
        with open('update.sql','w') as f:
            f.write(sql)
        # sqlcmd = '@./update.sql'
        connectStr='admin/admin@{innerIP}/orcl'
        connectStr = connectStr.format(innerIP=innerIP)
        with open('ip.txt','w') as f:
            f.write(connectStr)
        '''
        ret = runSql(sqlcmd,connectStr)
        if ret[0] != '' or ret[1] != '':
            print(sqlcmd)
            if ret[0]:
                print('[Result]:\t%s' % ret[0])
            if ret[1]:
                print('[ErrMsg]:\t%s' % ret[1])
        '''


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()