import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())

"""具体路径类包括一种resolve()通过查看文件系统中的目录和符号链接并生成由名称引用的绝对路径来规范化路径的方法。"""
