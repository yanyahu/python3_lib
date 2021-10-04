import glob

specials = '?*['

for char in specials:
    pattern = 'glob_mod/dirs/*' + glob.escape(char) + '.txt'
    print('Searching for: {!r}'.format(pattern))
    for name in sorted(glob.glob(pattern)):
        print(name)
    print()

"""有时需要搜索名称中包含glob用于其模式的特殊元字符的文件。该 escape()函数使用“转义”特殊字符构建合适的模式，因此它们不会被glob."""
