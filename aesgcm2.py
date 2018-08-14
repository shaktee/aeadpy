#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Testbed for AES-GCM testbench
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
debug = 0


def test(testcases):
    (total, enc_success, dec_success) = (0, 0, 0)
    for i in testcases:
        total += 1
        if debug:
            print 'Encrypt Test %d' % i.instance,
        if debug:
            print ''
        if debug > 2:
            print dir(i)
        ct = i.ctext_tag[:-16]
        tag = i.ctext_tag[-16:]
        aesgcmpy.tc_encrypt(i)

        # print rets

        if i.enc_status != 1:
            print 'FAILED - Bad status %d' % i.enc_status
        elif i.enc_ciphertext != ct:
            if debug:
                print 'Ciphertext Mismatch'
            if debug > 1:
                print 'Got', i.bytes_to_string(i.enc_ciphertext)
                print 'Expected', i.bytes_to_string(ct)
        elif i.enc_tag != tag:
            if debug:
                print 'Tag Mismatch'
            if debug > 1:
                print 'Got', i.bytes_to_string(i.enc_tag)
                print 'Expected', i.bytes_to_string(tag)
        else:
            if debug:
                print 'PASS'
            enc_success += 1
            pass

        if debug > 2:
            print dir(i)
        if debug:
            print 'Decrypt Test %d' % i.instance,
        if debug:
            print ''
        rets = aesgcmpy.tc_decrypt(i)
        stat = ''
        if i.dec_status != 1:
            stat = 'FAIL - Bad status (continue to check plaintext)'
        else:
            stat = 'PASS - TAG verified'
        if i.dec_plaintext != i.plaintext:
            if debug:
                print 'Mismatch'
            if debug > 1:
                print 'Got     ', i.bytes_to_string(i.dec_plaintext)
                print 'Expected', i.bytes_to_string(i.plaintext)
            stat += ', FAIL - Data Mismatch'
        else:
            stat += ', PASS - Data match'
            if i.dec_status == 1:
                dec_success += 1
            pass
        if debug:
            print stat
        if debug > 2:
            print dir(i)
        pass
    print '%d/%d/%d - EPASS/DPASS/TOTAL' % (enc_success, dec_success,
            total)
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
            debug += 1
        elif k == '-t':
            testcases_file = v
            pass
        pass
    i = importlib.import_module(testcases_file)
    test(testcases=i.testcases)
