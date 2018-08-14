#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Testbed class for AES-GCM testbench
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
import aesgcmpy
debug = False


def test(testcases):
    for i in testcases:
        print 'Encrypt Test %d' % i.instance,
        if debug:
            print ''

        rets = aesgcmpy.encrypt(i.key, i.plaintext, i.nonce, i.aad)
        ct = i.ctext_tag[:-16]
        tag = i.ctext_tag[-16:]

        # print rets

        if rets['status'] != 1:
            print 'FAILED - Bad status'
        elif rets['ciphertext'] != ct:
            print 'Ciphertext Mismatch'
            print 'Got', i.bytes_to_string(rets['ciphertext'])
            print 'Expected', i.bytes_to_string(ct)
        elif rets['tag'] != tag:
            print 'Tag Mismatch'
            print 'Got', i.bytes_to_string(rets['tag'])
            print 'Expected', i.bytes_to_string(tag)
        else:
            print 'PASS'
            pass

        print 'Decrypt Test %d' % i.instance,
        if debug:
            print ''
        rets = aesgcmpy.decrypt(i.key, ct, i.nonce, i.aad, tag)
        if rets['status'] != 1:
            print 'FAILED - Bad status'
        elif rets['plaintext'] != i.plaintext:
            print 'Mismatch'
            print 'Got', i.bytes_to_string(rets['plaintext'])
            print 'Expected', i.bytes_to_string(i.plaintext)
        else:
            print 'PASS'
            pass
        pass
    pass


if __name__ == '__main__':
    import getopt
    import sys
    import importlib
    testcases_file = 'ipsec_testcases'
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'dht:', [])
    except getopt.GetoptError, e:
        print e
        sys.exit(-1)
    for (k, v) in opts:
        if k == '-h':
            print '%s [-d|-h]' % sys.argv[0]
            sys.exit(0)
        elif k == '-d':
            aesgcmpy.debug()
            debug = True
        elif k == '-t':
            testcases_file = v
            pass
        pass
    i = importlib.import_module(testcases_file)
    test(testcases=i.testcases)
