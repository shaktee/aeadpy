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
import struct
import string
import sys
class Testcase:
    __instance = 1
    def __init__(self, *args, **kwargs):
        self.attrs = []
        for k in kwargs:
            self.attrs.append(k)
            setattr(self, k, self.string_to_bytes(kwargs[k]))
            pass
        self.instance = Testcase.__instance
        Testcase.__instance += 1
        pass
    
    def string_to_bytes(self, x):
        x = ''.join(x.split())
        if not all(c in string.hexdigits for c in x):
            return x
        if sys.version_info.major < 3:
            out = ''
            for i in range(0, len(x), 2):
                z = struct.pack('B', int(x[i:i+2], 16))
                out += z
                pass
            #print len(out)
            return out
        else:
            out = b''
            for i in range(0, len(x), 2):
                out += int(x[i:i+2], 16).to_bytes(1,byteorder='big')
                pass
            return out
        
    def bytes_to_string(self, x):
        if sys.version_info.major < 3:
            return "".join(["%02x" %i for i in struct.unpack('B' * len(x), x)])
        else:
            return "".join(["%02x" % int.from_bytes(i, byteorder='big') for i in x])
    def __repr__(self):
        out = "Testcase %d\n" % self.instance
        for i in self.attrs:
            _bytes = getattr(self, i)
            if not all(c in string.hexdigits for c in _bytes):
                data = _bytes
            else:
                data = self.bytes_to_string(_bytes)
            out += "%10s: %s\n" % (i, data)
            pass
        return out
