import glob

for name in sorted(glob.glob('glob_mod/dirs/file?.txt')):
    print(name)

"""问号 ( ?) 是另一个通配符。它匹配名称中该位置的任何单个字符。"""
