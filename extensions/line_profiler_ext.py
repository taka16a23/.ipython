#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$

import line_profiler

def load_ipython_extension(ip):
    r"""SUMMARY

    load_ipython_extension_()

    @Return:
    """
    ip.define_magic('lprun', line_profiler.magic_lprun)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# line_profiler_ext.py ends here
