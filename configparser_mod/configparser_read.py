from configparser import ConfigParser

parser = ConfigParser()
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))

# TODO https://pymotw.com/3/configparser/index.html