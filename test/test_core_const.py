#
# Copyright (c) 2014 Sylvain Peyrefitte
#
# This file is part of rdpy3.
#
# rdpy3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
unit test for rdpy3.core.const module
"""

from builtins import object
import os, sys
# Change path so we find rdpy
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
import rdpy3.core.const
import rdpy3.core.type

class ConstTest(unittest.TestCase):
    '''
    represent test case for all classes and function
    present in rdpy3.base.const
    '''
    def test_type_attributes(self):
        '''
        test if type attributes decorator works
        '''
        @rdpy3.core.const.TypeAttributes(rdpy3.core.type.UInt16Le)
        class Test(object):
            MEMBER_1 = 1
            MEMBER_2 = 2
        
        self.assertIsInstance(Test.MEMBER_1, rdpy3.core.type.UInt16Le, "MEMBER_1 is not in correct type")
        self.assertIsInstance(Test.MEMBER_2, rdpy3.core.type.UInt16Le, "MEMBER_2 is not in correct type")
        
    def test_const(self):
        '''
        test if get on const class member generate new object each
        '''
        @rdpy3.core.const.ConstAttributes
        class Test(object):
            MEMBER_1 = 1
            MEMBER_2 = 2
            
        self.assertEquals(Test.MEMBER_1, Test.MEMBER_1, "handle same type of object")