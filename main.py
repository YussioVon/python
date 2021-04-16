''''
import paramiko
import socket

class Operate_Server():
    def __init__(self, hostname, port, username):
        self.hostname = hostname  # 服务器IP地址
        self.port = port  # 服务器登录端口号
        self.username = username  # 登录账号

    def run(self, command, **kwargs):
        """
        :command: sh命令
        :param kwargs:  传参(private_key: 私钥路径) (password: 密码)
        :return:
        """
        try:
            # 创建SSHClient对象，ssh
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # 通过密钥调用connect函数建立Linux连接
            if "private_key" in kwargs.keys():
                private_key = paramiko.RSAKey.from_private_key_file(kwargs["private_key"])
                ssh.connect(
                    hostname=self.hostname, port=self.port, username=self.username, pkey=private_key)
            # 通过密码调用connect函数建立Linux连接
            if "password" in kwargs.keys():
                ssh.connect(
                    hostname=self.hostname, port=self.port, username=self.username, password=kwargs["password"])
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))

            # 执行sh命令并返回执行结果
            result = ssh.exec_command(command)[1].read()
            print(" shell命令[%s]执行结果：%s" % (command, result))

            # 登出服务器
            ssh.close()
            print(" 登出服务器[%s]" % self.hostname)
        except Exception as e:
            print("发生未知错误：%s" % e)
            raise


if __name__ == "__main__":
    # 通过密码登录
    Operate_Server(hostname="IP", port=22, username="用户").run(command="pwd", password="密码")

    # 通过密钥认证登录
    Operate_Server(hostname="IP", port=22, username="用户").run(command="pwd", private_key="私钥路径")
'''
import paramiko, getpass  # getpass是隐藏密码


def ssh_connect(host_ip,password):
    user_name = 'root'
    host_port = '22'

    # 待执行的命令
    #sed_command = "ls"
    #ls_command = "rm -rf test"

    # 注意：依次执行多条命令时，命令之间用分号隔开
    #command = sed_command + ";" + ls_command



    # SSH远程连接
    ssh = paramiko.SSHClient()  # 创建sshclient
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
    ssh.connect(host_ip, host_port, user_name, password)

    # 执行命令并获取执行结果
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.readlines()
    err = stderr.readlines()

    ssh.close()

    return out, err


if __name__ == '__main__':
    host_ip = input("请输入ip:\n")
    pwd = getpass.getpass("请输入密码:\n")
    command = input("请输入命令:\n")
    result = ssh_connect(host_ip,pwd)
    print(result)
