##############################################################################
#
# Copyright (c) 2001-2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Dummy Module

$Id: dummy.py 105433 2009-11-02 08:33:25Z ctheune $
"""
from zope.interface import moduleProvides
from zope.interface.tests.ifoo import IFoo
from zope.interface import moduleProvides

moduleProvides(IFoo)

def bar(baz):
    pass
