import fnmatch

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
print('Regex   :', fnmatch.translate(pattern))


"""在内部，fnmatch将 glob 模式转换为正则表达式并使用re模块来比较名称和模式。该translate()函数是用于将 glob 模式转换为正则表达式的公共 API。
"""
