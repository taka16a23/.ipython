#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""type_magic -- DESCRIPTION

"""
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic import register_line_magic


@magics_class
class TypeCheckMagic(Magics):
    """TypeCheckMagic

    TypeCheckMagic is a Magics.
    Responsibility:
    """
    @line_magic
    def T(self, parameter_s=''):
        """SUMMARY

        T(parameter_s='')

        @Arguments:
        - `parameter_s`:

        @Return:

        @Error:
        """
        obj = self.shell.ev(parameter_s)
        print(type(obj))


def load_ipython_extension(ipython):
    global __loaded
    if not __loaded:
        ipython.register_magics(TypeCheckMagic)
        __loaded = True

__loaded = False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# type_magic.py ends here
