# aeadpy
AEAD (AES-GCM, Chacha20-Poly1305) Testcases with a python wrapper

Description
===========
This is a simple python based validation bench of openssl's AEAD
implementation.

## Prerequisites

You will need `make`, `python` and `openssl` (developer tools).

## Using make

Type `make help` in the shell to get help on make targets

The test script is aeadpy, and can be called with or without the
ARGS=-p, the latter being the default. The difference is in how the
parameters are passed to the C API (in the former, they are passed in
via explicit parameters to the function call, while in the latter, the
Testcase object is passed in directly).

There are two testcase files - one is a set of test cases from IPsec,
the second is the set of test cases in the McGrew paper. The sources
for the test cases are also available in the comments.

You can generate your own test cases file and pass it in to the test
bench by modeling the file similar to the ones provided.

## Building

Simply type `make ` and it will make and run the test (assuming that you have the prerequisites installed)

But, to just build, the target is `make bld`. by default, it will build the extension for whatever version of python is installed in the path as `python`

    rv@roke:~/aesgcmpy$ make bld
    python setup.py build
    running build
    running build_ext
    building 'aesgcmpy' extension
    creating build
    creating build/temp.linux-x86_64-2.7
    x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/usr/include/python2.7 -c aesgcm_python.c -o build/temp.linux-x86_64-2.7/aesgcm_python.o
    creating build/lib.linux-x86_64-2.7
    x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security -Wl,-Bsymbolic-functions -Wl,-z,relro -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security build/temp.linux-x86_64-2.7/aesgcm_python.o -lcrypto -o build/lib.linux-x86_64-2.7/aesgcmpy.so

