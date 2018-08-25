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
from __future__ import print_function
import sys

def set_libdir():
    import os
    vers = "%d.%d" % (sys.version_info.major, sys.version_info.minor)
    for d, dd, f in os.walk('build'):
        if 'lib' in d and vers in d: sys.path.insert(0, d)
        pass
    pass

debug = 0

def test_with_params(testcase):
    enc_success, dec_success = 0, 0
    if debug: print('Encrypt Test %d' % testcase.instance, end=' ')
    rets = aeadpy.encrypt(testcase.algorithm, testcase.key, testcase.plaintext, testcase.nonce, testcase.aad)
    ct = testcase.ctext_tag[:-16]
    tag = testcase.ctext_tag[-16:]

    # print(rets)

    if rets['status'] != 1:
        print('FAILED - Bad status')
    elif rets['ciphertext'] != ct:
        print('Ciphertext Mismatch')
        print('Got     : %s' % testcase.bytes_to_string(rets['ciphertext']))
        print('Expected: %s' % testcase.bytes_to_string(ct))
    elif rets['tag'] != tag:
        print('Tag Mismatch')
        print('Got     : %s' % testcase.bytes_to_string(rets['tag']))
        print('Expected: %s' % testcase.bytes_to_string(tag))
    else:
        if debug: print('PASS')
        enc_success += 1
        pass

    if debug: print('Decrypt Test %d' % testcase.instance, end=' ')
    rets = aeadpy.decrypt(testcase.algorithm, testcase.key, ct, testcase.nonce, testcase.aad, tag)
    if rets['status'] != 1:
        print('FAILED - Bad status')
    elif rets['plaintext'] != testcase.plaintext:
        print('Mismatch')
        print('Got     : %s' % testcase.bytes_to_string(rets['plaintext']))
        print('Expected: %s' % testcase.bytes_to_string(testcase.plaintext))
    else:
        if debug: print('PASS')
        dec_success += 1
        pass
    return enc_success, dec_success


def test(testcases, objmode=True):
    (total, enc_success, dec_success) = (0, 0, 0)
    for testcase in testcases:
        if not hasattr(testcase, 'algorithm'):
            setattr(testcase, 'algorithm', "AES-GCM")
            pass
        
        total += 1
        if debug > 2:
            print(testcase)
        if objmode:
            es, ds = test_with_testcase(testcase)
        else:
            es, ds = test_with_params(testcase)
            pass
        enc_success, dec_success = (enc_success + es), (dec_success + ds)
        pass
    print('%d/%d/%d - EPASS/DPASS/TOTAL' % (enc_success, dec_success, total))

def test_with_testcase(testcase):
    enc_success, dec_success = 0, 0
    if debug: print('Encrypt Test %d - ' % testcase.instance, end=' ')
    ct = testcase.ctext_tag[:-16]
    tag = testcase.ctext_tag[-16:]
    if hasattr(testcase,"incremental") and testcase.incremental:
        if debug: print('Incremental - ', end=' ')
        enc = aeadpy.tc_encrypt_incremental
        dec = aeadpy.tc_decrypt_incremental
    else:
        enc = aeadpy.tc_encrypt
        dec = aeadpy.tc_decrypt

    try:
        enc(testcase)
    
        if testcase.enc_status != 1:
            print('FAILED - Bad status %d' % testcase.enc_status)
        
        elif testcase.enc_ciphertext != ct:
            if debug: print('Ciphertext Mismatch')
            if debug > 1:
                print('Got     : %s' % testcase.bytes_to_string(testcase.enc_ciphertext))
                print('Expected: %s' % testcase.bytes_to_string(ct))
                pass
        elif testcase.enc_tag != tag:
            if debug: print('Tag Mismatch')
            if debug > 1:
                print('Got     : %s' % testcase.bytes_to_string(testcase.enc_tag))
                print('Expected: %s' % testcase.bytes_to_string(tag))
                pass
        else:
            if debug: print('PASS')
            enc_success += 1
            pass
    except Exception as e:
        print("Error - %s" % e)
        pass

    
    if debug: print('Decrypt Test %d' % testcase.instance, end=' ')
    try:
        dec(testcase)
        stat = ''
        if testcase.dec_status != 1:
            stat = 'FAIL - Bad status (continue to check plaintext)'
            pass
        else:
            stat = 'PASS - TAG verified'
            pass
        if testcase.dec_plaintext != testcase.plaintext:
            if debug: print('Mismatch')
            if debug > 1:
                print('Got     : %s' % testcase.bytes_to_string(testcase.dec_plaintext))
                print('Expected: %s' % testcase.bytes_to_string(testcase.plaintext))
                pass
            stat += ', FAIL - Data Mismatch'
            pass
        else:
            stat += ', PASS - Data match'
            if testcase.dec_status == 1:
                dec_success += 1
                pass
            pass
        if debug: print(stat)
        if debug > 2: print(dir(testcase))
    except Exception as e:
        print("Error - %s" % e)
        
    return enc_success, dec_success

def usage(err=False):
    if err: print(err)
    ustr = """Usage: %s -h
      %s [-d ...] [-p] <testcase_file> [<testcase_file> ...]
    Where
    -h    - This help
    -d    - Enable Debug output. Can be called multiple times to increase verbosity
    -p    - Parameter mode (instead of the default object mode) to pass args to the C API
    """ % (sys.argv[0], sys.argv[0])
    print(ustr)
    sys.exit(-1 if err else 0)
    pass

if __name__ == '__main__':
    import getopt
    import importlib
    import re

    set_libdir() # need to set appropriate lib directory for use with
                 # python 2 or 3 before importing aeadpy
    import aeadpy

    default_testcases_file = ['ipsec_testcases']
    objmode = True
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'dhp', [])
    except getopt.GetoptError as e:
        usage(e)

    for (k, v) in opts:
        if k == '-h':
            usage()
        elif k == '-d':
            aeadpy.debug()
            debug += 1
        elif k == '-p':
            objmode = False
        pass

    if  args == []:
        args = default_testcases_file
        pass
    for testcases_file in args:
        print("Using testcases from %s" % testcases_file) 
        i = importlib.import_module(re.sub('.py', '', testcases_file))
        test(testcases=i.testcases, objmode=objmode)
