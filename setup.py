from distutils.core import setup, Extension
import os
# Script to build python package
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

if os.environ.has_key('OPENSSL_INCLUDE'):
    openssl_include = [os.environ['OPENSSL_INCLUDE']]
    openssl_lib = ["%s/../lib" % os.environ['OPENSSL_INCLUDE']]
elif os.path.exists("/usr/local/opt/openssl"):
    openssl_lib  =['/usr/local/opt/openssl/lib']
    openssl_include = ["/usr/local/opt/openssl/include"]
else:
    openssl_include = openssl_lib = []


module1 = Extension('aesgcmpy',
                    include_dirs = openssl_include,
                    library_dirs = openssl_lib,
                    libraries = ['crypto'],
                    sources = ['aesgcm_python.c'])

setup (name = 'Aesgcmpy',
       version = '1.0',
       description = """This is a python-based AES-GCM test bench to test openssl's implementation of AES-GCM""",
       author='Rajesh Vaidheeswarran',
       author_email='rv@gnu.org',
       url='https://github.com/shaktee/aesgcmpy.git',
       ext_modules = [module1])

