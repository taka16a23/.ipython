#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""pprint_dir_magic -- DESCRIPTION

"""
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic import register_line_magic
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)


## for implements
#
import re
from inspect import getmembers, isclass, ismodule
from pprint import pprint

try:
    from columnize import columnize
except ImportError as _err:
    print(err)
    print('try: pip install columnize')

try:
    from colorama import Fore, Style, Back, init, deinit, reinit
except ImportError as _err:
    print(err)
    print('try: pip install colorama')
##


@magics_class
class ColumnizeDirMagic(Magics):
    """ColumnizeDirMagic

    ColumnizeDirMagic is a Magics.
    Responsibility:
    """
    @magic_arguments()
    @argument(
        '-g',  '--grep', dest='pattern', default=None, type=str,
        help='grep method')
    @argument('evaluation', help='string of evaluation')
    @line_magic
    def D(self, parameter_s=''):
        """SUMMARY

        D(parameter_s='')

        @Arguments:
        - `parameter_s`:

        @Return:

        @Error:
        """
        init() # for colorama
        args = parse_argstring(self.D, parameter_s)
        obj = self.shell.ev(args.evaluation)
        if args.pattern: # "-g" grep option
            regex = re.compile(args.pattern)
            members = [(name, elem) for name, elem in getmembers(obj)
            if regex.search(name) is not None]
        else:
            members = getmembers(obj)
        results = []
        for name, elem in members:
            if isclass(elem):
                member = ColumnizeDirMagic._fore_green_reset(name)
            elif self._iscallable(elem):
                member = ColumnizeDirMagic._fore_red_reset(name)
            elif ismodule(elem):
                member = ColumnizeDirMagic._fore_cyan_reset(name)
            elif not name.startswith('_', ):
                member = ColumnizeDirMagic._fore_yellow_reset(name)
            else:
                member = ColumnizeDirMagic._fore_white_reset(name)
            results.append(member)
        print(columnize(results, displaywidth=110))[:-2] # trim '\\n'

    # fore
    @classmethod
    def _bright(cls, string):
        return Style.BRIGHT + '{}'.format(string)

    @classmethod
    def _fore_white(cls, string):
        return Fore.WHITE + '{}'.format(string)

    @classmethod
    def _fore_black(cls, string):
        return Fore.BLACK + '{}'.format(string)

    @classmethod
    def _fore_blue(cls, string):
        return Fore.BLUE + '{}'.format(string)

    @classmethod
    def _fore_cyan(cls, string):
        return Fore.CYAN + '{}'.format(string)

    @classmethod
    def _fore_red(cls, string):
        return Fore.RED + '{}'.format(string)

    @classmethod
    def _fore_magenta(cls, string):
        return Fore.MAGENTA + '{}'.format(string)

    @classmethod
    def _fore_green(cls, string):
        return Fore.GREEN + '{}'.format(string)

    @classmethod
    def _fore_yellow(cls, string):
        return Fore.YELLOW + '{}'.format(string)

    # back
    @classmethod
    def _back_white(cls, string):
        return Back.WHITE + '{}'.format(string)

    @classmethod
    def _back_black(cls, string):
        return Back.BLACK + '{}'.format(string)

    @classmethod
    def _back_blue(cls, string):
        return Back.BLUE + '{}'.format(string)

    @classmethod
    def _back_cyan(cls, string):
        return Back.CYAN + '{}'.format(string)

    @classmethod
    def _back_red(cls, string):
        return Back.RED + '{}'.format(string)

    @classmethod
    def _back_magenta(cls, string):
        return Back.MAGENTA + '{}'.format(string)

    @classmethod
    def _back_green(cls, string):
        return Back.GREEN + '{}'.format(string)

    @classmethod
    def _back_yellow(cls, string):
        return Back.YELLOW + '{}'.format(string)

    # reset
    @classmethod
    def _reset_all(cls, string):
        return '{}'.format(string) + Style.RESET_ALL

    # fore reset
    @classmethod
    def _fore_white_reset(cls, string):
        return cls._reset_all(cls._fore_white('{}'.format(string)))

    @classmethod
    def _fore_black_reset(cls, string):
        return cls._reset_all(cls._fore_black('{}'.format(string)))

    @classmethod
    def _fore_blue_reset(cls, string):
        return cls._reset_all(cls._fore_blue('{}'.format(string)))

    @classmethod
    def _fore_cyan_reset(cls, string):
        return cls._reset_all(cls._fore_cyan('{}'.format(string)))

    @classmethod
    def _fore_red_reset(cls, string):
        return cls._reset_all(cls._fore_red('{}'.format(string)))

    @classmethod
    def _fore_magenta_reset(cls, string):
        return cls._reset_all(cls._fore_magenta('{}'.format(string)))

    @classmethod
    def _fore_green_reset(cls, string):
        return cls._reset_all(cls._fore_green('{}'.format(string)))

    @classmethod
    def _fore_yellow_reset(cls, string):
        return cls._reset_all(cls._fore_yellow('{}'.format(string)))

    # back reset
    @classmethod
    def _back_white_reset(cls, string):
        return cls._reset_all(cls._back_white('{}'.format(string)))

    @classmethod
    def _back_black_reset(cls, string):
        return cls._reset_all(cls._back_black('{}'.format(string)))

    @classmethod
    def _back_blue_reset(cls, string):
        return cls._reset_all(cls._back_blue('{}'.format(string)))

    @classmethod
    def _back_cyan_reset(cls, string):
        return cls._reset_all(cls._back_cyan('{}'.format(string)))

    @classmethod
    def _back_red_reset(cls, string):
        return cls._reset_all(cls._back_red('{}'.format(string)))

    @classmethod
    def _back_magenta_reset(cls, string):
        return cls._reset_all(cls._back_magenta('{}'.format(string)))

    @classmethod
    def _back_green_reset(cls, string):
        return cls._reset_all(cls._back_green('{}'.format(string)))

    @classmethod
    def _back_yellow_reset(cls, string):
        return cls._reset_all(cls._back_yellow('{}'.format(string)))

    @classmethod
    def _iscallable(cls, obj):
        """SUMMARY

        _iscallable(obj)

        @Arguments:
        - `obj`:

        @Return:

        @Error:
        """
        return hasattr(obj, '__call__')



def load_ipython_extension(ipython):
    global __loaded
    if not __loaded:
        ipython.register_magics(ColumnizeDirMagic)
        __loaded = True

__loaded = False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pprint_dir_magic.py ends here
