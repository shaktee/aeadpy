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
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '4c80cdefbb5d10da906ac73c3613a634',
        spi = '00004321',
        seq = '8765432100000000',
        nonce = '2e443b684956ed7e3b244cfe',
        plaintext = """45000048699a000080114db7c0a80102
        c0a801010a9bf15638d3010000010000
        00000000045f736970045f7564700373
        69700963796265726369747902646b00
        0021000101020201""",
        aad = '000043218765432100000000',
        ctext_tag = """fecf537e729d5b07dc30df528dd22b76
        8d1b98736696a6fd348509fa13ceac34
        cfa2436f14a3f3cf65925bf1f4a13c5d
        15b21e1884f5ff6247aeabb786b93bce
        61bc17d768fd9732459018148f6cbe72
        2fd04796562dfdb4""",
        packet = """00004321000000004956ed7e3b244cfe
                 fecf537e729d5b07dc30df528dd22b76
                 8d1b98736696a6fd348509fa13ceac34
                 cfa2436f14a3f3cf65925bf1f4a13c5d
                 15b21e1884f5ff6247aeabb786b93bce
                 61bc17d768fd9732459018148f6cbe72
                 2fd04796562dfdb4""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = 'feffe9928665731c6d6a8f9467308308',
        spi = '0000a5f8',
        seq = '0000000a',
        nonce = 'cafebabefacedbaddecaf888',
        plaintext = """4500003e698f000080114dccc0a80102
                 c0a801010a980035002a2343b2d00100
                 00010000000000000373697009637962
                 65726369747902646b00000100010001""",
        aad = '0000a5f80000000a',
        ctext_tag = """deb22cd9b07c72c16e3a65beeb8df304
                 a5a5897d33ae530f1ba76d5d114d2a5c
                 3de81827c10e9a4f51330d0eec416642
                 cfbb85a5b47e48a4ec3b9ba95d918bd1
                 83b70d3aa8bc6ee4c309e9d85a41ad4a""",
        packet = """0000a5f80000000afacedbaddecaf888
                 deb22cd9b07c72c16e3a65beeb8df304
                 a5a5897d33ae530f1ba76d5d114d2a5c
                 3de81827c10e9a4f51330d0eec416642
                 cfbb85a5b47e48a4ec3b9ba95d918bd1
                 83b70d3aa8bc6ee4c309e9d85a41ad4a""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = """abbccddef00112233445566778899aab
                 abbccddef00112233445566778899aab""",
        spi = '4a2cbfe3',
        seq = '00000002',
        nonce = '112233440102030405060708',
        plaintext = """4500003069a6400080062690c0a80102
                 9389155e0a9e008b2dc57ee000000000
                 7002400020bf0000020405b401010402
                 01020201""",
        aad = '4a2cbfe300000002',
        ctext_tag = """ff425c9b724599df7a3bcd510194e00d
        6a78107f1b0b1cbf06efae9d65a5d763
                 748a637985771d347f0545659f14e99d
                 ef842d8eb335f4eecfdbf831824b4c49
                 15956c96""",
        packet = """4a2cbfe3000000020102030405060708
                 ff425c9b724599df7a3bcd510194e00d
                 6a78107f1b0b1cbf06efae9d65a5d763
                 748a637985771d347f0545659f14e99d
                 ef842d8eb335f4eecfdbf831824b4c49
                 15956c96""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '00000000000000000000000000000000',
        spi = '00000000',
        seq = '00000001',
        nonce = '000000000000000000000000',
        plaintext = """4500003c99c500008001cb7a40679318
                 010101010800075c0200440061626364
                 65666768696a6b6c6d6e6f7071727374
                 75767761626364656667686901020201""",

        aad = '0000000000000001',
        ctext_tag = """4688daf2f973a392732909c331d56d60
                 f694abaa414b5e7ff5fdcdfff5e9a284
                 456476492719ffb64de7d9dca1e1d894
                 bc3bd57873ed4d181d19d4d5c8c18af3
                 f821d496eeb096e98ad2b69e4799c71d""",
        packet = """00000000000000010000000000000000
                 4688daf2f973a392732909c331d56d60
                 f694abaa414b5e7ff5fdcdfff5e9a284
                 456476492719ffb64de7d9dca1e1d894
                 bc3bd57873ed4d181d19d4d5c8c18af3
                 f821d496eeb096e98ad2b69e4799c71d""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '3de09874b388e6491988d0c3607eae1f',
        spi = '42f67e3f',
        seq = '1010101010101010',
        nonce = '57690e434e280000a2fca1a3',
        plaintext = """4500003c99c300008001cb7c40679318
                 010101010800085c0200430061626364
                 65666768696a6b6c6d6e6f7071727374
                 75767761626364656667686901020201""",
        aad = '42f67e3f1010101010101010',
        ctext_tag = """fba2caa4853cf9f0f22cb10d86dd83b0
                 fec75691cf1a04b00d1138ec9c357917
                 65acbd8701ad79845bf9fe3fba487bc9
                 1755e6662b4c8d0d1f5e22739530320a
                 e0d731cc978ecafaeae88f00e80d6e48""",
        packet = """42f67e3f101010104e280000a2fca1a3
                 fba2caa4853cf9f0f22cb10d86dd83b0
                 fec75691cf1a04b00d1138ec9c357917
                 65acbd8701ad79845bf9fe3fba487bc9
                 1755e6662b4c8d0d1f5e22739530320a
                 e0d731cc978ecafaeae88f00e80d6e48""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '3de09874b388e6491988d0c3607eae1f',
        spi = '42f67e3f',
        seq = '1010101010101010',
        nonce = '57690e434e280000a2fca1a3',
        plaintext = """4500001c42a200008001441f406793b6
        e00000020a00f5ff01020201""",
        aad = '42f67e3f1010101010101010',
        ctext_tag = """fba2ca845e5df9f0f22c3e6e86dd831e
                 1fc65792cd1af9130e1379ed369f071f
                 35e034be95f112e4e7d05d35""",
        packet = """42f67e3f101010104e280000a2fca1a3
                 fba2ca845e5df9f0f22c3e6e86dd831e
                 1fc65792cd1af9130e1379ed369f071f
                 35e034be95f112e4e7d05d35""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = """feffe9928665731c6d6a8f9467308308
                 feffe9928665731c""",
        spi = '0000a5f8',
        seq = '0000000a',
        nonce = 'cafebabefacedbaddecaf888',
        plaintext = """45000028a4ad4000400678800a01038f
                 0a010612802306b8cb712602dd6bb03e
                 501016d075680001""",
        aad = '0000a5f80000000a',
        ctext_tag = """a5b1f8066029aea40e598b8122de0242
                 0938b3ab33f828e687b8858b5bfbdbd0
                 315b27452144cc7795457b9652037f53
                 18027b5b4cd7a636""",
        packet = """0000a5f80000000afacedbaddecaf888
                 a5b1f8066029aea40e598b8122de0242
                 0938b3ab33f828e687b8858b5bfbdbd0
                 315b27452144cc7795457b9652037f53
                 18027b5b4cd7a636""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = 'abbccddef00112233445566778899aab',
        spi = '00000100',
        seq = '0000000000000001',
        nonce = 'decaf888cafedebaceface74',
        plaintext = """4500004933ba00007f119106c3fb1d10
                 c2b1d326c02831ce0035dd7b800302d5
                 00004e20001e8c18d75b81dc91baa047
                 6b91b924b280389d92c963bac046ec95
                 9b6266c04722b14923010101""",

        aad = '000001000000000000000001',
        ctext_tag = """18a6fd42f72cbf4ab2a2ea901f73d814
                 e3e7f243d95412e1c349c1d2fbec168f
                 9190feebaf2cb01984e65863965d7472
                 b79da345e0e780191f0d2f0e0f496c22
                 6f2127b27db35724e7845d68651f57e6
                 5f354f75ff17015769623436""",

        packet = """0000010000000001cafedebaceface74
                 18a6fd42f72cbf4ab2a2ea901f73d814
                 e3e7f243d95412e1c349c1d2fbec168f
                 9190feebaf2cb01984e65863965d7472
                 b79da345e0e780191f0d2f0e0f496c22
                 6f2127b27db35724e7845d68651f57e6
                 5f354f75ff17015769623436""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = """abbccddef00112233445566778899aab
                 abbccddef00112233445566778899aab""",
        spi = '17405e67',
        seq = '156f3126dd0db99b',
        nonce = '73616c74616e640169766563',
        plaintext = """45080028732c00004006e9f90a010612
                 0a01038f06b88023dd6bafbecb712602
                 50101f646d540001""",
        aad = '17405e67156f3126dd0db99b',
        ctext_tag = """f2d69ecdbd5a0d5b8d5ef38bad4da58d
                 1f278fde98ef67549d524a3018d9a57f
                 f4d3a31ce673119e451626c2415771e3
                 b7eebca614c89b35""",
        packet = """17405e67dd0db99b616e640169766563
                 f2d69ecdbd5a0d5b8d5ef38bad4da58d
                 1f278fde98ef67549d524a3018d9a57f
                 f4d3a31ce673119e451626c2415771e3
                 b7eebca614c89b35""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '3de09874b388e6491988d0c3607eae1f',
        spi = '42f67e3f',
        seq = '1010101010101010',
        nonce = '57690e434e280000a2fca1a3',
        plaintext = """45000049333e00007f119182c3fb1d10
                 c2b1d326c02831ce0035cb458003025b
                 000001e0001e8c18d65759d52284a035
                 2c71475c8880391c764d6e5ee0496b32
                 5ae270c03899493915010101""",
        aad = '42f67e3f1010101010101010',
        ctext_tag = """fba2cad12fc1f9f00d3cebf305410db8
                 3d7784b607323d220f24b0a97d541828
                 00cadb0f68d99ef0e0c0c89ae9bea888
                 4e52d65bc1afd0740f742444747b5b39
                 ab533163aad4550ee5160975cdb608c5
                 769189609763b8e18caa81e2""",
        packet = """42f67e3f101010104e280000a2fca1a3
                 fba2cad12fc1f9f00d3cebf305410db8
                 3d7784b607323d220f24b0a97d541828
                 00cadb0f68d99ef0e0c0c89ae9bea888
                 4e52d65bc1afd0740f742444747b5b39
                 ab533163aad4550ee5160975cdb608c5
                 769189609763b8e18caa81e2""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = """abbccddef00112233445566778899aab
                 abbccddef00112233445566778899aab""",
        spi = '17405e67',
        seq = '156f3126dd0db99b',
        nonce = '73616c74616e640169766563',
        plaintext = """636973636f0172756c65730174686501
                 6e6574776501646566696e6501746865
                 746563686e6f6c6f6769657301746861
                 7477696c6c01646566696e65746f6d6f
                 72726f7701020201""",
        aad = '17405e67156f3126dd0db99b',
        ctext_tag = """d4b7ed86a1777f2ea13d6973d324c69e
                 7b43f826fb56831226508bebd2dceb18
                 d0a6df10e5487df074113e14c641024e
                 3e6773d91a62ee429b043a10e3efe6b0
                 12a49363412364f8c0cac587f249e56b
                 11e24f30e44ccc76""",
        packet = """17405e67dd0db99b616e640169766563
                 d4b7ed86a1777f2ea13d6973d324c69e
                 7b43f826fb56831226508bebd2dceb18
                 d0a6df10e5487df074113e14c641024e
                 3e6773d91a62ee429b043a10e3efe6b0
                 12a49363412364f8c0cac587f249e56b
                 11e24f30e44ccc76""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = '7d773d00c144c525ac619d18c84a3f47',

        spi = '335467ae',
        seq = 'ffffffff',

        nonce = 'd966426743457e9182443bc6',
        plaintext = '01020201',

        aad = '335467aeffffffff',

        ctext_tag = """437f866bcb3f699fe9b0822bac961c45
                 04bef270""",

        packet = """335467aeffffffff43457e9182443bc6
                 437f866bcb3f699fe9b0822bac961c45
                 04bef270""",

    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = 'abbccddef00112233445566778899aab',

        spi = '00000100',
        seq = '0000000000000001',

        nonce = 'decaf888cafedebaceface74',
        plaintext = """746f016265016f72016e6f7401746f01
                 62650001""",

        aad = '000001000000000000000001',

        ctext_tag = """29c9fc69a197d038ccdd14e2ddfcaa05
                 43332164412503524303ed3c6c5f2838
                 43af8c3e""",

        packet = """0000010000000001cafedebaceface74
                 29c9fc69a197d038ccdd14e2ddfcaa05
                 43332164412503524303ed3c6c5f2838
                 43af8c3e""",
    ),
    Testcase(
        algorithm = 'AES-GCM-ESP',
        key = """6c6567616c697a656d6172696a75616e
                 61616e64646f69746265666f72656961""",
        spi = '796b6963',
        seq = 'ffffffffffffffff',
        nonce = '7475726e333021696765746d',
        plaintext = """45000030da3a00008001df3bc0a80005
                 c0a800010800c6cd0200070061626364
                 65666768696a6b6c6d6e6f7071727374
                 01020201""",
        aad = '796b6963ffffffffffffffff',
        ctext_tag = """f97ab2aa356d8edce17644ac8c78e25d
                 d24dedbb29ebf1b64a274b39b49c3a86
                 4cd3d78ca4ae68a32b42458fb57dbe82
                 1dcc63b9d0937ba2945f669368661a32
                 9fb4c053""",
        packet = """796b6963ffffffff333021696765746d
                 f97ab2aa356d8edce17644ac8c78e25d
                 d24dedbb29ebf1b64a274b39b49c3a86
                 4cd3d78ca4ae68a32b42458fb57dbe82
                 1dcc63b9d0937ba2945f669368661a32
                 9fb4c053""",

    ),

    # From https://tools.ietf.org/html/rfc7634#page-9
    Testcase(
        algorithm = 'CHACHA20_POLY1305',
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

    # From https://tools.ietf.org/html/rfc7539#page-22
    # Testcase(
    #     algorithm = 'CHACHA20_POLY1305',
    #     plaintext = """
    #     4c 61 64 69 65 73 20 61 6e 64 20 47 65 6e 74 6c
    #     65 6d 65 6e 20 6f 66 20 74 68 65 20 63 6c 61 73
    #     73 20 6f 66 20 27 39 39 3a 20 49 66 20 49 20 63
    #     6f 75 6c 64 20 6f 66 66 65 72 20 79 6f 75 20 6f
    #     6e 6c 79 20 6f 6e 65 20 74 69 70 20 66 6f 72 20
    #     74 68 65 20 66 75 74 75 72 65 2c 20 73 75 6e 73
    #     63 72 65 65 6e 20 77 6f 75 6c 64 20 62 65 20 69
    #     74 2e""",

    #     aad = """  50 51 52 53 c0 c1 c2 c3 c4 c5 c6 c7""",

    #     key = """
    #     80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
    #     90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f""",

    #     nonce = "  40 41 42 43 44 45 46 47",
    #     ctext_tag = """
    #     d3 1a 8d 34 64 8e 60 db 7b 86 af bc 53 ef 7e c2
    #     a4 ad ed 51 29 6e 08 fe a9 e2 b5 a7 36 ee 62 d6
    #     3d be a4 5e 8c a9 67 12 82 fa fb 69 da 92 72 8b
    #     1a 71 de 0a 9e 06 0b 29 05 d6 a5 b6 7e cd 3b 36
    #     92 dd bd 7f 2d 77 8b 8c 98 03 ae e3 28 09 1b 58
    #     fa b3 24 e4 fa d6 75 94 55 85 80 8b 48 31 d7 bc
    #     3f f4 de f0 8e 4b 7a 9d e5 76 d2 65 86 ce c6 4b
    #     61 16
    #     1a e1 0b 59 4f 09 e2 6a 7e 90 2e cb d0 60 06 91
    #     """,
    # ),

    Testcase(
        algorithm = 'CHACHA20_POLY1305',
        plaintext = """00 00 00 0c 00 00 40 01 00 00 00 0a 00""",
        ctext_tag = """61 03 94 70 1f 8d 01 7f 7c 12 92 48 89
        6b 71 bf e2 52 36 ef d7 cd c6 70 66 90 63 15 b2""",
        aad = """c0 c1 c2 c3 c4 c5 c6 c7 d0 d1 d2 d3 d4 d5 d6 d7
        2e 20 25 00 00 00 00 09 00 00 00 45 29 00 00 29""",
        nonce = """a0 a1 a2 a3 10 11 12 13 14 15 16 17 """,
        key = """
        80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
        90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f""",

    ),
]
    
