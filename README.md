# aesgcmpy
AES-GCM Testcases with a python wrapper

Description
===========
This is a simple python based validation bench of openssl's AES-GCM
implementation.

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

## Running the test

The default set of testcases is defined in testcases.py and passed to the script via the -t parameter, or via make, using the TEST variable (without the .py suffix)

To use a specific test case file, pass it in to make via `make run TEST=<x>`

## Debug and verbose output

To enable debug and more verbose output pass -d (up to three times to increase verbosity of debug output) to the script (or via ARGS="-d" to make).
