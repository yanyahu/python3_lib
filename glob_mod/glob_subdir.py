import glob

print('Named explicitly:')
for name in sorted(glob.glob('glob_mod/dirs/subdir/*')):
    print('  {}'.format(name))

print('Named with wildcard:')
for name in sorted(glob.glob('glob_mod/dirs/*/*')):
    print('  {}'.format(name))
