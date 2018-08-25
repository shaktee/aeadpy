from testcase import Testcase

# Test cases for AES-GCM bench

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

# Test cases from
# https://tools.ietf.org/id/draft-mcgrew-gcm-test-01.html#aes-gcm

testcases = [
    # From https://tools.ietf.org/html/rfc7634#page-9
    Testcase(
        algorithm = 'CHACHA20_POLY1305',
        incremental = True,
        plaintext = """
        45 00 00 54 a6 f2 00 00 40 01 e7 78 c6 33 64 05
        c0 00 02 05 08 00 5b 7a 3a 08 00 00 55 3b ec 10
        00 07 36 27 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13
        14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23
        24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33
        34 35 36 37 01 02 02 04        """,
        key = """
        80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
        90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f
        a0 a1 a2 a3
        """,
        aad = """01 02 03 04 00 00 00 05
        """,
        nonce = """a0 a1 a2 a3 10 11 12 13 14 15 16 17
        """,
        ctext_tag = """
        24 03 94 28 b9 7f 41 7e 3c 13 75 3a 4f 05 08 7b
        67 c3 52 e6 a7 fa b1 b9 82 d4 66 ef 40 7a e5 c6
        14 ee 80 99 d5 28 44 eb 61 aa 95 df ab 4c 02 f7
        2a a7 1e 7c 4c 4f 64 c9 be fe 2f ac c6 38 e8 f3
        cb ec 16 3f ac 46 9b 50 27 73 f6 fb 94 e6 64 da
        91 65 b8 28 29 f6 41 e0
        76 aa a8 26 6b 7f b0 f7 b1 1b 36 99 07 e1 ad 43        
        """,
        ),
]
