import glob
for name in sorted(glob.glob('glob_mod/dirs/*')):
    print(name)
