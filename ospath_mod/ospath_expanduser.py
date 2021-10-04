import os.path

for user in ['', 'dhellmann', 'nosuchuser']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.format(lookup, os.path.expanduser(lookup)))

"""如果找不到用户的主目录，则字符串将原样返回，如~nosuchuser本例所示。"""
