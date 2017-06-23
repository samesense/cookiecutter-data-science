import os, sys

SECRETS = '/home/evansj/me/.secrets/'
sys.path.append(SECRETS)
from pass_wd import *

if 'code' in p:
    PWD = os.getcwd().split('src/')[0]
else:
    PWD = p + '/'

WORK = PWD + 'work/'
FILES = PWD + 'docs/'
SCRIPTS = PWD + 'src/scripts/'
DATA = PWD + 'data/'
LOG = PWD + 'log/'
CONFIG = PWD + 'configs/'
