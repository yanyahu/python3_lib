import glob

for name in sorted(glob.glob('glob_mod/dirs/*[0-9].*')):
    print(name)