To specifically build for a different python version, you must specify `PYTHON=<pythonX.x>

    rv@roke:~/aesgcmpy$ make PYTHON=python3 bld
    python3 setup.py build
    running build
    running build_ext
    building 'aesgcmpy' extension
    creating build/temp.linux-x86_64-3.6
    x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -g -fdebug-prefix-map=/build/python3.6-EKG1lX/python3.6-3.6.5=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DNDEBUG=1 -I/usr/include/python3.6m -c aesgcm_python.c -o build/temp.linux-x86_64-3.6/aesgcm_python.o
    creating build/lib.linux-x86_64-3.6
    x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -specs=/usr/share/dpkg/no-pie-link.specs -Wl,-z,relro -Wl,-Bsymbolic-functions -specs=/usr/share/dpkg/no-pie-link.specs -Wl,-z,relro -g -fdebug-prefix-map=/build/python3.6-EKG1lX/python3.6-3.6.5=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.6/aesgcm_python.o -lcrypto -o build/lib.linux-x86_64-3.6/aesgcmpy.cpython-36m-x86_64-linux-gnu.so

## Running the test

To run testcases with the default python, call `make`
    rv@roke:~/aesgcmpy$ make
    python setup.py build
    running build
    running build_ext
    python aesgcm.py  ipsec_testcases mcgrew_testcases
    Using testcases from ipsec_testcases
    14/14/14 - EPASS/DPASS/TOTAL
    Using testcases from mcgrew_testcases
    18/18/18 - EPASS/DPASS/TOTAL

To run testcases with a specific version, call `make PYTHON=<pythonX>`

    rv@roke:~/aesgcmpy$ make PYTHON=python3
    python3 setup.py build
    running build
    running build_ext
    python3 aesgcm.py  ipsec_testcases mcgrew_testcases
    Using testcases from ipsec_testcases
    14/14/14 - EPASS/DPASS/TOTAL
    Using testcases from mcgrew_testcases
    18/18/18 - EPASS/DPASS/TOTAL

The default set of testcases is defined in testcases.py and passed to the script via the -t parameter, or via make, using the TEST variable (without the .py suffix)

To use a specific test case file, pass it in to make via `make run TEST=<x>`

The output of the test is a tuple of EPASS/DPASS/TOTAL, indicating the number of tests that passed encryption testing, decryption testing and the total number of test cases run.

## Debug and verbose output

To enable debug and more verbose output pass -d (up to three times to increase verbosity of debug output) to the script (or via ARGS="-d" to make).

    rv@roke:~/aesgcmpy$ make ARGS=-d
    python setup.py build
    running build
    running build_ext
    python aesgcm.py -d ipsec_testcases mcgrew_testcases
    Using testcases from ipsec_testcases
    Encrypt Test 1 -  PASS
    Decrypt Test 1 PASS - TAG verified, PASS - Data match
    Encrypt Test 2 -  PASS
    Decrypt Test 2 PASS - TAG verified, PASS - Data match
    Encrypt Test 3 -  PASS
    Decrypt Test 3 PASS - TAG verified, PASS - Data match
    Encrypt Test 4 -  PASS
    Decrypt Test 4 PASS - TAG verified, PASS - Data match
    Encrypt Test 5 -  PASS
    Decrypt Test 5 PASS - TAG verified, PASS - Data match
    Encrypt Test 6 -  PASS
    Decrypt Test 6 PASS - TAG verified, PASS - Data match
    Encrypt Test 7 -  PASS
    Decrypt Test 7 PASS - TAG verified, PASS - Data match
    Encrypt Test 8 -  PASS
    Decrypt Test 8 PASS - TAG verified, PASS - Data match
    Encrypt Test 9 -  PASS
    Decrypt Test 9 PASS - TAG verified, PASS - Data match
    Encrypt Test 10 -  PASS
    Decrypt Test 10 PASS - TAG verified, PASS - Data match
    Encrypt Test 11 -  PASS
    Decrypt Test 11 PASS - TAG verified, PASS - Data match
    Encrypt Test 12 -  PASS
    Decrypt Test 12 PASS - TAG verified, PASS - Data match
    Encrypt Test 13 -  PASS
    Decrypt Test 13 PASS - TAG verified, PASS - Data match
    Encrypt Test 14 -  PASS
    Decrypt Test 14 PASS - TAG verified, PASS - Data match
    14/14/14 - EPASS/DPASS/TOTAL
    Using testcases from mcgrew_testcases
    Encrypt Test 15 -  PASS
    Decrypt Test 15 PASS - TAG verified, PASS - Data match
    Encrypt Test 16 -  PASS
    Decrypt Test 16 PASS - TAG verified, PASS - Data match
    Encrypt Test 17 -  PASS
    Decrypt Test 17 PASS - TAG verified, PASS - Data match
    Encrypt Test 18 -  PASS
    Decrypt Test 18 PASS - TAG verified, PASS - Data match
    Encrypt Test 19 -  PASS
    Decrypt Test 19 PASS - TAG verified, PASS - Data match
    Encrypt Test 20 -  PASS
    Decrypt Test 20 PASS - TAG verified, PASS - Data match
    Encrypt Test 21 -  PASS
    Decrypt Test 21 PASS - TAG verified, PASS - Data match
    Encrypt Test 22 -  PASS
    Decrypt Test 22 PASS - TAG verified, PASS - Data match
    Encrypt Test 23 -  PASS
    Decrypt Test 23 PASS - TAG verified, PASS - Data match
    Encrypt Test 24 -  PASS
    Decrypt Test 24 PASS - TAG verified, PASS - Data match
    Encrypt Test 25 -  PASS
    Decrypt Test 25 PASS - TAG verified, PASS - Data match
    Encrypt Test 26 -  PASS
    Decrypt Test 26 PASS - TAG verified, PASS - Data match
    Encrypt Test 27 -  PASS
    Decrypt Test 27 PASS - TAG verified, PASS - Data match
    Encrypt Test 28 -  PASS
    Decrypt Test 28 PASS - TAG verified, PASS - Data match
    Encrypt Test 29 -  PASS
    Decrypt Test 29 PASS - TAG verified, PASS - Data match
    Encrypt Test 30 -  PASS
    Decrypt Test 30 PASS - TAG verified, PASS - Data match
    Encrypt Test 31 -  PASS
    Decrypt Test 31 PASS - TAG verified, PASS - Data match
    Encrypt Test 32 -  PASS
    Decrypt Test 32 PASS - TAG verified, PASS - Data match
    18/18/18 - EPASS/DPASS/TOTAL

### More verbosity

For more verbosity, add -d to the ARGS

    rv@roke:~/aesgcmpy$ make ARGS="-d -d"
    PYTHONPATH=build/lib.linux-x86_64-2.7 python aesgcm.py -d -d ipsec_testcases
    Encrypt Test 1 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - 4c 80 cd ef bb 5d 10 da-90 6a c7 3c 36 13 a6 34   L....]...j.<6..4
    IV (12):
    0000 - 2e 44 3b 68 49 56 ed 7e-3b 24 4c fe               .D;hIV.~;$L.
    AAD (12):
    0000 - 00 00 43 21 87 65 43 21-                          ..C!.eC!
    000c - <SPACES/NULS>
    Plaintext (72):
    0000 - 45 00 00 48 69 9a 00 00-80 11 4d b7 c0 a8 01 02   E..Hi.....M.....
    0010 - c0 a8 01 01 0a 9b f1 56-38 d3 01 00 00 01 00 00   .......V8.......
    0020 - 00 00 00 00 04 5f 73 69-70 04 5f 75 64 70 03 73   ....._sip._udp.s
    0030 - 69 70 09 63 79 62 65 72-63 69 74 79 02 64 6b 00   ip.cybercity.dk.
    0040 - 00 21 00 01 01 02 02 01-                          .!......
    Ciphertext (72):
    0000 - fe cf 53 7e 72 9d 5b 07-dc 30 df 52 8d d2 2b 76   ..S~r.[..0.R..+v
    0010 - 8d 1b 98 73 66 96 a6 fd-34 85 09 fa 13 ce ac 34   ...sf...4......4
    0020 - cf a2 43 6f 14 a3 f3 cf-65 92 5b f1 f4 a1 3c 5d   ..Co....e.[...<]
    0030 - 15 b2 1e 18 84 f5 ff 62-47 ae ab b7 86 b9 3b ce   .......bG.....;.
    0040 - 61 bc 17 d7 68 fd 97 32-                          a...h..2
    Tag (16):
    0000 - 45 90 18 14 8f 6c be 72-2f d0 47 96 56 2d fd b4   E....l.r/.G.V-..
    PASS
    Decrypt Test 1 
    AES GCM Decrypt:
    Ciphertext (72):
    0000 - fe cf 53 7e 72 9d 5b 07-dc 30 df 52 8d d2 2b 76   ..S~r.[..0.R..+v
    0010 - 8d 1b 98 73 66 96 a6 fd-34 85 09 fa 13 ce ac 34   ...sf...4......4
    0020 - cf a2 43 6f 14 a3 f3 cf-65 92 5b f1 f4 a1 3c 5d   ..Co....e.[...<]
    0030 - 15 b2 1e 18 84 f5 ff 62-47 ae ab b7 86 b9 3b ce   .......bG.....;.
    0040 - 61 bc 17 d7 68 fd 97 32-                          a...h..2
    TAG (16):
    0000 - 45 90 18 14 8f 6c be 72-2f d0 47 96 56 2d fd b4   E....l.r/.G.V-..
    Plaintext (72):
    0000 - 45 00 00 48 69 9a 00 00-80 11 4d b7 c0 a8 01 02   E..Hi.....M.....
    0010 - c0 a8 01 01 0a 9b f1 56-38 d3 01 00 00 01 00 00   .......V8.......
    0020 - 00 00 00 00 04 5f 73 69-70 04 5f 75 64 70 03 73   ....._sip._udp.s
    0030 - 69 70 09 63 79 62 65 72-63 69 74 79 02 64 6b 00   ip.cybercity.dk.
    0040 - 00 21 00 01 01 02 02 01-                          .!......
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 2 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - fe ff e9 92 86 65 73 1c-6d 6a 8f 94 67 30 83 08   .....es.mj..g0..
    IV (12):
    0000 - ca fe ba be fa ce db ad-de ca f8 88               ............
    AAD (8):
    0000 - 00 00 a5 f8 00 00 00 0a-                          ........
    Plaintext (64):
    0000 - 45 00 00 3e 69 8f 00 00-80 11 4d cc c0 a8 01 02   E..>i.....M.....
    0010 - c0 a8 01 01 0a 98 00 35-00 2a 23 43 b2 d0 01 00   .......5.*#C....
    0020 - 00 01 00 00 00 00 00 00-03 73 69 70 09 63 79 62   .........sip.cyb
    0030 - 65 72 63 69 74 79 02 64-6b 00 00 01 00 01 00 01   ercity.dk.......
    Ciphertext (64):
    0000 - de b2 2c d9 b0 7c 72 c1-6e 3a 65 be eb 8d f3 04   ..,..|r.n:e.....
    0010 - a5 a5 89 7d 33 ae 53 0f-1b a7 6d 5d 11 4d 2a 5c   ...}3.S...m].M*\
    0020 - 3d e8 18 27 c1 0e 9a 4f-51 33 0d 0e ec 41 66 42   =..'...OQ3...AfB
    0030 - cf bb 85 a5 b4 7e 48 a4-ec 3b 9b a9 5d 91 8b d1   .....~H..;..]...
    Tag (16):
    0000 - 83 b7 0d 3a a8 bc 6e e4-c3 09 e9 d8 5a 41 ad 4a   ...:..n.....ZA.J
    PASS
    Decrypt Test 2 
    AES GCM Decrypt:
    Ciphertext (64):
    0000 - de b2 2c d9 b0 7c 72 c1-6e 3a 65 be eb 8d f3 04   ..,..|r.n:e.....
    0010 - a5 a5 89 7d 33 ae 53 0f-1b a7 6d 5d 11 4d 2a 5c   ...}3.S...m].M*\
    0020 - 3d e8 18 27 c1 0e 9a 4f-51 33 0d 0e ec 41 66 42   =..'...OQ3...AfB
    0030 - cf bb 85 a5 b4 7e 48 a4-ec 3b 9b a9 5d 91 8b d1   .....~H..;..]...
    TAG (16):
    0000 - 83 b7 0d 3a a8 bc 6e e4-c3 09 e9 d8 5a 41 ad 4a   ...:..n.....ZA.J
    Plaintext (64):
    0000 - 45 00 00 3e 69 8f 00 00-80 11 4d cc c0 a8 01 02   E..>i.....M.....
    0010 - c0 a8 01 01 0a 98 00 35-00 2a 23 43 b2 d0 01 00   .......5.*#C....
    0020 - 00 01 00 00 00 00 00 00-03 73 69 70 09 63 79 62   .........sip.cyb
    0030 - 65 72 63 69 74 79 02 64-6b 00 00 01 00 01 00 01   ercity.dk.......
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 3 
    AES GCM Testcase Encrypt:
    KEY (32):
    0000 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    0010 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    IV (12):
    0000 - 11 22 33 44 01 02 03 04-05 06 07 08               ."3D........
    AAD (8):
    0000 - 4a 2c bf e3 00 00 00 02-                          J,......
    Plaintext (52):
    0000 - 45 00 00 30 69 a6 40 00-80 06 26 90 c0 a8 01 02   E..0i.@...&.....
    0010 - 93 89 15 5e 0a 9e 00 8b-2d c5 7e e0 00 00 00 00   ...^....-.~.....
    0020 - 70 02 40 00 20 bf 00 00-02 04 05 b4 01 01 04 02   p.@. ...........
    0030 - 01 02 02 01                                       ....
    Ciphertext (52):
    0000 - ff 42 5c 9b 72 45 99 df-7a 3b cd 51 01 94 e0 0d   .B\.rE..z;.Q....
    0010 - 6a 78 10 7f 1b 0b 1c bf-06 ef ae 9d 65 a5 d7 63   jx..........e..c
    0020 - 74 8a 63 79 85 77 1d 34-7f 05 45 65 9f 14 e9 9d   t.cy.w.4..Ee....
    0030 - ef 84 2d 8e                                       ..-.
    Tag (16):
    0000 - b3 35 f4 ee cf db f8 31-82 4b 4c 49 15 95 6c 96   .5.....1.KLI..l.
    PASS
    Decrypt Test 3 
    AES GCM Decrypt:
    Ciphertext (52):
    0000 - ff 42 5c 9b 72 45 99 df-7a 3b cd 51 01 94 e0 0d   .B\.rE..z;.Q....
    0010 - 6a 78 10 7f 1b 0b 1c bf-06 ef ae 9d 65 a5 d7 63   jx..........e..c
    0020 - 74 8a 63 79 85 77 1d 34-7f 05 45 65 9f 14 e9 9d   t.cy.w.4..Ee....
    0030 - ef 84 2d 8e                                       ..-.
    TAG (16):
    0000 - b3 35 f4 ee cf db f8 31-82 4b 4c 49 15 95 6c 96   .5.....1.KLI..l.
    Plaintext (52):
    0000 - 45 00 00 30 69 a6 40 00-80 06 26 90 c0 a8 01 02   E..0i.@...&.....
    0010 - 93 89 15 5e 0a 9e 00 8b-2d c5 7e e0 00 00 00 00   ...^....-.~.....
    0020 - 70 02 40 00 20 bf 00 00-02 04 05 b4 01 01 04 02   p.@. ...........
    0030 - 01 02 02 01                                       ....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 4 
    AES GCM Testcase Encrypt:
    KEY (16):
    0010 - <SPACES/NULS>
    IV (12):
    000c - <SPACES/NULS>
    AAD (8):
    0000 - 00 00 00 00 00 00 00 01-                          ........
    Plaintext (64):
    0000 - 45 00 00 3c 99 c5 00 00-80 01 cb 7a 40 67 93 18   E..<.......z@g..
    0010 - 01 01 01 01 08 00 07 5c-02 00 44 00 61 62 63 64   .......\..D.abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 75 76 77 61 62 63 64 65-66 67 68 69 01 02 02 01   uvwabcdefghi....
    Ciphertext (64):
    0000 - 46 88 da f2 f9 73 a3 92-73 29 09 c3 31 d5 6d 60   F....s..s)..1.m`
    0010 - f6 94 ab aa 41 4b 5e 7f-f5 fd cd ff f5 e9 a2 84   ....AK^.........
    0020 - 45 64 76 49 27 19 ff b6-4d e7 d9 dc a1 e1 d8 94   EdvI'...M.......
    0030 - bc 3b d5 78 73 ed 4d 18-1d 19 d4 d5 c8 c1 8a f3   .;.xs.M.........
    Tag (16):
    0000 - f8 21 d4 96 ee b0 96 e9-8a d2 b6 9e 47 99 c7 1d   .!..........G...
    PASS
    Decrypt Test 4 
    AES GCM Decrypt:
    Ciphertext (64):
    0000 - 46 88 da f2 f9 73 a3 92-73 29 09 c3 31 d5 6d 60   F....s..s)..1.m`
    0010 - f6 94 ab aa 41 4b 5e 7f-f5 fd cd ff f5 e9 a2 84   ....AK^.........
    0020 - 45 64 76 49 27 19 ff b6-4d e7 d9 dc a1 e1 d8 94   EdvI'...M.......
    0030 - bc 3b d5 78 73 ed 4d 18-1d 19 d4 d5 c8 c1 8a f3   .;.xs.M.........
    TAG (16):
    0000 - f8 21 d4 96 ee b0 96 e9-8a d2 b6 9e 47 99 c7 1d   .!..........G...
    Plaintext (64):
    0000 - 45 00 00 3c 99 c5 00 00-80 01 cb 7a 40 67 93 18   E..<.......z@g..
    0010 - 01 01 01 01 08 00 07 5c-02 00 44 00 61 62 63 64   .......\..D.abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 75 76 77 61 62 63 64 65-66 67 68 69 01 02 02 01   uvwabcdefghi....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 5 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - 3d e0 98 74 b3 88 e6 49-19 88 d0 c3 60 7e ae 1f   =..t...I....`~..
    IV (12):
    0000 - 57 69 0e 43 4e 28 00 00-a2 fc a1 a3               Wi.CN(......
    AAD (12):
    0000 - 42 f6 7e 3f 10 10 10 10-10 10 10 10               B.~?........
    Plaintext (64):
    0000 - 45 00 00 3c 99 c3 00 00-80 01 cb 7c 40 67 93 18   E..<.......|@g..
    0010 - 01 01 01 01 08 00 08 5c-02 00 43 00 61 62 63 64   .......\..C.abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 75 76 77 61 62 63 64 65-66 67 68 69 01 02 02 01   uvwabcdefghi....
    Ciphertext (64):
    0000 - fb a2 ca a4 85 3c f9 f0-f2 2c b1 0d 86 dd 83 b0   .....<...,......
    0010 - fe c7 56 91 cf 1a 04 b0-0d 11 38 ec 9c 35 79 17   ..V.......8..5y.
    0020 - 65 ac bd 87 01 ad 79 84-5b f9 fe 3f ba 48 7b c9   e.....y.[..?.H{.
    0030 - 17 55 e6 66 2b 4c 8d 0d-1f 5e 22 73 95 30 32 0a   .U.f+L...^"s.02.
    Tag (16):
    0000 - e0 d7 31 cc 97 8e ca fa-ea e8 8f 00 e8 0d 6e 48   ..1...........nH
    PASS
    Decrypt Test 5 
    AES GCM Decrypt:
    Ciphertext (64):
    0000 - fb a2 ca a4 85 3c f9 f0-f2 2c b1 0d 86 dd 83 b0   .....<...,......
    0010 - fe c7 56 91 cf 1a 04 b0-0d 11 38 ec 9c 35 79 17   ..V.......8..5y.
    0020 - 65 ac bd 87 01 ad 79 84-5b f9 fe 3f ba 48 7b c9   e.....y.[..?.H{.
    0030 - 17 55 e6 66 2b 4c 8d 0d-1f 5e 22 73 95 30 32 0a   .U.f+L...^"s.02.
    TAG (16):
    0000 - e0 d7 31 cc 97 8e ca fa-ea e8 8f 00 e8 0d 6e 48   ..1...........nH
    Plaintext (64):
    0000 - 45 00 00 3c 99 c3 00 00-80 01 cb 7c 40 67 93 18   E..<.......|@g..
    0010 - 01 01 01 01 08 00 08 5c-02 00 43 00 61 62 63 64   .......\..C.abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 75 76 77 61 62 63 64 65-66 67 68 69 01 02 02 01   uvwabcdefghi....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 6 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - 3d e0 98 74 b3 88 e6 49-19 88 d0 c3 60 7e ae 1f   =..t...I....`~..
    IV (12):
    0000 - 57 69 0e 43 4e 28 00 00-a2 fc a1 a3               Wi.CN(......
    AAD (12):
    0000 - 42 f6 7e 3f 10 10 10 10-10 10 10 10               B.~?........
    Plaintext (28):
    0000 - 45 00 00 1c 42 a2 00 00-80 01 44 1f 40 67 93 b6   E...B.....D.@g..
    0010 - e0 00 00 02 0a 00 f5 ff-01 02 02 01               ............
    Ciphertext (28):
    0000 - fb a2 ca 84 5e 5d f9 f0-f2 2c 3e 6e 86 dd 83 1e   ....^]...,>n....
    0010 - 1f c6 57 92 cd 1a f9 13-0e 13 79 ed               ..W.......y.
    Tag (16):
    0000 - 36 9f 07 1f 35 e0 34 be-95 f1 12 e4 e7 d0 5d 35   6...5.4.......]5
    PASS
    Decrypt Test 6 
    AES GCM Decrypt:
    Ciphertext (28):
    0000 - fb a2 ca 84 5e 5d f9 f0-f2 2c 3e 6e 86 dd 83 1e   ....^]...,>n....
    0010 - 1f c6 57 92 cd 1a f9 13-0e 13 79 ed               ..W.......y.
    TAG (16):
    0000 - 36 9f 07 1f 35 e0 34 be-95 f1 12 e4 e7 d0 5d 35   6...5.4.......]5
    Plaintext (28):
    0000 - 45 00 00 1c 42 a2 00 00-80 01 44 1f 40 67 93 b6   E...B.....D.@g..
    0010 - e0 00 00 02 0a 00 f5 ff-01 02 02 01               ............
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 7 
    AES GCM Testcase Encrypt:
    KEY (24):
    0000 - fe ff e9 92 86 65 73 1c-6d 6a 8f 94 67 30 83 08   .....es.mj..g0..
    0010 - fe ff e9 92 86 65 73 1c-                          .....es.
    IV (12):
    0000 - ca fe ba be fa ce db ad-de ca f8 88               ............
    AAD (8):
    0000 - 00 00 a5 f8 00 00 00 0a-                          ........
    Plaintext (40):
    0000 - 45 00 00 28 a4 ad 40 00-40 06 78 80 0a 01 03 8f   E..(..@.@.x.....
    0010 - 0a 01 06 12 80 23 06 b8-cb 71 26 02 dd 6b b0 3e   .....#...q&..k.>
    0020 - 50 10 16 d0 75 68 00 01-                          P...uh..
    Ciphertext (40):
    0000 - a5 b1 f8 06 60 29 ae a4-0e 59 8b 81 22 de 02 42   ....`)...Y.."..B
    0010 - 09 38 b3 ab 33 f8 28 e6-87 b8 85 8b 5b fb db d0   .8..3.(.....[...
    0020 - 31 5b 27 45 21 44 cc 77-                          1['E!D.w
    Tag (16):
    0000 - 95 45 7b 96 52 03 7f 53-18 02 7b 5b 4c d7 a6 36   .E{.R..S..{[L..6
    PASS
    Decrypt Test 7 
    AES GCM Decrypt:
    Ciphertext (40):
    0000 - a5 b1 f8 06 60 29 ae a4-0e 59 8b 81 22 de 02 42   ....`)...Y.."..B
    0010 - 09 38 b3 ab 33 f8 28 e6-87 b8 85 8b 5b fb db d0   .8..3.(.....[...
    0020 - 31 5b 27 45 21 44 cc 77-                          1['E!D.w
    TAG (16):
    0000 - 95 45 7b 96 52 03 7f 53-18 02 7b 5b 4c d7 a6 36   .E{.R..S..{[L..6
    Plaintext (40):
    0000 - 45 00 00 28 a4 ad 40 00-40 06 78 80 0a 01 03 8f   E..(..@.@.x.....
    0010 - 0a 01 06 12 80 23 06 b8-cb 71 26 02 dd 6b b0 3e   .....#...q&..k.>
    0020 - 50 10 16 d0 75 68 00 01-                          P...uh..
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 8 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    IV (12):
    0000 - de ca f8 88 ca fe de ba-ce fa ce 74               ...........t
    AAD (12):
    0000 - 00 00 01 00 00 00 00 00-00 00 00 01               ............
    Plaintext (76):
    0000 - 45 00 00 49 33 ba 00 00-7f 11 91 06 c3 fb 1d 10   E..I3...........
    0010 - c2 b1 d3 26 c0 28 31 ce-00 35 dd 7b 80 03 02 d5   ...&.(1..5.{....
    0020 - 00 00 4e 20 00 1e 8c 18-d7 5b 81 dc 91 ba a0 47   ..N .....[.....G
    0030 - 6b 91 b9 24 b2 80 38 9d-92 c9 63 ba c0 46 ec 95   k..$..8...c..F..
    0040 - 9b 62 66 c0 47 22 b1 49-23 01 01 01               .bf.G".I#...
    Ciphertext (76):
    0000 - 18 a6 fd 42 f7 2c bf 4a-b2 a2 ea 90 1f 73 d8 14   ...B.,.J.....s..
    0010 - e3 e7 f2 43 d9 54 12 e1-c3 49 c1 d2 fb ec 16 8f   ...C.T...I......
    0020 - 91 90 fe eb af 2c b0 19-84 e6 58 63 96 5d 74 72   .....,....Xc.]tr
    0030 - b7 9d a3 45 e0 e7 80 19-1f 0d 2f 0e 0f 49 6c 22   ...E....../..Il"
    0040 - 6f 21 27 b2 7d b3 57 24-e7 84 5d 68               o!'.}.W$..]h
    Tag (16):
    0000 - 65 1f 57 e6 5f 35 4f 75-ff 17 01 57 69 62 34 36   e.W._5Ou...Wib46
    PASS
    Decrypt Test 8 
    AES GCM Decrypt:
    Ciphertext (76):
    0000 - 18 a6 fd 42 f7 2c bf 4a-b2 a2 ea 90 1f 73 d8 14   ...B.,.J.....s..
    0010 - e3 e7 f2 43 d9 54 12 e1-c3 49 c1 d2 fb ec 16 8f   ...C.T...I......
    0020 - 91 90 fe eb af 2c b0 19-84 e6 58 63 96 5d 74 72   .....,....Xc.]tr
    0030 - b7 9d a3 45 e0 e7 80 19-1f 0d 2f 0e 0f 49 6c 22   ...E....../..Il"
    0040 - 6f 21 27 b2 7d b3 57 24-e7 84 5d 68               o!'.}.W$..]h
    TAG (16):
    0000 - 65 1f 57 e6 5f 35 4f 75-ff 17 01 57 69 62 34 36   e.W._5Ou...Wib46
    Plaintext (76):
    0000 - 45 00 00 49 33 ba 00 00-7f 11 91 06 c3 fb 1d 10   E..I3...........
    0010 - c2 b1 d3 26 c0 28 31 ce-00 35 dd 7b 80 03 02 d5   ...&.(1..5.{....
    0020 - 00 00 4e 20 00 1e 8c 18-d7 5b 81 dc 91 ba a0 47   ..N .....[.....G
    0030 - 6b 91 b9 24 b2 80 38 9d-92 c9 63 ba c0 46 ec 95   k..$..8...c..F..
    0040 - 9b 62 66 c0 47 22 b1 49-23 01 01 01               .bf.G".I#...
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 9 
    AES GCM Testcase Encrypt:
    KEY (32):
    0000 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    0010 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    IV (12):
    0000 - 73 61 6c 74 61 6e 64 01-69 76 65 63               saltand.ivec
    AAD (12):
    0000 - 17 40 5e 67 15 6f 31 26-dd 0d b9 9b               .@^g.o1&....
    Plaintext (40):
    0000 - 45 08 00 28 73 2c 00 00-40 06 e9 f9 0a 01 06 12   E..(s,..@.......
    0010 - 0a 01 03 8f 06 b8 80 23-dd 6b af be cb 71 26 02   .......#.k...q&.
    0020 - 50 10 1f 64 6d 54 00 01-                          P..dmT..
    Ciphertext (40):
    0000 - f2 d6 9e cd bd 5a 0d 5b-8d 5e f3 8b ad 4d a5 8d   .....Z.[.^...M..
    0010 - 1f 27 8f de 98 ef 67 54-9d 52 4a 30 18 d9 a5 7f   .'....gT.RJ0....
    0020 - f4 d3 a3 1c e6 73 11 9e-                          .....s..
    Tag (16):
    0000 - 45 16 26 c2 41 57 71 e3-b7 ee bc a6 14 c8 9b 35   E.&.AWq........5
    PASS
    Decrypt Test 9 
    AES GCM Decrypt:
    Ciphertext (40):
    0000 - f2 d6 9e cd bd 5a 0d 5b-8d 5e f3 8b ad 4d a5 8d   .....Z.[.^...M..
    0010 - 1f 27 8f de 98 ef 67 54-9d 52 4a 30 18 d9 a5 7f   .'....gT.RJ0....
    0020 - f4 d3 a3 1c e6 73 11 9e-                          .....s..
    TAG (16):
    0000 - 45 16 26 c2 41 57 71 e3-b7 ee bc a6 14 c8 9b 35   E.&.AWq........5
    Plaintext (40):
    0000 - 45 08 00 28 73 2c 00 00-40 06 e9 f9 0a 01 06 12   E..(s,..@.......
    0010 - 0a 01 03 8f 06 b8 80 23-dd 6b af be cb 71 26 02   .......#.k...q&.
    0020 - 50 10 1f 64 6d 54 00 01-                          P..dmT..
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 10 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - 3d e0 98 74 b3 88 e6 49-19 88 d0 c3 60 7e ae 1f   =..t...I....`~..
    IV (12):
    0000 - 57 69 0e 43 4e 28 00 00-a2 fc a1 a3               Wi.CN(......
    AAD (12):
    0000 - 42 f6 7e 3f 10 10 10 10-10 10 10 10               B.~?........
    Plaintext (76):
    0000 - 45 00 00 49 33 3e 00 00-7f 11 91 82 c3 fb 1d 10   E..I3>..........
    0010 - c2 b1 d3 26 c0 28 31 ce-00 35 cb 45 80 03 02 5b   ...&.(1..5.E...[
    0020 - 00 00 01 e0 00 1e 8c 18-d6 57 59 d5 22 84 a0 35   .........WY."..5
    0030 - 2c 71 47 5c 88 80 39 1c-76 4d 6e 5e e0 49 6b 32   ,qG\..9.vMn^.Ik2
    0040 - 5a e2 70 c0 38 99 49 39-15 01 01 01               Z.p.8.I9....
    Ciphertext (76):
    0000 - fb a2 ca d1 2f c1 f9 f0-0d 3c eb f3 05 41 0d b8   ..../....<...A..
    0010 - 3d 77 84 b6 07 32 3d 22-0f 24 b0 a9 7d 54 18 28   =w...2=".$..}T.(
    0020 - 00 ca db 0f 68 d9 9e f0-e0 c0 c8 9a e9 be a8 88   ....h...........
    0030 - 4e 52 d6 5b c1 af d0 74-0f 74 24 44 74 7b 5b 39   NR.[...t.t$Dt{[9
    0040 - ab 53 31 63 aa d4 55 0e-e5 16 09 75               .S1c..U....u
    Tag (16):
    0000 - cd b6 08 c5 76 91 89 60-97 63 b8 e1 8c aa 81 e2   ....v..`.c......
    PASS
    Decrypt Test 10 
    AES GCM Decrypt:
    Ciphertext (76):
    0000 - fb a2 ca d1 2f c1 f9 f0-0d 3c eb f3 05 41 0d b8   ..../....<...A..
    0010 - 3d 77 84 b6 07 32 3d 22-0f 24 b0 a9 7d 54 18 28   =w...2=".$..}T.(
    0020 - 00 ca db 0f 68 d9 9e f0-e0 c0 c8 9a e9 be a8 88   ....h...........
    0030 - 4e 52 d6 5b c1 af d0 74-0f 74 24 44 74 7b 5b 39   NR.[...t.t$Dt{[9
    0040 - ab 53 31 63 aa d4 55 0e-e5 16 09 75               .S1c..U....u
    TAG (16):
    0000 - cd b6 08 c5 76 91 89 60-97 63 b8 e1 8c aa 81 e2   ....v..`.c......
    Plaintext (76):
    0000 - 45 00 00 49 33 3e 00 00-7f 11 91 82 c3 fb 1d 10   E..I3>..........
    0010 - c2 b1 d3 26 c0 28 31 ce-00 35 cb 45 80 03 02 5b   ...&.(1..5.E...[
    0020 - 00 00 01 e0 00 1e 8c 18-d6 57 59 d5 22 84 a0 35   .........WY."..5
    0030 - 2c 71 47 5c 88 80 39 1c-76 4d 6e 5e e0 49 6b 32   ,qG\..9.vMn^.Ik2
    0040 - 5a e2 70 c0 38 99 49 39-15 01 01 01               Z.p.8.I9....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 11 
    AES GCM Testcase Encrypt:
    KEY (32):
    0000 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    0010 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    IV (12):
    0000 - 73 61 6c 74 61 6e 64 01-69 76 65 63               saltand.ivec
    AAD (12):
    0000 - 17 40 5e 67 15 6f 31 26-dd 0d b9 9b               .@^g.o1&....
    Plaintext (72):
    0000 - 63 69 73 63 6f 01 72 75-6c 65 73 01 74 68 65 01   cisco.rules.the.
    0010 - 6e 65 74 77 65 01 64 65-66 69 6e 65 01 74 68 65   netwe.define.the
    0020 - 74 65 63 68 6e 6f 6c 6f-67 69 65 73 01 74 68 61   technologies.tha
    0030 - 74 77 69 6c 6c 01 64 65-66 69 6e 65 74 6f 6d 6f   twill.definetomo
    0040 - 72 72 6f 77 01 02 02 01-                          rrow....
    Ciphertext (72):
    0000 - d4 b7 ed 86 a1 77 7f 2e-a1 3d 69 73 d3 24 c6 9e   .....w...=is.$..
    0010 - 7b 43 f8 26 fb 56 83 12-26 50 8b eb d2 dc eb 18   {C.&.V..&P......
    0020 - d0 a6 df 10 e5 48 7d f0-74 11 3e 14 c6 41 02 4e   .....H}.t.>..A.N
    0030 - 3e 67 73 d9 1a 62 ee 42-9b 04 3a 10 e3 ef e6 b0   >gs..b.B..:.....
    0040 - 12 a4 93 63 41 23 64 f8-                          ...cA#d.
    Tag (16):
    0000 - c0 ca c5 87 f2 49 e5 6b-11 e2 4f 30 e4 4c cc 76   .....I.k..O0.L.v
    PASS
    Decrypt Test 11 
    AES GCM Decrypt:
    Ciphertext (72):
    0000 - d4 b7 ed 86 a1 77 7f 2e-a1 3d 69 73 d3 24 c6 9e   .....w...=is.$..
    0010 - 7b 43 f8 26 fb 56 83 12-26 50 8b eb d2 dc eb 18   {C.&.V..&P......
    0020 - d0 a6 df 10 e5 48 7d f0-74 11 3e 14 c6 41 02 4e   .....H}.t.>..A.N
    0030 - 3e 67 73 d9 1a 62 ee 42-9b 04 3a 10 e3 ef e6 b0   >gs..b.B..:.....
    0040 - 12 a4 93 63 41 23 64 f8-                          ...cA#d.
    TAG (16):
    0000 - c0 ca c5 87 f2 49 e5 6b-11 e2 4f 30 e4 4c cc 76   .....I.k..O0.L.v
    Plaintext (72):
    0000 - 63 69 73 63 6f 01 72 75-6c 65 73 01 74 68 65 01   cisco.rules.the.
    0010 - 6e 65 74 77 65 01 64 65-66 69 6e 65 01 74 68 65   netwe.define.the
    0020 - 74 65 63 68 6e 6f 6c 6f-67 69 65 73 01 74 68 61   technologies.tha
    0030 - 74 77 69 6c 6c 01 64 65-66 69 6e 65 74 6f 6d 6f   twill.definetomo
    0040 - 72 72 6f 77 01 02 02 01-                          rrow....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 12 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - 7d 77 3d 00 c1 44 c5 25-ac 61 9d 18 c8 4a 3f 47   }w=..D.%.a...J?G
    IV (12):
    0000 - d9 66 42 67 43 45 7e 91-82 44 3b c6               .fBgCE~..D;.
    AAD (8):
    0000 - 33 54 67 ae ff ff ff ff-                          3Tg.....
    Plaintext (4):
    0000 - 01 02 02 01                                       ....
    Ciphertext (4):
    0000 - 43 7f 86 6b                                       C..k
    Tag (16):
    0000 - cb 3f 69 9f e9 b0 82 2b-ac 96 1c 45 04 be f2 70   .?i....+...E...p
    PASS
    Decrypt Test 12 
    AES GCM Decrypt:
    Ciphertext (4):
    0000 - 43 7f 86 6b                                       C..k
    TAG (16):
    0000 - cb 3f 69 9f e9 b0 82 2b-ac 96 1c 45 04 be f2 70   .?i....+...E...p
    Plaintext (4):
    0000 - 01 02 02 01                                       ....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 13 
    AES GCM Testcase Encrypt:
    KEY (16):
    0000 - ab bc cd de f0 01 12 23-34 45 56 67 78 89 9a ab   .......#4EVgx...
    IV (12):
    0000 - de ca f8 88 ca fe de ba-ce fa ce 74               ...........t
    AAD (12):
    0000 - 00 00 01 00 00 00 00 00-00 00 00 01               ............
    Plaintext (20):
    0000 - 74 6f 01 62 65 01 6f 72-01 6e 6f 74 01 74 6f 01   to.be.or.not.to.
    0010 - 62 65 00 01                                       be..
    Ciphertext (20):
    0000 - 29 c9 fc 69 a1 97 d0 38-cc dd 14 e2 dd fc aa 05   )..i...8........
    0010 - 43 33 21 64                                       C3!d
    Tag (16):
    0000 - 41 25 03 52 43 03 ed 3c-6c 5f 28 38 43 af 8c 3e   A%.RC..<l_(8C..>
    PASS
    Decrypt Test 13 
    AES GCM Decrypt:
    Ciphertext (20):
    0000 - 29 c9 fc 69 a1 97 d0 38-cc dd 14 e2 dd fc aa 05   )..i...8........
    0010 - 43 33 21 64                                       C3!d
    TAG (16):
    0000 - 41 25 03 52 43 03 ed 3c-6c 5f 28 38 43 af 8c 3e   A%.RC..<l_(8C..>
    Plaintext (20):
    0000 - 74 6f 01 62 65 01 6f 72-01 6e 6f 74 01 74 6f 01   to.be.or.not.to.
    0010 - 62 65 00 01                                       be..
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    Encrypt Test 14 
    AES GCM Testcase Encrypt:
    KEY (32):
    0000 - 6c 65 67 61 6c 69 7a 65-6d 61 72 69 6a 75 61 6e   legalizemarijuan
    0010 - 61 61 6e 64 64 6f 69 74-62 65 66 6f 72 65 69 61   aanddoitbeforeia
    IV (12):
    0000 - 74 75 72 6e 33 30 21 69-67 65 74 6d               turn30!igetm
    AAD (12):
    0000 - 79 6b 69 63 ff ff ff ff-ff ff ff ff               ykic........
    Plaintext (52):
    0000 - 45 00 00 30 da 3a 00 00-80 01 df 3b c0 a8 00 05   E..0.:.....;....
    0010 - c0 a8 00 01 08 00 c6 cd-02 00 07 00 61 62 63 64   ............abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 01 02 02 01                                       ....
    Ciphertext (52):
    0000 - f9 7a b2 aa 35 6d 8e dc-e1 76 44 ac 8c 78 e2 5d   .z..5m...vD..x.]
    0010 - d2 4d ed bb 29 eb f1 b6-4a 27 4b 39 b4 9c 3a 86   .M..)...J'K9..:.
    0020 - 4c d3 d7 8c a4 ae 68 a3-2b 42 45 8f b5 7d be 82   L.....h.+BE..}..
    0030 - 1d cc 63 b9                                       ..c.
    Tag (16):
    0000 - d0 93 7b a2 94 5f 66 93-68 66 1a 32 9f b4 c0 53   ..{.._f.hf.2...S
    PASS
    Decrypt Test 14 
    AES GCM Decrypt:
    Ciphertext (52):
    0000 - f9 7a b2 aa 35 6d 8e dc-e1 76 44 ac 8c 78 e2 5d   .z..5m...vD..x.]
    0010 - d2 4d ed bb 29 eb f1 b6-4a 27 4b 39 b4 9c 3a 86   .M..)...J'K9..:.
    0020 - 4c d3 d7 8c a4 ae 68 a3-2b 42 45 8f b5 7d be 82   L.....h.+BE..}..
    0030 - 1d cc 63 b9                                       ..c.
    TAG (16):
    0000 - d0 93 7b a2 94 5f 66 93-68 66 1a 32 9f b4 c0 53   ..{.._f.hf.2...S
    Plaintext (52):
    0000 - 45 00 00 30 da 3a 00 00-80 01 df 3b c0 a8 00 05   E..0.:.....;....
    0010 - c0 a8 00 01 08 00 c6 cd-02 00 07 00 61 62 63 64   ............abcd
    0020 - 65 66 67 68 69 6a 6b 6c-6d 6e 6f 70 71 72 73 74   efghijklmnopqrst
    0030 - 01 02 02 01                                       ....
    Tag Verify Successful!
    PASS - TAG verified, PASS - Data match
    14/14/14 - EPASS/DPASS/TOTAL
