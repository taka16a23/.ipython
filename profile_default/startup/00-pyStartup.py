#!/usr/bin/env python
#
"""\
Name: pyStartup.py
$Revision$


"""
import os
import readline
import rlcompleter
import atexit

try:
    from pathhandler import PathHandler
    PH = PathHandler
except ImportError as imperr:
    print(imperr)


__all__ = []

_all = __all__

# tab completion
readline.parse_and_bind('tab: complete')


#history file
if 'nt' == os.name:
    histfile = ''
    # histfile = os.path.join(P_OFFICE,
    #                          'emacs/.emacs.d/data_e/code/python/interpreter/'
    #                          '.pythistory')
elif 'posix' == os.name:
    histfile = os.path.join(os.environ['HOME'],
                            '.emacs.d/data_e/code/python/interpreter/'
                            '.pythistory')

try:
    readline.read_history_file(histfile)
except IOError:
    pass

atexit.register(readline.write_history_file, histfile)


del histfile, readline, rlcompleter, #P_OFFICE



print __all__



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pyStartup.py ends here
