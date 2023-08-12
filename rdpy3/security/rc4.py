"""
    Copyright (C) 2012 Bo Zhu http://about.bozhu.me

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""


def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    # print("KEY:", key)
    for i in range(256):
        # print(S[i], key[i % keylength])
        k = key[i % keylength]
        if isinstance(k, str):
            k = ord(k)
        elif not isinstance(k, int):
            raise TypeError("Key must be a string or a list of integers")
        j = (j + S[i] + k) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S
    # for s in S:
    #     yield s


def PRGA(S):
    i = 0
    j = 0
    # S = list(S)
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


def RC4Key(key):
    return RC4(key)


def crypt(keystream, plaintext: bytes) -> bytes:
    # print("KEYSTREAM?", keystream)
    # if keystream == "RC4 bad crypt": return keystream
    # try:
    return bytes([(c if isinstance(c, int) else ord(c)) ^ next(keystream) for c in plaintext])
    # except:
    #     return "RC4 bad crypt"
