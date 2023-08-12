#!/usr/bin/python
#
# Copyright (c) 2014-2015 Sylvain Peyrefitte
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
example of use rdpy3 as rdp client
"""

import sys
import asyncio

import rdpy3.core.tpkt as tpkt
import rdpy3.core.x224 as x224
from rdpy3.core.nla import ntlm
from rdpy3.core.t125 import mcs
from rdpy3.model.message import UInt8

if __name__ == '__main__':

    #sys.exit(app.exec_())

    async def tcp_echo_client(message):
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 33389)

        x224_layer = await x224.connect(tpkt.Tpkt(reader, writer), ntlm.NTLMv2("", "sylvain", "sylvain"))
        mcs_layer = mcs.Client(x224_layer)
        await mcs_layer.connect()

        await asyncio.sleep(10)
        print("foooooooooooooooooooo")

    asyncio.run(tcp_echo_client('Hello World!'))