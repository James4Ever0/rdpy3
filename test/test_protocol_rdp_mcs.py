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
unit test for rdpy3.protocol.rdp.mcs automata
"""

import os, sys
# Change path so we find rdpy
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest

class MCSTest(unittest.TestCase):
    """
    @summary: test case for per layer (RDP)
    """
    
    def test_per_readLength(self):
        pass