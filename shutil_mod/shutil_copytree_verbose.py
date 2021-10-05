import glob
import pprint
import shutil


def verbose_copy(src, dst):
    print('copying\n {!r}\n to {!r}'.format(src, dst))
    return shutil.copy2(src, dst)


print('BEFORE:')
pprint.pprint(glob.glob('/tmp/example/*'))
print()

shutil.copytree(
    '../shutil', '/tmp/example',
    copy_function=verbose_copy,
    ignore=shutil.ignore_patterns('*.py'),
)

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))

"""ignore_patterns()用于创建忽略函数以跳过复制 Python 源文件。verbose_copy() 在复制文件时打印文件的名称，然后使用copy2()默认的复制功能进行复制。"""
