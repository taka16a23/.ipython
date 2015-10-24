#!/usr/bin/env python
#
"""\
Name: pyStartup.py
$Revision$


"""
import os as _os
import os
import sys
import re
import dis
import readline
import rlcompleter
import atexit
import types
import time
import exceptions
from time import sleep
import subprocess as sbp
from inspect import *
from pympler.asizeof import asizeof as asize

try:
    from pathhandler import PathHandler
    PH = PathHandler
except ImportError as imperr:
    print(imperr)

# try:
#     from portable import P_OFFICE
# except ImportError:
#     print('Failed import portable')

# try:
#     from MySampleData import MySampleData
#     S = MySampleData()
# except ImportError:
#     print('Failed import MySampleData')

__all__ = []

_all = __all__

# tab completion
readline.parse_and_bind('tab: complete')

#history file


if 'nt' == _os.name:
    histfile = ''
    # histfile = os.path.join(P_OFFICE,
    #                          'emacs/.emacs.d/data_e/code/python/interpreter/'
    #                          '.pythistory')
elif 'posix' == _os.name:
    histfile = os.path.join(os.environ['HOME'],
                            '.emacs.d/data_e/code/python/interpreter/'
                            '.pythistory')

try:
    readline.read_history_file(histfile)
except IOError:
    pass

atexit.register(readline.write_history_file, histfile)


del histfile, readline, rlcompleter, #P_OFFICE


print('imported: ' ' '.join(['os', 'sys', 're', 'pprint', 'dis',
                            'types', 'time', 'subprocess as sbp', 'inspect']))

print __all__


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pyStartup.py ends here
