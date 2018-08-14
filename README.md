# aesgcmpy
AES-GCM Testcases with a python wrapper

Description
===========
This is a simple python based validation bench of openssl's AES-GCM
implementation.

## Prerequisites

You will need `make`, `python` and `openssl` (developer tools).

## Using make

Type `make help` in the shell to get help on make targets

There are two scripts aesgcm.py and aesgcm2.py, the latter being the
default. The difference is in how the parameters are passed to the C
API (in the former, they are passed in via explicit parameters to the
function call, while in the latter, the Testcase object is passed in
directly).

There are two testcase files - one is a set of test cases from IPsec,
the second is the set of test cases in the McGrew paper. The sources
for the test cases are also available in the comments.

You can generate your own test cases file and pass it in to the test
bench by modeling the file similar to the ones provided.

## Building

Simply type `make ` and it will make and run the test (assuming that you have the prerequisites installed)
`
rv@roke:~/aesgcmpy$ make
python setup.py build
running build
running build_ext
building 'aesgcmpy' extension
creating build
creating build/temp.linux-x86_64-2.7
x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/usr/include/python2.7 -c aesgcm_python.c -o build/temp.linux-x86_64-2.7/aesgcm_python.o
creating build/lib.linux-x86_64-2.7
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security -Wl,-Bsymbolic-functions -Wl,-z,relro -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-nbjU53/python2.7-2.7.15~rc1=. -fstack-protector-strong -Wformat -Werror=format-security build/temp.linux-x86_64-2.7/aesgcm_python.o -lcrypto -o build/lib.linux-x86_64-2.7/aesgcmpy.so
PYTHONPATH=build/lib.linux-x86_64-2.7 python aesgcm2.py -t ipsec_testcases 
14/14/14 - EPASS/DPASS/TOTAL
`

To run mcgrew_testcases, do the following

`
rv@roke:~/aesgcmpy$ make TEST=mcgrew_testcases
PYTHONPATH=build/lib.linux-x86_64-2.7 python aesgcm2.py -t mcgrew_testcases 
18/18/18 - EPASS/DPASS/TOTAL
`

## Running the test

The default set of testcases is defined in testcases.py and passed to the script via the -t parameter, or via make, using the TEST variable (without the .py suffix)

To use a specific test case file, pass it in to make via `make run TEST=<x>`

## Debug and verbose output

To enable debug and more verbose output pass -d (up to three times to increase verbosity of debug output) to the script (or via ARGS="-d" to make).
