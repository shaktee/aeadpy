import struct
import string

# Testcase class for AES-GCM testbench
# Copyright (C) 2018 Rajesh Vaidheeswarrana

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class Testcase:
    __instance = 1
    def __init__(self, *args, **kwargs):
        for k in kwargs:
            setattr(self, k, self.string_to_bytes(kwargs[k]))
            pass
        self.instance = Testcase.__instance
        Testcase.__instance += 1
        pass
    
    def string_to_bytes(self, x):
        x = ''.join(x.split())
        if not all(c in string.hexdigits for c in x):
            return x
        out = ''
        for i in range(0, len(x), 2):
            out += struct.pack('B', int(x[i:i+2], 16))
            pass
        #print len(out)
        return out
    def bytes_to_string(self, x):
        return "".join(["%02x" %i for i in struct.unpack('B' * len(x), x)])
