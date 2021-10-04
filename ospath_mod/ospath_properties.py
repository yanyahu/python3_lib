import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

"""
os.path.getatime()返回访问时间， 
os.path.getmtime()返回修改时间， 
os.path.getctime()返回创建时间。 
os.path.getsize()返回文件中的数据量，以字节表示。
"""