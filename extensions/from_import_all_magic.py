#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""from_import_all_magic -- DESCRIPTION

"""
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic import register_line_magic

from inspect import getmembers


@magics_class
class FromImportAllMagic(Magics):
    """FromImportAllMagic

    FromImportAllMagic is a Magics.
    Responsibility:
    """
    @line_magic
    def F(self, parameter_s=''):
        """SUMMARY

        F(parameter_s='')

        @Arguments:
        - `parameter_s`:

        @Return:

        @Error:
        """
        mod = __import__(parameter_s)
        if hasattr(mod, '__all__'):
            for key, value in getmembers(mod):
                if not key.startswith('_'):
                    cmdline = 'from {} import {}'.format(parameter_s, key)
                    print(cmdline)
                    self.shell.ex(cmdline)


def load_ipython_extension(ipython):
    global __loaded
    if not __loaded:
        ipython.register_magics(FromImportAllMagic)
        __loaded = True

__loaded = False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# from_import_all_magic.py ends here
