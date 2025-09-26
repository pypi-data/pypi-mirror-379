# Copyright (c) 2015, Hubert Kario
#
# See the LICENSE file for legal information regarding use of this file.

# compatibility with Python 2.6, for that we need unittest2 package,
# which is not available on 3.3 or 3.4
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from tlslite.utils.rsakey import RSAKey
from tlslite.utils.python_rsakey import Python_RSAKey
from tlslite.utils.cryptomath import *
from tlslite.errors import *
from tlslite.utils.keyfactory import parsePEMKey, generateRSAKey
from tlslite.utils.compat import a2b_hex, remove_whitespace
try:
    import mock
    from mock import call
except ImportError:
    import unittest.mock as mock
    from unittest.mock import call


def calc_kdk(key, ciphertext):
    key_hash = secureHash(numberToByteArray(key.d, numBytes(key.n)), "sha256")

    kdk = secureHMAC(key_hash, ciphertext, "sha256")

    return kdk


def calc_lengths(key, kdk):
    lengths_bytes = key._dec_prf(kdk, b"length", 128 * 2 * 8)

    max_sep_offset = numBytes(key.n) - 10
    mask = (1 << numBits(max_sep_offset)) - 1

    lengths_iter = iter(lengths_bytes)

    lengths = [
        ((i << 8) + j) & mask
        for i, j in zip(lengths_iter, lengths_iter)
    ]
    return lengths


class TestRSAPSS_components(unittest.TestCase):
    # component functions NOT tested from test vectors

    def setUp(self):
        self.rsa = Python_RSAKey()

    def test_unknownRSAType(self):
        message = bytearray(b'\xad\x8f\xd1\xf7\xf9' +
                                                 b'\x7fgrRS\xce}\x18\x985' +
                                                 b'\xb3')
        signed = bytearray(
                             b'\xb80\x12s\xbb\xd9j\xce&U\x08\x14\xb2\x070' +
                             b'\xc7\xc8\xa8\xa0\xc1\xc3\xf3\xd41\xad\xbe' +
                             b'\xe8\x1dN\x94\xf6sx\x02\xed\xfb\x0b\x0b\x85' +
                             b'\xc5N\xff\x04z\xec\x13\x86O\x15\xe8|\xae\xc6' +
                             b'\x1c\r\xcd\xec\xf4\xb1\xb5$\xf2\x17\xff\xf6' +
                             b'\xc2\xf5\xd2\x8a\xd2\x98\xa8\xb7\xe0;\xab\xe0' +
                             b'\xe9P\xd9\xea\x86\xb3\xeb)\xa3\x98\xb4e\xb5P' +
                             b'\x07\x14\xf1?\xa8i\xb7\xc6\x94\x1c9\x1fX>@' +
                             b'\xe3')
        with self.assertRaises(UnknownRSAType):
            self.rsa.hashAndVerify(message, signed, rsaScheme='foo',
                                   hAlg='sha1')

    def test_encodingError(self):
        mHash = secureHash(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'),
                'sha1')
        with self.assertRaises(EncodingError):
            self.assertEqual(self.rsa.EMSA_PSS_encode(mHash, 10, 'sha1', 10),
                bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3' +
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2\xf4' +
                          b'\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13\xfd' +
                          b'\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'))

    def test_maskTooLong(self):
        with self.assertRaises(MaskTooLongError):
            self.rsa.MGF1(bytearray(b'\xad\x8f\xd1\xf7\xf9\x7fgrRS\xce}\x18' +
                                    b'\x985\xb3'), 85899345921, 'sha1')

    def test_EMSA_PSS_verifyInvalidSignature29(self):
        with self.assertRaises(InvalidSignature):
            self.rsa.EMSA_PSS_verify(
                bytearray(b'\x6b\x9c\xfa\xc0\xba\x1c\x78\x90\xb1\x3e\x38\x1c' +
                          b'\xe7\x52\x19\x5c\xc1\x37\x52\x37\xdb\x2a\xfc\xf6' +
                          b'\xa9\xdc\xd1\xf9\x5e\xc7\x33\xa8\x0c\xc1\x70\xad' +
                          b'\x0d\xd2\x44\x61\xa3\x43\x9f\x83\xdb\xf7\xa9\x30' +
                          b'\xb7\xff\x03\x0f\x8b\x68\x50\xcd\xa8\x57\xf5\xc9' +
                          b'\x38\x59\x1c\x10\x69\xf4\xff\x8b\xce\x82\x63\x77' +
                          b'\x02\x3f\x62\x16\x8e\xa0\x6e\xa4\x0c\xe6\x93\x8d' +
                          b'\x8d\xf4\xfc\xdd\x39\x5d\xb9\xf8\x35\xc2\xc0\x8b' +
                          b'\xca\x5b\x31\xc2\xc3\xd3\xde\xbc\x16\x59\x0a\x3c' +
                          b'\xc7\xf4\x71\xa1\x0a\x16\x89\x18\xa8\x75\x08\x10' +
                          b'\xa3\x16\xa6\xee\x1d\xaa\x24\x02'),
                bytearray(b'\x56\x2d\x87\xb5\x78\x1c\x01\xd1\x66\xfe\xf3\x97' +
                          b'\x26\x69\xa0\x49\x5c\x14\x5b\x89\x8a\x17\xdf\x47' +
                          b'\x43\xfb\xef\xb0\xa1\x58\x2b\xd6\xba\x9d\xf1\xb0' +
                          b'\xf7\x0f\xa4\xb4\x48\x5a\x75\x7d\x91\x74\x97\x2e' +
                          b'\x69\x19\x29\xf4\xc1\xd3\x45\x19\xbc\xcc\x7a\x5c' +
                          b'\x4c\x8b\xca\x14\x4e\x58\xbe\x08\x39\xe8\x7e\x1e' +
                          b'\x9f\xe9\x01\xf0\xda\x40\x29\xb3\x1e\x78\x00\xdc' +
                          b'\x79\xe8\xc1\xbd\x68\xaf\x41\xc3\x93\xf8\x11\xe9' +
                          b'\x9e\xec\xdb\x52\xf6\x97\x8b\x18\x42\xe1\x70\xc0' +
                          b'\x15\x3e\xba\x5f\x18\x45\xff\xcd\x36\xff\x3f\x79' +
                          b'\x95\x53\x9f\x3c\x74\xde\x3c\xaa'),
                1023, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature(self):
        with self.assertRaises(InvalidSignature):
            self.rsa.EMSA_PSS_verify(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'),
                bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3' +
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2' +
                          b'\xf4\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13' +
                          b'\xfd\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'),
                10, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature2(self):
        with self.assertRaises(InvalidSignature):
            self.rsa.EMSA_PSS_verify(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'),
                bytearray(b'eA=!Fq4\xee\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3' +
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2' +
                          b'\xf4\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13' +
                          b'\xfd\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'),
                1023, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature3(self):
        with self.assertRaises(InvalidSignature):
            self.rsa.EMSA_PSS_verify(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'),
                bytearray(b'\xffA=!Fq4\xee\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3'+
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2' +
                          b'\xf4\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13' +
                          b'\xfd\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'),
                1023, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature4(self):
        def m(p, hAlg):
            r = secureHash(p, hAlg)
            r[getattr(hashlib, hAlg)().digest_size-1] = r[getattr(
                hashlib, hAlg)().digest_size-1]-1
            return r

        with mock.patch('tlslite.utils.rsakey.secureHash', m):
            with self.assertRaises(InvalidSignature):
                self.rsa.EMSA_PSS_verify(
                    bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|' +
                              b'\xca<\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9' +
                              b'\xb0!@\xfe#\x89\x08\xe4\xf6\xc1\x8f\x07\xa8' +
                              b'\x9ch|\x86\x84f\x9b\x1f\x1d\xb2\xba\xf9%' +
                              b'\x1a<\x82\x9f\xac\xcbI0\x84\xe1n\xc9\xe2' +
                              b'\x8dX\x86\x80t\xa5\xd6"\x16g\xddnR\x8d\x16' +
                              b'\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c\x849\xaf8' +
                              b'\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4\xa5' +
                              b'\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                              b'\x8c\xdf\xe4\x08qh'),
                    bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(' +
                              b'\xe3\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2' +
                              b'\x08\xa2<Q\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f' +
                              b'\x83\x9f\xe2\xf4\xb9\x89\x9b\xdbv\xb8\xb1&' +
                              b'\r\xa8\xdfA\x13\xfd\xed\xce\x85\xb5\x0e\xae' +
                              b'\xd0t\xe5`\xbaen"\xcd_=:V\'A\xe32u%7\x8b\xed' +
                              b'\x16\xc7$\x919\xa5\x18XA\xa3\xf5r\xad\x8f' +
                              b'\xd1\xf7\xf9\x7f;\x01\xccgrRS\xce}\x18\x985' +
                              b'\xb3\xbc'),
                    1023, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature5(self):
        def m(leght):
            return bytearray(b'\x11"3DUT2\x16x\x90')

        with self.assertRaises(InvalidSignature):
            with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
                self.rsa.EMSA_PSS_verify(
                    bytearray(b'\xc8\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|' +
                              b'\xca<\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9' +
                              b'\xb0!@\xfe#\x89\x08\xe4\xf6\xc1\x8f\x07\xa8' +
                              b'\x9ch|\x86\x84f\x9b\x1f\x1d\xb2\xba\xf9%' +
                              b'\x1a<\x82\x9f\xac\xcbI0\x84\xe1n\xc9\xe2' +
                              b'\x8dX\x86\x80t\xa5\xd6"\x16g\xddnR\x8d\x16' +
                              b'\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c\x849\xaf8' +
                              b'\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4\xa5' +
                              b'\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                              b'\x8c\xdf\xe4\x08qh'),
                    bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(' +
                              b'\xe3\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2' +
                              b'\x08\xa2<Q\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f' +
                              b'\x83\x9f\xe2\xf4\xb9\x89\x9b\xdbv\xb8\xb1&' +
                              b'\r\xa8\xdfA\x13\xfd\xed\xce\x85\xb5\x0e\xae' +
                              b'\xd0t\xe5`\xbaen"\xcd_=:V\'A\xe32u%7\x8b\xed' +
                              b'\x16\xc7$\x919\xa5\x18XA\xa3\xf5r\xad\x8f' +
                              b'\xd1\xf7\xf9\x7f;\x01\xccgrRS\xce}\x18\x985' +
                              b'\xb3\xbc'),
                    1023, 'sha1', 10)

    def test_EMSA_PSS_verifyInvalidSignature6(self):
        def m(leght):
            return bytearray(b'\x11"3DUT2\x16x\x90')

        with self.assertRaises(InvalidSignature):
            with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
                self.rsa.EMSA_PSS_verify(
                    bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a' +
                              b'\x8d|\xca<\xc5\xc0y\x02@)\xf3\xba\xe5' +
                              b'\x10\xf9\xb0!@\xfe#\x89\x08\xe4\xf6\xc1' +
                              b'\x8f\x07\xa8\x9ch|\x86\x84f\x9b\x1f\x1d' +
                              b'\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0\x84' +
                              b'\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"' +
                              b'\x16g\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf' +
                              b'\xaflM\xce\x8c\x849\xaf8\xce\xaa\xaa\x9c' +
                              b'\xe2\xec\xae{\xc8\xf4\xa5\xa5^;\xf9m\xf9' +
                              b'\xcdW\\O\x9c\xb3\'\x95\x1b\x8c\xdf\xe4' +
                              b'\x08qh'),
                    bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX' +
                              b'\xdc~(\xe3\x92\x17z\xa5-\xcfV\xd4)\x99' +
                              b'\x8fJ\xb2\x08\xa2<Q\x02e\xb4\xe0\xecq' +
                              b'\xa3:\xe0I\x1f\x83\x9f\xe2\xf4\xb9\x89' +
                              b'\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13\xfd' +
                              b'\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`' +
                              b'\xbaen"\xcd_=:V\'A\xe32u%7\x8b\xed\x17' +
                              b'\xc7$\x919\xa5\x18XA\xa3\xf5r\xad\x8f' +
                              b'\xd1\xf7\xf9\x7f;\x01\xccgrRS\xce}\x18' +
                              b'\x985\xb3\xbc'),
                    1023, 'sha1', 10)

    def test_MGF1_1(self):
        self.assertEqual(self.rsa.MGF1(bytearray(b'\xad\x8f\xd1\xf7\xf9' +
                                                 b'\x7fgrRS\xce}\x18\x985' +
                                                 b'\xb3'), 107, 'sha1'),
                         bytearray(
                             b'\xb80\x12s\xbb\xd9j\xce&U\x08\x14\xb2\x070' +
                             b'\xc7\xc8\xa8\xa0\xc1\xc3\xf3\xd41\xad\xbe' +
                             b'\xe8\x1dN\x94\xf6sx\x02\xed\xfb\x0b\x0b\x85' +
                             b'\xc5N\xff\x04z\xec\x13\x86O\x15\xe8|\xae\xc6' +
                             b'\x1c\r\xcd\xec\xf4\xb1\xb5$\xf2\x17\xff\xf6' +
                             b'\xc2\xf5\xd2\x8a\xd2\x98\xa8\xb7\xe0;\xab\xe0' +
                             b'\xe9P\xd9\xea\x86\xb3\xeb)\xa3\x98\xb4e\xb5P' +
                             b'\x07\x14\xf1?\xa8i\xb7\xc6\x94\x1c9\x1fX>@' +
                             b'\xe3'))

    def test_MGF1_2(self):
        self.assertEqual(self.rsa.MGF1(bytearray(b'\xad\x8f\xd1\xf7\xf9' +
                                                 b'\x7fgrRS\xce}\x18\x985' +
                                                 b'\xb3'), 40, 'sha1'),
                         bytearray(
                             b'\xb80\x12s\xbb\xd9j\xce&U\x08\x14\xb2\x070' +
                             b'\xc7\xc8\xa8\xa0\xc1\xc3\xf3\xd41\xad\xbe\xe8' +
                             b'\x1dN\x94\xf6sx\x02\xed\xfb\x0b\x0b\x85\xc5'))

    def test_EMSA_PSS_encode(self):
        def m(leght):
            return bytearray(b'\x11"3DUT2\x16x\x90')
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = SHA1(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'))
            self.assertEqual(self.rsa.EMSA_PSS_encode(mHash, 1023, 'sha1', 10),
                bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3' +
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2\xf4' +
                          b'\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13\xfd' +
                          b'\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'))

    def test_EMSA_PSS_verify(self):
        def m(leght):
            return bytearray(b'\x11"3DUT2\x16x\x90')
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = SHA1(
                bytearray(b'\xc7\xf5\'\x0f\xcar_\x9b\xd1\x9fQ\x9a\x8d|\xca<' +
                          b'\xc5\xc0y\x02@)\xf3\xba\xe5\x10\xf9\xb0!@\xfe#' +
                          b'\x89\x08\xe4\xf6\xc1\x8f\x07\xa8\x9ch|\x86\x84f' +
                          b'\x9b\x1f\x1d\xb2\xba\xf9%\x1a<\x82\x9f\xac\xcbI0' +
                          b'\x84\xe1n\xc9\xe2\x8dX\x86\x80t\xa5\xd6"\x16g' +
                          b'\xddnR\x8d\x16\xfe,\x9f=\xb4\xcf\xaflM\xce\x8c' +
                          b'\x849\xaf8\xce\xaa\xaa\x9c\xe2\xec\xae{\xc8\xf4' +
                          b'\xa5\xa5^;\xf9m\xf9\xcdW\\O\x9c\xb3\'\x95\x1b' +
                          b'\x8c\xdf\xe4\x08qh'))
            self.assertTrue(self.rsa.EMSA_PSS_verify(mHash,
                bytearray(b'eA=!Fq4\xce\xef5?\xf4\xec\xd8\xa6FPX\xdc~(\xe3' +
                          b'\x92\x17z\xa5-\xcfV\xd4)\x99\x8fJ\xb2\x08\xa2<Q' +
                          b'\x02e\xb4\xe0\xecq\xa3:\xe0I\x1f\x83\x9f\xe2' +
                          b'\xf4\xb9\x89\x9b\xdbv\xb8\xb1&\r\xa8\xdfA\x13' +
                          b'\xfd\xed\xce\x85\xb5\x0e\xae\xd0t\xe5`\xbaen"' +
                          b'\xcd_=:V\'A\xe32u%7\x8b\xed\x16\xc7$\x919\xa5' +
                          b'\x18XA\xa3\xf5r\xad\x8f\xd1\xf7\xf9\x7f;\x01' +
                          b'\xccgrRS\xce}\x18\x985\xb3\xbc'),
                1023, 'sha1', 10))

class TestRSAPSS_mod1026(unittest.TestCase):

    n = int("2b35541ee2850f34c7727e13eed15d60fb62c0cf230c31bbd0766b6994cff4e5e"
            "6279ad00e5fedabd0ed31c77956be0d91c0d9435bf73b270a740fb792c0819ce7"
            "cdac92189d6fcc08d58640c44b69c8fea7c5301a3a62960dee0698ab49ab5f8f1"
            "c4a465c244b79c293f108a9f5ed8425bacba0eb51dcee4a3c3c4d5d81fae70bac"
            "e8ba8c79a2a9cf2be32e0ef2a23b5755743bd356bac5733796d34ebba2d420ae6"
            "e384208b9d8cdd83dced8f6f587b744f814a5d3fcd409869220bb63439cf50fa0"
            "24de4bfad2061706a31c77a8589ac218c7fd90b135f1975783b2765ce88d1570e"
            "812ebea195ae06639d88688e505582dc49ddcab767741cba145be11bf",
            16)
    e = int("65537", 10)
    d = int("024d35eceb3e11404b7b82d1c6ffea0c77779c33ac7742d2f158cd81f3465c923"
            "e7f4f94d39f3286db7b37129c190dc8a541f390cdfe4e6d56f635bc1e9a188d66"
            "1fa398a8ad023e891deea7d68cf9d6961213c3eb31befca5434fa0a4472954cec"
            "7c0011d796577d7f08f7f59a65aff960eec37e7311626af57a412aeef7490fce4"
            "1fdac6d20c4034ac68187a824d6c1a642d917450ede20578cc7812c0109094e28"
            "8b5fdd74b1dc7cb94ecc864b5867e143689cba68a0c1d044569e3cd35f1e815c4"
            "c023ebb24b21dbcdd30e0c7375db1f641cb364470a8378643fd3e6a7692708269"
            "9264cb9dee983832dfac3ee7cee32a35738b5c1dc16bf62f9dcd7bf59",
            16)
    p = int("72a5b2ff09d1ad78f1c72e9bc9c0cf1bcc9b03a1595a153886a0273f515e58cc4"
            "e27adfb6fe52dc9bd95a76056a1093350f5cd9e1a6aeecc6137540fe747f3e3f5"
            "3f2d71fdf4d7ae9b2576830c40f04a8851af78f27b2378056a80053a8a31aed27"
            "0bf757c2e1dc82857dd9a490fc1a442d22c9d7d54137483793486ded1e773",
            16)
    q = int("607b3d256cbe2c063105065825c062d2b4495da3362090820b8cf42bb2434e879"
            "b271543741b691307a75d92b6251723f4e31a79e76ab0b45928200fb67931b8b4"
            "28f89bcd10f1816adffc97bfe0f50b50e63cdcf9da57ee93be926654d5b4e1fe0"
            "33e96ace587ffb2af7ec2c37664a1dfaaec8e9810ba7c13f0f15b17f92185",
            16)
    dP = d % (p - 1)
    dQ = d % (q - 1)
    qInv = invMod(q, p)
    message = bytearray(b'\xc7\xf5\x27\x0f\xca\x72\x5f\x9b\xd1\x9f\x51' +
                        b'\x9a\x8d\x7c\xca\x3c\xc5\xc0\x79\x02\x40\x29' +
                        b'\xf3\xba\xe5\x10\xf9\xb0\x21\x40\xfe\x23\x89' +
                        b'\x08\xe4\xf6\xc1\x8f\x07\xa8\x9c\x68\x7c\x86' +
                        b'\x84\x66\x9b\x1f\x1d\xb2\xba\xf9\x25\x1a\x3c' +
                        b'\x82\x9f\xac\xcb\x49\x30\x84\xe1\x6e\xc9\xe2' +
                        b'\x8d\x58\x86\x80\x74\xa5\xd6\x22\x16\x67\xdd' +
                        b'\x6e\x52\x8d\x16\xfe\x2c\x9f\x3d\xb4\xcf\xaf' +
                        b'\x6c\x4d\xce\x8c\x84\x39\xaf\x38\xce\xaa\xaa' +
                        b'\x9c\xe2\xec\xae\x7b\xc8\xf4\xa5\xa5\x5e\x3b' +
                        b'\xf9\x6d\xf9\xcd\x57\x5c\x4f\x9c\xb3\x27\x95' +
                        b'\x1b\x8c\xdf\xe4\x08\x71\x68')

    def setUp(self):
        self.rsa = Python_RSAKey(self.n, self.e, self.d, self.p, self.q,
                                 self.dP, self.dQ, self.qInv)

    def test_RSAPSS_1026(self):
        signed = bytearray(b'\x0f\xd2\xef/\xa6\xb6+j\xce\xfc\x16.\xce\x99WH_' +
                           b'\x94\xb5\x15\xf1\x8a\xf3\xaa\x12\x82R.\xe8&\xc6' +
                           b'\xf9\xd3\xa9STTW\x0f/L`\nQ>\xeb\t{\x8c\x13\xa3' +
                           b'\xfbm\xe7\xd2\r\xbc!\x91\x07\xaf \xf9\xd3V@' +
                           b'\xb0z,\xb8q\xec$A\x0c\x13\xda\xb7/\xa4U\xa3' +
                           b'\xbb7A\x92\x9b\'\xcf\x9f,\xad\x18\x1a\xf9_\x87' +
                           b'\xf5\x0e\x02\x08\x04\x88\xa3uDnrI\xff\xd0\xa7~_' +
                           b'\xdc>"}%i\xc4\x1a"w\xfdW\x14\x91\xae\x1b\x1f' +
                           b'\xcd\xd9L\xf7(w-]f\xc7\xdc\x82\n\x00[4\xf1f\xf6' +
                           b'\x141\x0e\x12\x13\xf8\x96fc\xc1\x15\xca\x95W' +
                           b'\xd8i\x0f@\x94\x01%\x14(Z\x88\xe1\x00\xf4\xf7' +
                           b'\x81\xfd,\x899x\x9b"\xa4\x01\xef@4@\x9cY\xe2' +
                           b'\x91\x89;{\x8dh\x80Ei\x1b\xf1\x7f1\x93\xe1\xa1j' +
                           b'\xb0\xf1Z\x0c>\xcc\xbeX&$\xfd\x96\xd3\x1e\x92' +
                           b'\xf5\x9b\xbd\x1a\xaa\t\x85>\x13\xb5\xf1s\xa7YN' +
                           b'\x1f\xdb\xa1*\xcc\x93\xa2\xbf\xfd\xe0\xda>0')
        mHash = secureHash(self.message, 'sha1')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(
            mHash, signed, 'sha1', 0))

class TestRSAPSS_mod1024(unittest.TestCase):
    # Test cases from http://csrc.nist.gov/groups/STM/cavp/
    # file SigVerPSS_186-3.rsp

    n = int("be499b5e7f06c83fa0293e31465c8eb6b58af920bae52a7b5b9bfeb7aa72db126"
            "4112eb3fd431d31a2a7e50941566929494a0e891ed5613918b4b51b0d1fb97783"
            "b26acf7d0f384cfb35f4d2824f5dd380623a26bf180b63961c619dcdb20cae406"
            "f22f6e276c80a37259490cfeb72c1a71a84f1846d330877ba3e3101ec9c7b",
            16)
    e = int("00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "0000000000000000000000000000000000000000000000000000000000011",
            16)
    d = int("0d0f17362bdad181db4e1fe03e8de1a3208989914e14bf269558826bfa20faf4b"
            "68dba6bb989a01f03a21c44665dc5f648cb5b59b954eb1077a80263bd22cdfb88"
            "d39164b7404f4f1106ee01cf60b77695748d8fdaf9fd428963fe75144010b1934"
            "c8e26a88239672cf49b3422a07c4d834ba208d570fe408e7095c90547e68d",
            16)
    p = int("e7a80c5d211c06acb900939495f26d365fc2b4825b75e356f89003eaa5931e6be"
            "5c3f7e6a633ad59db6289d06c354c235e739a1e3f3d39fb40d1ffb9cb44288f",
            16)
    q = int("d248aa248000f720258742da67b711940c8f76e1ecd52b67a6ffe1e49354d66ff"
            "84fa601804743f5838da2ed4693a5a28658d6528cc1803bf6c8dc73c5230b55",
            16)
    dP = d % (p - 1)
    dQ = d % (q - 1)
    qInv = invMod(q, p)
    message = bytearray(b'\xc7\xf5\x27\x0f\xca\x72\x5f\x9b\xd1\x9f\x51' +
                        b'\x9a\x8d\x7c\xca\x3c\xc5\xc0\x79\x02\x40\x29' +
                        b'\xf3\xba\xe5\x10\xf9\xb0\x21\x40\xfe\x23\x89' +
                        b'\x08\xe4\xf6\xc1\x8f\x07\xa8\x9c\x68\x7c\x86' +
                        b'\x84\x66\x9b\x1f\x1d\xb2\xba\xf9\x25\x1a\x3c' +
                        b'\x82\x9f\xac\xcb\x49\x30\x84\xe1\x6e\xc9\xe2' +
                        b'\x8d\x58\x86\x80\x74\xa5\xd6\x22\x16\x67\xdd' +
                        b'\x6e\x52\x8d\x16\xfe\x2c\x9f\x3d\xb4\xcf\xaf' +
                        b'\x6c\x4d\xce\x8c\x84\x39\xaf\x38\xce\xaa\xaa' +
                        b'\x9c\xe2\xec\xae\x7b\xc8\xf4\xa5\xa5\x5e\x3b' +
                        b'\xf9\x6d\xf9\xcd\x57\x5c\x4f\x9c\xb3\x27\x95' +
                        b'\x1b\x8c\xdf\xe4\x08\x71\x68')
    salt = bytearray(b'\x11\x22\x33\x44\x55\x54\x32\x16\x78\x90')

    def setUp(self):
        self.rsa = Python_RSAKey(self.n, self.e, self.d, self.p, self.q,
                                 self.dP, self.dQ, self.qInv)

    def test_RSAPSS_sha1(self):
        intendedS = bytearray(b'\x96\xc3\xf6\x92\x70\x1d\x14\xeb\xbe\xf9' +
                              b'\x22\xa5\xc2\x25\x7f\x71\x3d\x20\xa9\x2c' +
                              b'\x69\x38\x74\xe0\x35\xb5\xb0\x65\x15\x92' +
                              b'\xab\x1b\x96\x43\xd3\x81\xd6\xb4\xa9\x70' +
                              b'\xda\xd7\xe2\x38\x00\xe4\x9d\x1a\x66\x57' +
                              b'\xc3\x33\x35\x8e\x9b\xfa\x5c\x71\x34\x93' +
                              b'\x53\x3b\x90\xb0\x23\x4a\x0d\x0d\xcf\x42' +
                              b'\xd0\xa6\x6b\x48\x03\xe4\xdb\x78\x06\x19' +
                              b'\xcc\xab\x6b\xa5\xbb\x27\xd0\x43\xf3\x2d' +
                              b'\x8e\x60\x1e\x2f\x12\xee\x08\xae\xce\x5c' +
                              b'\x47\xcc\x2e\x02\x89\xcd\xbf\x25\xc9\x77' +
                              b'\xcf\x1b\xea\xdc\x04\x74\x21\x50\xbe\xea' +
                              b'\xd6\x96\x2d\xdd\xa9\xe9\x1e\x17')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(self.message, 'sha1')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha1', 10)
            self.assertEqual(signed, intendedS)

    def test_RSAPSS_sha224(self):
        intendedS = bytearray(b'\x47\xbd\x25\xf8\x19\xbe\x0f\x7e\xe8\x48\xa3' +
                              b'\x3c\x19\x54\xb5\xbb\xc5\xb0\x0f\xf1\x04\xa2' +
                              b'\xab\x98\xf4\x8c\x38\xe0\x17\x6a\x74\xd7\x07' +
                              b'\xb4\x4c\x36\xdf\x8d\x8c\x12\xda\x49\xec\xec' +
                              b'\x7b\xdc\xc3\x51\x45\x39\xdb\x2b\xd8\xe0\x64' +
                              b'\xca\x62\x89\xaf\xd0\x72\xfd\x86\xc9\xf4\x2e' +
                              b'\x56\x58\xb4\x35\x5b\x34\x19\x30\x4e\x0a\xe9' +
                              b'\x28\x57\x12\x8a\x3c\x5e\xbc\x9b\xa6\x01\x38' +
                              b'\xaf\x67\x44\xec\xf7\x52\x1a\xa1\x11\x94\xac' +
                              b'\x95\x20\x6c\xf7\xa8\x0b\xe9\xca\x5f\x4e\x58' +
                              b'\x49\xae\x67\xf0\x73\xdb\x7b\x69\x2f\xd9\x39' +
                              b'\xcb\x31\xed\x6b\xf5\xe0\x66')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(self.message, 'sha224')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha224', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha256(self):
        intendedS = bytearray(b'\x11\xe1\x69\xf2\xfd\x40\xb0\x76\x41\xb9\x76' +
                              b'\x8a\x2a\xb1\x99\x65\xfb\x6c\x27\xf1\x0f\xcf' +
                              b'\x03\x23\xfc\xc6\xd1\x2e\xb4\xf1\xc0\x6b\x33' +
                              b'\x0d\xda\xa1\xea\x50\x44\x07\xaf\xa2\x9d\xe9' +
                              b'\xeb\xe0\x37\x4f\xe9\xd1\xe7\xd0\xff\xbd\x5f' +
                              b'\xc1\xcf\x3a\x34\x46\xe4\x14\x54\x15\xd2\xab' +
                              b'\x24\xf7\x89\xb3\x46\x4c\x5c\x43\xa2\x56\xbb' +
                              b'\xc1\xd6\x92\xcf\x7f\x04\x80\x1d\xac\x5b\xb4' +
                              b'\x01\xa4\xa0\x3a\xb7\xd5\x72\x8a\x86\x0c\x19' +
                              b'\xe1\xa4\xdc\x79\x7c\xa5\x42\xc8\x20\x3c\xec' +
                              b'\x2e\x60\x1e\xb0\xc5\x1f\x56\x7f\x2e\xda\x02' +
                              b'\x2b\x0b\x9e\xbd\xde\xee\xfa')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(self.message, 'sha256')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha256', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha384(self):
        intendedS = bytearray(b'\xb2\x81\xad\x93\x4b\x27\x75\xc0\xcb\xa5\xfb' +
                              b'\x10\xaa\x57\x4d\x2e\xd8\x5c\x7f\x99\xb9\x42' +
                              b'\xb7\x8e\x49\x70\x24\x80\x06\x93\x62\xed\x39' +
                              b'\x4b\xad\xed\x55\xe5\x6c\xfc\xbe\x7b\x0b\x8d' +
                              b'\x22\x17\xa0\x5a\x60\xe1\xac\xd7\x25\xcb\x09' +
                              b'\x06\x0d\xfa\xc5\x85\xbc\x21\x32\xb9\x9b\x41' +
                              b'\xcd\xbd\x53\x0c\x69\xd1\x7c\xdb\xc8\x4b\xc6' +
                              b'\xb9\x83\x0f\xc7\xdc\x8e\x1b\x24\x12\xcf\xe0' +
                              b'\x6d\xcf\x8c\x1a\x0c\xc3\x45\x3f\x93\xf2\x5e' +
                              b'\xbf\x10\xcb\x0c\x90\x33\x4f\xac\x57\x3f\x44' +
                              b'\x91\x38\x61\x6e\x1a\x19\x4c\x67\xf4\x4e\xfa' +
                              b'\xc3\x4c\xc0\x7a\x52\x62\x67')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(self.message, 'sha384')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha384', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha512(self):
        intendedS = bytearray(b'\x8f\xfc\x38\xf9\xb8\x20\xef\x6b\x08\x0f\xd2' +
                              b'\xec\x7d\xe5\x62\x6c\x65\x8d\x79\x05\x6f\x3e' +
                              b'\xdf\x61\x0a\x29\x5b\x7b\x05\x46\xf7\x3e\x01' +
                              b'\xff\xdf\x4d\x00\x70\xeb\xf7\x9c\x33\xfd\x86' +
                              b'\xc2\xd6\x08\xbe\x94\x38\xb3\xd4\x20\xd0\x95' +
                              b'\x35\xb9\x7c\xd3\xd8\x46\xec\xaf\x8f\x65\x51' +
                              b'\xcd\xf9\x31\x97\xe9\xf8\xfb\x04\x80\x44\x47' +
                              b'\x3a\xb4\x1a\x80\x1e\x9f\x7f\xc9\x83\xc6\x2b' +
                              b'\x32\x43\x61\xda\xde\x9f\x71\xa6\x59\x52\xbd' +
                              b'\x35\xc5\x9f\xaa\xa4\xd6\xff\x46\x2f\x68\xa6' +
                              b'\xc4\xec\x0b\x42\x8a\xa4\x73\x36\xf2\x17\x8a' +
                              b'\xeb\x27\x61\x36\x56\x3b\x7d')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(self.message, 'sha512')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha512', 10)
            self.assertEqual(signed, intendedS)

    def test_RSASSA_PSS_verify_sha1(self):
        signed = bytearray(b'\x96\xc3\xf6\x92\x70\x1d\x14\xeb\xbe\xf9' +
                              b'\x22\xa5\xc2\x25\x7f\x71\x3d\x20\xa9\x2c' +
                              b'\x69\x38\x74\xe0\x35\xb5\xb0\x65\x15\x92' +
                              b'\xab\x1b\x96\x43\xd3\x81\xd6\xb4\xa9\x70' +
                              b'\xda\xd7\xe2\x38\x00\xe4\x9d\x1a\x66\x57' +
                              b'\xc3\x33\x35\x8e\x9b\xfa\x5c\x71\x34\x93' +
                              b'\x53\x3b\x90\xb0\x23\x4a\x0d\x0d\xcf\x42' +
                              b'\xd0\xa6\x6b\x48\x03\xe4\xdb\x78\x06\x19' +
                              b'\xcc\xab\x6b\xa5\xbb\x27\xd0\x43\xf3\x2d' +
                              b'\x8e\x60\x1e\x2f\x12\xee\x08\xae\xce\x5c' +
                              b'\x47\xcc\x2e\x02\x89\xcd\xbf\x25\xc9\x77' +
                              b'\xcf\x1b\xea\xdc\x04\x74\x21\x50\xbe\xea' +
                              b'\xd6\x96\x2d\xdd\xa9\xe9\x1e\x17')
        mHash = secureHash(self.message, 'sha1')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha1', 10))

    def test_RSASSA_PSS_verify_shortSign(self):
        with self.assertRaises(InvalidSignature):
            signed = bytearray(b'\x96\xc3\xf6\x92\x70\x1d\x14\xeb\xbe\xf9' +
                               b'\x22\xa5\xc2\x25\x7f\x71\x3d\x20\xa9\x2c' +
                               b'\x69\x38\x74\xe0\x35\xb5\xb0\x65\x15\x92' +
                               b'\xab\x1b\x96\x43\xd3\x81\xd6\xb4\xa9\x70')

            self.assertTrue(self.rsa.RSASSA_PSS_verify(self.message, signed,
                                                   'sha1', 10))

    def test_RSASSA_PSS_verify_sha224(self):
        signed = bytearray(b'\x47\xbd\x25\xf8\x19\xbe\x0f\x7e\xe8\x48\xa3' +
                              b'\x3c\x19\x54\xb5\xbb\xc5\xb0\x0f\xf1\x04\xa2' +
                              b'\xab\x98\xf4\x8c\x38\xe0\x17\x6a\x74\xd7\x07' +
                              b'\xb4\x4c\x36\xdf\x8d\x8c\x12\xda\x49\xec\xec' +
                              b'\x7b\xdc\xc3\x51\x45\x39\xdb\x2b\xd8\xe0\x64' +
                              b'\xca\x62\x89\xaf\xd0\x72\xfd\x86\xc9\xf4\x2e' +
                              b'\x56\x58\xb4\x35\x5b\x34\x19\x30\x4e\x0a\xe9' +
                              b'\x28\x57\x12\x8a\x3c\x5e\xbc\x9b\xa6\x01\x38' +
                              b'\xaf\x67\x44\xec\xf7\x52\x1a\xa1\x11\x94\xac' +
                              b'\x95\x20\x6c\xf7\xa8\x0b\xe9\xca\x5f\x4e\x58' +
                              b'\x49\xae\x67\xf0\x73\xdb\x7b\x69\x2f\xd9\x39' +
                              b'\xcb\x31\xed\x6b\xf5\xe0\x66')
        mHash = secureHash(self.message, 'sha224')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha224', 10))

    def test_RSASSA_PSS_verify_sha256(self):
        signed = bytearray(b'\x11\xe1\x69\xf2\xfd\x40\xb0\x76\x41\xb9\x76' +
                              b'\x8a\x2a\xb1\x99\x65\xfb\x6c\x27\xf1\x0f\xcf' +
                              b'\x03\x23\xfc\xc6\xd1\x2e\xb4\xf1\xc0\x6b\x33' +
                              b'\x0d\xda\xa1\xea\x50\x44\x07\xaf\xa2\x9d\xe9' +
                              b'\xeb\xe0\x37\x4f\xe9\xd1\xe7\xd0\xff\xbd\x5f' +
                              b'\xc1\xcf\x3a\x34\x46\xe4\x14\x54\x15\xd2\xab' +
                              b'\x24\xf7\x89\xb3\x46\x4c\x5c\x43\xa2\x56\xbb' +
                              b'\xc1\xd6\x92\xcf\x7f\x04\x80\x1d\xac\x5b\xb4' +
                              b'\x01\xa4\xa0\x3a\xb7\xd5\x72\x8a\x86\x0c\x19' +
                              b'\xe1\xa4\xdc\x79\x7c\xa5\x42\xc8\x20\x3c\xec' +
                              b'\x2e\x60\x1e\xb0\xc5\x1f\x56\x7f\x2e\xda\x02' +
                              b'\x2b\x0b\x9e\xbd\xde\xee\xfa')
        mHash = secureHash(self.message, 'sha256')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha256', 10))

    def test_RSASSA_PSS_verify_sha384(self):
        signed = bytearray(b'\xb2\x81\xad\x93\x4b\x27\x75\xc0\xcb\xa5\xfb' +
                              b'\x10\xaa\x57\x4d\x2e\xd8\x5c\x7f\x99\xb9\x42' +
                              b'\xb7\x8e\x49\x70\x24\x80\x06\x93\x62\xed\x39' +
                              b'\x4b\xad\xed\x55\xe5\x6c\xfc\xbe\x7b\x0b\x8d' +
                              b'\x22\x17\xa0\x5a\x60\xe1\xac\xd7\x25\xcb\x09' +
                              b'\x06\x0d\xfa\xc5\x85\xbc\x21\x32\xb9\x9b\x41' +
                              b'\xcd\xbd\x53\x0c\x69\xd1\x7c\xdb\xc8\x4b\xc6' +
                              b'\xb9\x83\x0f\xc7\xdc\x8e\x1b\x24\x12\xcf\xe0' +
                              b'\x6d\xcf\x8c\x1a\x0c\xc3\x45\x3f\x93\xf2\x5e' +
                              b'\xbf\x10\xcb\x0c\x90\x33\x4f\xac\x57\x3f\x44' +
                              b'\x91\x38\x61\x6e\x1a\x19\x4c\x67\xf4\x4e\xfa' +
                              b'\xc3\x4c\xc0\x7a\x52\x62\x67')
        mHash = secureHash(self.message, 'sha384')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha384', 10))

    def test_RSASSA_PSS_verify_sha512(self):
        signed = bytearray(b'\x8f\xfc\x38\xf9\xb8\x20\xef\x6b\x08\x0f\xd2' +
                              b'\xec\x7d\xe5\x62\x6c\x65\x8d\x79\x05\x6f\x3e' +
                              b'\xdf\x61\x0a\x29\x5b\x7b\x05\x46\xf7\x3e\x01' +
                              b'\xff\xdf\x4d\x00\x70\xeb\xf7\x9c\x33\xfd\x86' +
                              b'\xc2\xd6\x08\xbe\x94\x38\xb3\xd4\x20\xd0\x95' +
                              b'\x35\xb9\x7c\xd3\xd8\x46\xec\xaf\x8f\x65\x51' +
                              b'\xcd\xf9\x31\x97\xe9\xf8\xfb\x04\x80\x44\x47' +
                              b'\x3a\xb4\x1a\x80\x1e\x9f\x7f\xc9\x83\xc6\x2b' +
                              b'\x32\x43\x61\xda\xde\x9f\x71\xa6\x59\x52\xbd' +
                              b'\x35\xc5\x9f\xaa\xa4\xd6\xff\x46\x2f\x68\xa6' +
                              b'\xc4\xec\x0b\x42\x8a\xa4\x73\x36\xf2\x17\x8a' +
                              b'\xeb\x27\x61\x36\x56\x3b\x7d')
        mHash = secureHash(self.message, 'sha512')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha512', 10))

    def test_RSASSA_PSS_verify_noSalt(self):
        signed = bytearray(b'\xafe\x03\xb5\xaf5\x0b\t\xd1?9\x89\xee\x0eP\xcc' +
                           b'\x82\xef%\xc2t<\xa2\xff\xd6\x13[\x97\xbd\xac' +
                           b'\xda\x97;\xcb!\xfa"\x10\t\xb7\x81\xb9\x8f\x9a' +
                           b'\x1a\xc87\xa3,\xb4\xea\xddG7\xe8RI\xf9\x91m\x8e' +
                           b'\x91\xe3\xf8Y\xdd \x92\xd7I\xcc`czm\x01~\x85' +
                           b'\xf6\xa6\xd6_PF3\xc9\xb5\x192\xf4U\\|\xcc' +
                           b'\xcd6|7d\xca,\x8dIF\x02\xf8\xcd\x81\xdd\x88' +
                           b'\xb0\xae\xe9\x1f\x93\xf3\xfa\x90\x0f\xcd' +
                           b'\xe2|\xbc<R\xf7\xa3\x8a')
        mHash = secureHash(self.message, 'sha512')
        self.assertTrue(self.rsa.RSASSA_PSS_verify(mHash, signed,
                                                   'sha512', 0))

    def test_RSASSA_PSS_verify_wrongSign(self):
        signed = bytearray(b'\x96\xc3\xf6\x92\x70\x1d\x14\xeb\xbe\xf9' +
                           b'\x22\xa5\xc2\x25\x7f\x71\x3d\x20\xa9\x2c' +
                           b'\x69\x38\x74\xe0\x35\xb5\xb0\x65\x15\x92' +
                           b'\xab\x1b\x96\x43\xd3\x81\xd6\xb4\xa9\x70' +
                           b'\xda\xd7\xe2\x38\x00\xe4\x9d\x1a\x66\x57' +
                           b'\xc3\x33\x35\x8e\x8b\xfa\x5c\x71\x34\x93' +
                           b'\x53\x3b\x90\xb0\x23\x4a\x0d\x0d\xcf\x42' +
                           b'\xd0\xa6\x6b\x48\x03\xe4\xdb\x78\x06\x19' +
                           b'\xcc\xab\x6b\xa5\xbb\x27\xd0\x43\xf3\x2d' +
                           b'\x8e\x60\x1e\x2f\x12\xee\x08\xae\xce\x5c' +
                           b'\x47\xcc\x2e\x02\x89\xcd\xbf\x25\xc9\x77' +
                           b'\xcf\x1b\xea\xdc\x04\x74\x21\x50\xbe\xea' +
                           b'\xd6\x96\x2d\xdd\xa9\xe9\x1e\x10')
        with self.assertRaises(InvalidSignature):
            self.rsa.RSASSA_PSS_verify(self.message, signed,
                                                        'sha1', 10)

    def test_RSASSA_PSS_verify_wrongSign2(self):
        def m(x, M, EM, numBits, hAlg, sLen):
            return False
        signed = bytearray(b'\x96\xc3\xf6\x92\x70\x1d\x14\xeb\xbe\xf9' +
                           b'\x22\xa5\xc2\x25\x7f\x71\x3d\x20\xa9\x2c' +
                           b'\x69\x38\x74\xe0\x35\xb5\xb0\x65\x15\x92' +
                           b'\xab\x1b\x96\x43\xd3\x81\xd6\xb4\xa9\x70' +
                           b'\xda\xd7\xe2\x38\x00\xe4\x9d\x1a\x66\x57' +
                           b'\xc3\x33\x35\x8e\x8b\xfa\x5c\x71\x34\x93' +
                           b'\x53\x3b\x90\xb0\x23\x4a\x0d\x0d\xcf\x42' +
                           b'\xd0\xa6\x6b\x48\x03\xe4\xdb\x78\x06\x19' +
                           b'\xcc\xab\x6b\xa5\xbb\x27\xd0\x43\xf3\x2d' +
                           b'\x8e\x60\x1e\x2f\x12\xee\x08\xae\xce\x5c' +
                           b'\x47\xcc\x2e\x02\x89\xcd\xbf\x25\xc9\x77' +
                           b'\xcf\x1b\xea\xdc\x04\x74\x21\x50\xbe\xea' +
                           b'\xd6\x96\x2d\xdd\xa9\xe9\x1e\x10')
        with mock.patch('tlslite.utils.rsakey.RSAKey.EMSA_PSS_verify', m):
            with self.assertRaises(InvalidSignature):
                self.rsa.RSASSA_PSS_verify(self.message, signed,
                                           'sha1', 10)

class TestRSAPSS_mod2048(unittest.TestCase):
    # Test cases from http://csrc.nist.gov/groups/STM/cavp/
    # file SigVerPSS_186-3.rsp

    n = int("c6e0ed537a2d85cf1c4effad6419884d824ceabf5200e755691cb7328acd6a755"
            "fe85798502ccaec9e55d47afd0cf3258ebe920b50c5fd9d72897462bd0e459bbd"
            "f902b63d17195b2ef54908980be12aa7489f8af274b92c0cbc16aed2fa46f782d"
            "5517b666edfb2e5e5efeaff7e24965e26472e51980b0cfe457d297e6aa5dacb8e"
            "728dc6f58130f925a13275c3cace62f820db1e13cc5274c58ff4d7837671a1bf5"
            "f80d6ad8699c568df8d24dd0f152ded36ef4861f59b354bba96a076913a25facf"
            "4722737e6deed95b69a00fb2bced0feeedea4ff01a92605cfe26a6b39553d0c74"
            "e5650eb3779705e135c4b2fa518a8d4339c53efab4bb0058238def555",
            16)
    e = int("00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "000000000000000000000000000000000000000000000000000010001",
            16)
    d = int("03ac73787e325992a96749d5ef8500e2ccf99e96214dbc22df2c6fde3538aaa85"
            "78e1b3cc871af5f940ed4a6df46438bdf240f896478fd2090fffa2af9c034a7cb"
            "684e5fc491f3940987c537d80128d6b37230ba4314c60d3580ad9aeb46ed6929d"
            "cf1629f6784667c547fec48c3112a1d9144f1802c82bb1476544e757e98538191"
            "85949352b92411adabd0f76efafe72c3b3fce88c5895b0bc4ac1ad36ec8d5be4a"
            "db89e72519850c6fc8c4076b658a2e554a37b5aa76aef7293a1ec256ccdc0c93c"
            "60aa528596a44ad72c76ed55726206d4bfd2f431745cc1c7dc399213051275fcf"
            "d2757552cef855be7bf23a5480688032bb4f322669a3e7d2fbff31c91",
            16)
    p = int("e2f7ceb13ea5385ad7659d7bbf0ad4a517c697b70c9d2af7a2193d62b14014412"
            "cc3e5fda97882341e0a370ce9f0f6c8149bb199d6f408b65d0524aecaf6e3fd7e"
            "3c35de940dc661ae17ddbdf57184e75bd2e9642401045ba48c7aee4abdc1caddc"
            "a85fd064e80ab82ce58537848d9e9b8a477b4dfd04b9be496baec79cfa4c5",
            16)
    q = int("e0515147b6e596b7e5140e81365ad698dbeddd874642510f42d357123c20ffb0e"
            "1f377afefe97f20442e1c3f3c88919c39978b78835b9c7253f6ea632ab3298667"
            "48c6dc195865ce123c8e153d03a3d731b7161205e2d83e6651152ee8181e389ad"
            "7a795dd3ce6ba44c753b4c7774fafbfa9c6606f89c08eec37632ba607b751",
            16)
    dP = d % (p - 1)
    dQ = d % (q - 1)
    qInv = invMod(q, p)
    salt = bytearray(b'\x11\x22\x33\x44\x55\x54\x32\x16\x78\x90')

    def setUp(self):
        self.rsa = Python_RSAKey(self.n, self.e, self.d, self.p, self.q,
                                 self.dP, self.dQ, self.qInv)

    def test_RSAPSS_sha1_wrongSignature(self):
        message = bytearray(b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x4f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7')
        intendedS = bytearray(b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                              b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                              b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                              b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                              b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                              b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                              b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                              b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                              b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                              b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                              b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                              b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                              b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                              b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                              b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                              b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                              b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                              b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                              b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                              b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                              b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                              b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                              b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                              b'\x72\xa9\x1f')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            signed = self.rsa.RSASSA_PSS_sign(message, 'sha1', 10)
            self.assertNotEqual(signed, intendedS)

    def test_RSAPSS_sha1_messageTooLong(self):
        message = bytearray(b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                            b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                            b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                            b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                            b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                            b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                            b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                            b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                            b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                            b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                            b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                            b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                            b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                            b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                            b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                            b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                            b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                            b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                            b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                            b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                            b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                            b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                            b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                            b'\x72\xa9\x1f' +
                            b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x4f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7' +
                            b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                            b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                            b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                            b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                            b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                            b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                            b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                            b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                            b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                            b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                            b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                            b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                            b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                            b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                            b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                            b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                            b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                            b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                            b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                            b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                            b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                            b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                            b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                            b'\x72\xa9\x1f' +
                            b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x4f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7' +
                            b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                            b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                            b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                            b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                            b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                            b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                            b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                            b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                            b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                            b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                            b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                            b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                            b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                            b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                            b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                            b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                            b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                            b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                            b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                            b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                            b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                            b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                            b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                            b'\x72\xa9\x1f' +
                            b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x4f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7' +
                            b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                            b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                            b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                            b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                            b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                            b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                            b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                            b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                            b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                            b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                            b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                            b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                            b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                            b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                            b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                            b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                            b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                            b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                            b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                            b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                            b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                            b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                            b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                            b'\x72\xa9\x1f' +
                            b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x4f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7')

        def m(x,M, emBits, hAlg, sLen):
            return bytearray(b"4c\xa3n\xae\xc9\x15\x84\'\xc3&\xd4*A\xb2\x04r" +
                             b"\x930\xc2\x972(cQ\xc9\xea\xcf\x94?#\x9b\xfer" +
                             b"\xff\xfe]C\x8d\xd5\x9b\xab\xe2oM`\xdc\x92!" +
                             b"\x00\x8fSp\xcf\x8b\x9c\x12s\xabH\xd6\xe4=\xac" +
                             b"\xd5\x12\xc8^\x0f\x95\xc4\xe7\xb0\x91\xa3\x1e" +
                             b"\xffb\xc0V{z\xbd\xc0P\xb7\xbd\x80gQXIh\x15:" +
                             b"\x7f\xca\xf7}\xf8\xaf\xdc\xb9d\x19\xe4\x02" +
                             b"\xc5d\xcaJ\x81\xd9`\x0fL)~Q\xfd\x08i\xc39\x03" +
                             b"\xda\xc6\xcf\xa3\xf9\x81\x8d&\xed\xaeQ\xc3" +
                             b"\xf5\x0e\x07\x8a\x8c\x14\xf9V\xbc\xf0\x13\xa3" +
                             b"\xdcw\x97\x81\xa7ym\xb3\xbd\xa3\xc0\n\x1a\xc3"
                             b"\x94\xd0\xaa\x8a\xbfV\xa6i\xa1\x86L#\xb1O\x12"+
                             b"\xce\x0b\x90\xaaU\xa1\xe8&5\x8b\xd5\xd0Ek(" +
                             b"\x10Az\x95\xc7\xc8\xe8\x1f\x05\xc7\xb7\xc3q" +
                             b"\x8f\xe5\x0cT\x05\x1a\x0f\x05\x8cCq\x1c\xbdSV" +
                             b"\x14n\x85M\x99\xdf\xff\x86\xd5\x98\xdf\x1ef" +
                             b"\xde\x1f\x07r\xa7\xd2\xfe\x16\x8e6\xcd\xfd" +
                             b"\t%\xa4\x87\'\xc61V\x0c\xbc\ff\ff\ff\ff\ff")

        with mock.patch('tlslite.utils.rsakey.RSAKey.EMSA_PSS_encode', m):
            with self.assertRaises(MessageTooLongError):
                self.rsa.RSASSA_PSS_sign(message, 'sha224', 10)

    def test_RSAPSS_sha1_noSalt(self):
        message = bytearray(b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x5f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7')
        intendedS = bytearray(b'6\xbb\x70\x06\x53\x58\x78\xca\x42\x76\x2a' +
                              b'\x55\x43\x72\x8a\xb0\xf6\x85\x70\xfa\xbc\xd4' +
                              b'\xb4\xba\xa4\x67\x0e\x5b\xdf\xfb\x41\xfa\x31' +
                              b'\x64\xeb\xac\x95\x2f\xc8\x79\xad\x58\x73\x60' +
                              b'\xac\x38\xd2\x4c\xde\xcf\xe4\x04\xfc\xc0\x7b' +
                              b'\xde\x52\x14\x3b\x79\x98\xcf\x80\xb7\x98\xe3' +
                              b'\x38\xc1\xfa\xac\xac\x59\xeb\x65\xec\xa1\xc7' +
                              b'\xa7\xba\x9a\xa5\x35\xa5\xf7\xb4\x89\x4f\x91' +
                              b'\x85\xab\x2e\x4d\xbd\x39\x56\x7a\xaa\x4b\xb9' +
                              b'\x72\xa2\x44\xa4\xa5\x55\x37\xfd\x16\x8c\x4a' +
                              b'\xa4\x91\x3d\xa5\xb2\x45\xd3\x64\x77\xdc\x5e' +
                              b'\x02\xa6\x8c\x32\xef\x54\x18\xb5\x3a\xe5\xff' +
                              b'\x9e\xcc\x6c\x6c\x39\x36\x40\x9a\x1a\x20\xe5' +
                              b'\x86\x39\x1e\x1e\xad\xd1\xff\x25\x1f\x48\x97' +
                              b'\xd3\x38\xf6\x6e\x9a\xe6\x15\x48\xc2\x83\x4c' +
                              b'\x82\xa9\x98\x35\x29\x19\xef\xaa\x22\x26\xcc' +
                              b'\x8b\xbe\x6d\x64\xfe\xa8\x4f\xd3\xe0\x43\xf8' +
                              b'\xf7\xd2\xe0\xcf\x65\x5e\x14\x96\xbf\x1a\x2d' +
                              b'\x3e\xf5\x1f\xf7\xd3\x54\x92\xf1\x4f\xd2\x44' +
                              b'\xd2\xb8\x4c\xfc\xa8\x15\x93\xaf\x85\x92\x8f' +
                              b'\x47\x28\x2c\x0f\x48\xce\x84\xaf\x1d\xb4\x54' +
                              b'\x3f\xc1\x6d\x6e\x86\xf3\xb5\x5a\xac\x95\x08' +
                              b'\x8f\x0d\x74\xbc\xe6\xfc\x4b\x83\xdd\x4c\xae' +
                              b'\xa5\xdd\xea')
        mHash = secureHash(message, 'sha1')
        signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha1')
        self.assertEqual(signed, intendedS)

    def test_RSAPSS_sha1(self):
        message = bytearray(b'\x13\x0f\x45\x53\x89\x78\xe3\x2f\x14\xb9\xb9' +
                            b'\x1f\x2c\xf9\xa3\xa1\x28\xc2\x56\xa6\x03\xb2' +
                            b'\x43\xe8\x5f\x73\xbe\x7e\xca\xed\x5f\xad\x41' +
                            b'\xb9\xa8\x02\xf2\xd9\xe9\x9d\x46\xa7\x61\xd0' +
                            b'\x1f\x0c\xa6\xe9\x5f\xf2\x47\x4b\xa9\xfc\xaf' +
                            b'\xc4\x6b\x74\x4c\x1a\x1c\x85\xf1\xe7\xc2\xaa' +
                            b'\x79\xa7\xb8\x66\xae\x10\xae\x36\x69\xa2\xf1' +
                            b'\xc4\xfa\x7e\xed\x5d\xc9\x7b\xf0\xa5\x3e\x77' +
                            b'\x30\x89\xdf\xeb\x10\x76\xb8\xc2\x9f\xc8\x00' +
                            b'\x6c\x61\x86\xf9\x2e\x53\x4c\x18\xbc\x29\x88' +
                            b'\x66\x09\xda\xe9\x26\x5e\x5e\x15\xb8\xaa\xb6' +
                            b'\x9b\xbd\x19\x2e\x28\x7c\xe7')
        intendedS = bytearray(b'\xc2\xc8\xb9\xd9\x32\x95\x1b\xe1\x80\xeb\x87' +
                              b'\x34\x69\xb8\x6f\x71\x17\x92\xe0\x19\x3b\x03' +
                              b'\xbf\xc3\x61\x83\x76\x61\x20\x52\x5c\xfe\xb8' +
                              b'\x03\x5c\x99\x01\xd0\x09\xd9\x7d\xea\x81\xed' +
                              b'\x0a\x43\x7d\x85\x5b\x8f\x73\x55\xec\xd1\xd7' +
                              b'\x16\x20\xdb\x91\x8b\x5d\xbc\x14\x1a\x77\xed' +
                              b'\x24\x0f\x73\x9a\x98\x98\x7a\xf8\x6f\x1f\x88' +
                              b'\x20\x6f\x96\x77\x55\x26\xe6\xa9\x79\x51\x0d' +
                              b'\x4d\xf9\x1c\xf2\xa8\x90\xf9\x08\x6f\x06\x84' +
                              b'\x2e\xe2\x8b\x95\xb1\xc5\x94\xed\xe7\xd0\xc9' +
                              b'\xe8\x59\x5d\x53\x11\xc7\x0f\x00\x3b\xd3\x2c' +
                              b'\x86\x56\x09\x3a\x23\x14\xb5\x73\x54\x75\xae' +
                              b'\xe1\x21\xd4\x84\x6e\xd4\xaa\x52\xb2\x46\xb3' +
                              b'\x37\xd4\x88\x36\x9a\xa3\x91\xb0\x51\x70\xbf' +
                              b'\x73\x15\xf6\xf1\xbc\x2a\x7b\x9b\x0f\x4f\x1c' +
                              b'\xf1\xab\x5d\xe1\x71\xe0\xdf\xb4\xe0\x10\x35' +
                              b'\xb4\x3e\xbd\xa0\xef\x13\xd3\xc8\x6b\x26\xbf' +
                              b'\xf4\xf3\x50\x9b\xe6\x83\xf5\x75\xbe\xcf\x17' +
                              b'\x46\x84\xfb\xfb\xee\x98\xe8\x69\xbb\xad\xca' +
                              b'\x8a\xbd\x02\xde\xfd\xf9\x3a\x68\xf4\x50\xba' +
                              b'\xa7\x5e\x6f\x81\xc0\xaa\x17\xaf\x59\x12\xdb' +
                              b'\x12\xa2\x4d\xf8\xf7\x2f\x63\xc2\x2d\x17\x14' +
                              b'\x13\x6e\x47\x4d\x9d\xb6\xf8\xa9\xf0\xb2\x6d' +
                              b'\x72\xa9\x1f')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(message, 'sha1')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha1', 10)
            self.assertEqual(signed, intendedS)

    def test_RSAPSS_sha224(self):
        message = bytearray(b'\x40\x12\x6e\xcf\x7f\x69\x69\x1e\x10\x74\x4e' +
                            b'\xa0\x3a\x2d\xbc\xc6\xb0\x4b\x21\x9d\x66\xc4' +
                            b'\x2a\x65\xa2\x91\x7e\x7e\x56\xb1\xab\x8c\xad' +
                            b'\x70\x60\xd3\xe4\xe9\xde\xe3\x5b\xca\xa9\x7a' +
                            b'\xec\x57\x83\xa6\x7b\xb2\x9a\x2a\xce\x59\x01' +
                            b'\x23\x9f\xf0\x5d\xeb\xf0\x41\xe1\x3e\x9f\x81' +
                            b'\x7c\x9b\x3a\xd4\x50\xed\x14\x14\x67\x6b\x99' +
                            b'\xce\xa1\xbd\xde\x8e\xf1\x60\x7d\x5d\xc9\x4b' +
                            b'\x9f\x87\xd3\xd3\x5a\xa2\xe2\xcc\x3e\xcb\x28' +
                            b'\xf1\x2a\x33\xa9\x86\x64\xdb\xef\x3b\xe9\x9b' +
                            b'\x00\x54\x02\x69\x8d\x07\x18\xd8\x6c\x25\xc9' +
                            b'\xdf\x49\xfd\x3c\xdc\x98\x7e')
        intendedS = bytearray(b'\x32\xda\x2a\xd3\x9b\x0d\xc4\xd5\x66\xfe\x7d' +
                              b'\xc7\xe3\x5d\xb8\xd7\x62\x11\x6d\x6c\x83\x4b' +
                              b'\xaf\xe6\x77\xd2\x08\x62\x0d\x86\xa1\x57\x7d' +
                              b'\x52\x45\x2b\x7a\x6f\x4c\xd5\x75\x59\xfa\x04' +
                              b'\x97\x36\x5f\x6b\xb7\x4f\x11\x2d\xbf\x34\x25' +
                              b'\x19\xc2\x45\xd0\x5a\x6a\x69\xaf\xfd\xbb\xad' +
                              b'\x71\x65\x66\xf0\x62\xac\xd6\x53\x9d\xe3\x49' +
                              b'\xe9\x50\x6c\x2a\xf9\xc4\x26\x84\x66\x5b\x11' +
                              b'\xe5\x3f\x46\x2a\xa1\xa2\x8a\x09\x2e\x68\x01' +
                              b'\x32\x38\x6c\x00\xf8\x3f\xc2\x9b\x9c\xc0\xa8' +
                              b'\xf0\x38\x26\x9c\x88\xba\x02\x56\x23\x8a\xee' +
                              b'\xde\x11\x72\xd7\xbd\x6d\xff\xef\x80\x47\x34' +
                              b'\x57\x38\x17\xf0\x6f\xb7\x6e\x6f\xe0\x16\xe3' +
                              b'\x5b\x19\x6b\xa9\x6b\xc3\x99\xe1\x19\xf3\x29' +
                              b'\xc0\xd7\x34\x69\x3b\xac\x2a\xb6\xcb\x8e\xda' +
                              b'\x9e\xa3\xe9\x1a\x77\x98\xb8\x29\x64\xbc\xe2' +
                              b'\xbe\xd6\xf2\xe4\x6a\x23\x1c\x50\x01\xc9\x68' +
                              b'\x2d\x40\x3c\xc5\x29\x51\x72\xc9\x25\xd8\xbb' +
                              b'\xbf\xbc\xe6\xd1\x0d\xfa\x2d\x67\x17\xe0\x11' +
                              b'\x18\x5c\x24\x52\x60\x1d\xf8\x2c\x27\x00\x44' +
                              b'\x09\x17\xd5\x28\x43\xd3\x39\x12\x63\x07\xc9' +
                              b'\xca\xb2\x64\x47\x30\xf1\x41\x93\x33\xf2\xd7' +
                              b'\xfa\x7e\x33\x60\xf0\x30\xfd\x95\x41\x39\x1b' +
                              b'\xc3\x7a\x31')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(message, 'sha224')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha224', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha256(self):
        message = bytearray(b'\x81\xea\xf4\x73\xd4\x08\x96\xdb\xf4\xde\xac' +
                            b'\x0f\x35\xc6\x3b\xd1\xe1\x29\x14\x7c\x76\xe7' +
                            b'\xaa\x8d\x0e\xf9\x21\x63\x1f\x55\xa7\x43\x64' +
                            b'\x11\x07\x9f\x1b\xcc\x7b\x98\x71\x4a\xc2\xc1' +
                            b'\x3b\x5e\x73\x26\xe6\x0d\x91\x8d\xb1\xf0\x5f' +
                            b'\xfb\x19\xda\x76\x7a\x95\xbb\x14\x1a\x84\xc4' +
                            b'\xb7\x36\x64\xcc\xeb\xf8\x44\xf3\x60\x1f\x7c' +
                            b'\x85\x3f\x00\x9b\x21\xbe\xcb\xa1\x1a\xf3\x10' +
                            b'\x6f\x1d\xe5\x82\x7b\x14\xe9\xfa\xc8\x4b\x2c' +
                            b'\xbf\x16\xd1\x8c\x04\x56\x22\xac\xb2\x60\x02' +
                            b'\x47\x68\xe8\xac\xc4\xc0\xae\x2c\x0b\xd5\xf6' +
                            b'\x0a\x98\x02\x38\x28\xcd\xec')
        intendedS = bytearray(b'\x40\xd5\x9e\xbc\x6c\xb7\xb9\x60\xcb\xda\x0d' +
                              b'\xb3\x53\xf9\xb8\x5d\x77\xe7\xc0\x3f\x84\x44' +
                              b'\x7f\xb8\xe9\x1b\x96\xa5\xa7\x37\x7a\xbc\x32' +
                              b'\x9d\x1f\x55\xc8\x5e\x0d\xbe\xdb\xc2\x88\x6c' +
                              b'\xe1\x91\xd9\xe2\xcf\x3b\xe0\x5b\x33\xd6\xbb' +
                              b'\xd2\xba\x92\xb8\x5e\xee\x2f\xf8\x9c\xd6\xee' +
                              b'\x29\xcd\x53\x1e\x42\x01\x6e\x6a\xba\x1d\x62' +
                              b'\x0f\xe5\x5e\x44\x48\x0c\x03\x3e\x8a\x59\xc0' +
                              b'\x85\x2d\xd1\xca\xff\xbc\x2c\xe8\x29\x69\xe3' +
                              b'\xa9\xf4\x4c\xef\xf7\x9f\x89\x99\x3b\x9e\xbf' +
                              b'\x37\x41\xb2\xcc\xab\x0b\x95\x16\xf2\xe1\x28' +
                              b'\x65\x6a\x5b\x2a\xd5\x25\x1e\x20\xc6\xce\x0c' +
                              b'\x26\xa1\x4e\xef\x7e\xe8\x64\x58\x94\x2d\xdb' +
                              b'\xe9\x5c\xcc\x1f\x67\xb2\x53\xe4\x3e\x72\x11' +
                              b'\x7f\x49\x59\x5d\xab\x5b\xa4\x23\x49\x6e\xce' +
                              b'\x12\x82\x54\x35\x66\x11\x12\x66\x6d\xba\xe7' +
                              b'\x1a\xaf\xfd\x5a\x8f\x1d\x58\xdb\x9d\xc0\x2e' +
                              b'\x0d\x70\xfe\x3a\xc3\x6a\x87\xb8\xee\xed\x4f' +
                              b'\x20\xc0\x0f\xd4\x30\x3f\x9f\x76\x7d\x03\xbc' +
                              b'\xa1\xa6\x19\xbb\xe4\xb0\x8e\x4e\x53\xb5\xcb' +
                              b'\x69\xd2\xba\x02\x35\x06\x3e\x04\xca\x39\x23' +
                              b'\x34\xd9\x97\x9a\x41\xc4\x2a\x66\xca\x8b\x97' +
                              b'\x21\xed\xcf\x76\x98\x9b\xa8\x9f\x3a\x17\x0b' +
                              b'\xb2\xe4\x85')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(message, 'sha256')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha256', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha384(self):
        message = bytearray(b'\x32\xa7\xb1\x47\x9a\xcf\x50\x5d\xb7\x93\xf3' +
                              b'\xeb\xed\x95\x3f\x4e\x31\xc9\xec\xad\x1a\x34' +
                              b'\x79\xdf\x3a\xf3\x1e\x89\xae\x7e\x03\x87\xf4' +
                              b'\x2e\xaf\x8e\xfd\xfd\xc3\x0f\x83\x8e\xe8\x5e' +
                              b'\x9d\x6d\x06\x13\x91\x97\xb7\xb1\xe9\x3d\xfb' +
                              b'\x85\xc9\xc5\x2d\xd1\x7f\x12\x35\x2a\x5c\x05' +
                              b'\x00\x1f\xc2\x43\x2d\x1b\x7f\x39\x09\x8d\x59' +
                              b'\x5e\xbe\x45\xea\xb8\xc7\x21\xaf\xa2\xa7\xea' +
                              b'\x5b\xcc\xdb\x79\x71\x83\x0d\x1e\x11\x33\x8a' +
                              b'\x42\x12\x2a\xf6\x4a\x52\x9e\x3f\xbf\x4a\xf2' +
                              b'\xcf\xac\xe6\x35\x06\x48\x93\xec\xe7\xd5\x99' +
                              b'\x11\x11\xc8\xab\x5b\xf1\x2a')
        intendedS = bytearray(b'\x0c\xb3\x75\xec\xc3\x4a\x9f\x36\xb8\x8b\xf5' +
                              b'\x6e\xbf\x12\x35\x38\x7f\xfa\xcf\xd3\xdd\x09' +
                              b'\xc4\x8e\x87\x28\x97\xca\xca\x60\xaf\x9e\x38' +
                              b'\x64\x96\xaa\xfd\x0d\x4b\x1f\xd8\xfb\x47\x14' +
                              b'\xfa\xc9\x25\xed\xda\x6f\x34\x63\x3c\x3b\xb0' +
                              b'\x8f\x7c\xca\x3d\x9a\xd8\xb7\x64\x72\xde\x8c' +
                              b'\x9f\x91\xcb\x75\x18\x64\x8d\x36\x8f\xbe\xb3' +
                              b'\x1d\x1a\x7c\xb3\x9a\x40\xa7\xb1\x7e\xe2\xf7' +
                              b'\xba\xce\x9b\xd9\x9b\xa0\x82\x95\xaa\xdd\x85' +
                              b'\x6c\xd6\x90\x2e\xe6\xc9\x6d\x5c\x12\x91\xdc' +
                              b'\x29\x9a\x7f\x35\x28\xa8\x69\xf6\x2f\xb8\xfb' +
                              b'\xd5\x18\x17\xff\xe6\x49\x0e\xd6\xe0\x00\x7d' +
                              b'\x79\x81\xab\x12\xb8\xf4\xce\x0d\x74\x32\xe8' +
                              b'\xc3\x21\x3f\xae\x2b\x81\x00\x6f\x33\x37\x14' +
                              b'\xb5\x13\xeb\xa0\x41\x4c\x16\x1f\xab\x6e\xa2' +
                              b'\x33\x38\x56\x79\x95\xf2\x73\xe3\x26\x9c\x44' +
                              b'\xa5\x87\xad\x83\x5c\x32\x0d\x1e\x5f\xf5\x53' +
                              b'\xdb\x4c\x47\x12\x66\x80\xcd\x58\x29\x32\x31' +
                              b'\x91\x5c\xf7\xae\xfb\x80\x69\x04\x99\x24\x3e' +
                              b'\xda\x83\xf5\x34\x7a\x30\x0e\x07\x05\x68\xba' +
                              b'\xee\x27\x45\xb2\x0c\x68\x68\x8d\xad\x6e\x38' +
                              b'\x07\xaf\xcb\x34\xc7\x2c\xda\xeb\x9a\x57\x10' +
                              b'\x89\xc7\xf8\xc6\x3d\x1b\x6f\xfd\xbe\x2f\xd1' +
                              b'\x33\x30\xe6')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(message, 'sha384')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha384', 10)
            self.assertEqual(signed, intendedS)


    def test_RSAPSS_sha512(self):
        message = bytearray(b'\x35\xa3\x79\x46\xe5\x26\x78\xee\x37\x8f\x5f' +
                            b'\x17\x68\x38\xef\x08\xf3\xc2\x13\x92\xb1\xad' +
                            b'\x20\x46\x45\x25\x5b\xe5\xb7\x1f\xbc\x18\x5f' +
                            b'\xa5\xf1\x61\x05\x6e\xa6\x52\x46\xb2\x04\xfd' +
                            b'\x39\x3c\x77\xab\x53\xc1\xb5\xd1\x88\x70\xfc' +
                            b'\x3f\xb3\xca\x9a\x9b\x38\xb4\xb3\x0e\xe8\xcb' +
                            b'\x3f\x3d\x25\xf7\x52\x7b\x46\x43\xa0\x3c\x3d' +
                            b'\xec\x40\xcd\x76\xb7\xb0\x43\x03\x88\x1a\xb2' +
                            b'\xf7\x31\xd5\x9f\x0f\x88\x2f\xb7\x98\xbc\x6a' +
                            b'\xc1\x8c\xe9\x04\xd1\xff\xe9\x3c\xbe\xb9\x6e' +
                            b'\xd1\xd7\x25\x4d\x0d\xd2\x6a\x1d\x02\x05\xd7' +
                            b'\x01\x14\xd9\x84\xc2\xb7\x7b')
        intendedS = bytearray(b'\x56\x27\x9c\xcd\x2d\x37\xe8\x11\x36\x25\x73' +
                              b'\x2c\xd3\xf3\xb6\x1b\x4e\xf9\x32\x51\x60\xc7' +
                              b'\xf6\xaf\x70\x77\xc2\x50\x49\xd3\x27\x42\x60' +
                              b'\x7a\xe3\xf8\x45\xbd\x66\xcd\x67\x52\x81\x3c' +
                              b'\x26\x06\x7f\xdc\x23\xf0\x80\x08\xcf\x6a\x53' +
                              b'\x11\x24\xe9\xeb\xc9\x26\x4f\x7c\xfd\x6d\x6e' +
                              b'\xef\xf1\x5d\xaf\x97\xda\xd2\x25\x65\xec\x36' +
                              b'\xb6\x91\x25\xe7\xb2\x7f\xc9\x38\x92\xf6\xff' +
                              b'\x42\xce\x8f\x26\x5d\xc2\xcf\x2e\x57\x58\xba' +
                              b'\x0d\x67\x96\x8e\x80\x0e\x73\xfd\x47\x13\x10' +
                              b'\x08\xf5\xad\xc8\x63\x91\x9e\xa0\xcc\x15\x3c' +
                              b'\xf7\xef\xff\x13\x4b\x0b\xcb\xd0\xaf\x55\x05' +
                              b'\xab\x49\xaf\x7b\x75\xd6\x3a\x8a\xa7\x97\x6b' +
                              b'\x8f\xe7\x7b\xaf\x5a\x69\x9a\x7e\x38\xa6\x0e' +
                              b'\xb7\xca\x64\xe8\x34\xf3\xe0\xf8\x9d\xa5\xb6' +
                              b'\xa3\x43\xa0\x1f\x76\x57\xfd\x84\x2c\x09\x1a' +
                              b'\x62\x08\x50\x3b\xc7\x5d\xe8\xf9\x5d\xe0\xd8' +
                              b'\x71\xa6\xfc\x11\x4b\x59\x4f\xf9\x9d\x61\x58' +
                              b'\x25\xfd\x3b\x89\x69\x33\x38\x14\x52\x53\x6d' +
                              b'\x68\xd9\xe0\x34\xf6\x5a\xbf\x34\x12\xe8\xe3' +
                              b'\x20\x02\x68\x9e\x10\x2a\x8b\xb6\x99\x91\xe0' +
                              b'\x4a\x7f\xf6\x81\xb6\x2e\x48\xee\x68\x7b\xad' +
                              b'\xf8\x69\x0b\x2c\xce\xe4\xbf\x24\x5c\xd0\xa2' +
                              b'\x5d\xcf\x21')
        def m(leght):
            return self.salt
        with mock.patch('tlslite.utils.rsakey.getRandomBytes', m):
            mHash = secureHash(message, 'sha512')
            signed = self.rsa.RSASSA_PSS_sign(mHash, 'sha512', 10)
            self.assertEqual(signed, intendedS)


class TestEncryptDecrypt(unittest.TestCase):
    n = int("a8d68acd413c5e195d5ef04e1b4faaf242365cb450196755e92e1215ba59802aa"
            "fbadbf2564dd550956abb54f8b1c917844e5f36195d1088c600e07cada5c080ed"
            "e679f50b3de32cf4026e514542495c54b1903768791aae9e36f082cd38e941ada"
            "89baecada61ab0dd37ad536bcb0a0946271594836e92ab5517301d45176b5",
            16)
    e = int("00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "0000000000000000000000000000000000000000000000000000000000003",
            16)
    p = int("c107a2fe924b76e206cb9bc4af2ab7008547c00846bf6d0680b3eac3ebcbd0c7f"
            "d7a54c2b9899b08f80cde1d3691eaaa2816b1eb11822d6be7beaf4e30977c49",
            16)
    q = int("dfea984ce4307eafc0d140c2bb82861e5dbac4f8567cbc981d70440dd63949207"
            "9031486315e305eb83e591c4a2e96064966f7c894c3ca351925b5ce82d8ef0d",
            16)
    d = int("1c23c1cce034ba598f8fd2b7af37f1d30b090f7362aee68e5187adae49b9955c7"
            "29f24a863b7a38d6e3c748e2972f6d940b7ba89043a2d6c2100256a1cf0f56a8c"
            "d35fc6ee205244876642f6f9c3820a3d9d2c8921df7d82aaadcaf2d7334d39893"
            "1ddbba553190b3a416099f3aa07fd5b26214645a828419e122cfb857ad73b",
            16)

    def setUp(self):
        self.rsa = Python_RSAKey(self.n, self.e, 0, self.p, self.q)

    def test_init(self):
        self.rsa.d == self.d

    def test_encDec(self):
        self.assertEqual(bytearray(b'test'),
                         self.rsa.decrypt(self.rsa.encrypt(bytearray(b'test')))
                         )

    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            Python_RSAKey(self.n, self.e, self.d, self.p)

    def test_with_generated_key(self):
        key = generateRSAKey(1024)

        txt = bytearray(b"test string")
        self.assertEqual(txt, key.decrypt(key.encrypt(txt)))


class TestRSAPKCS1(unittest.TestCase):
    n = int("a8d68acd413c5e195d5ef04e1b4faaf242365cb450196755e92e1215ba59802aa"
            "fbadbf2564dd550956abb54f8b1c917844e5f36195d1088c600e07cada5c080ed"
            "e679f50b3de32cf4026e514542495c54b1903768791aae9e36f082cd38e941ada"
            "89baecada61ab0dd37ad536bcb0a0946271594836e92ab5517301d45176b5",
            16)
    e = int("00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000000000"
            "0000000000000000000000000000000000000000000000000000000000003",
            16)
    p = int("c107a2fe924b76e206cb9bc4af2ab7008547c00846bf6d0680b3eac3ebcbd0c7f"
            "d7a54c2b9899b08f80cde1d3691eaaa2816b1eb11822d6be7beaf4e30977c49",
            16)
    q = int("dfea984ce4307eafc0d140c2bb82861e5dbac4f8567cbc981d70440dd63949207"
            "9031486315e305eb83e591c4a2e96064966f7c894c3ca351925b5ce82d8ef0d",
            16)
    d = int("1c23c1cce034ba598f8fd2b7af37f1d30b090f7362aee68e5187adae49b9955c7"
            "29f24a863b7a38d6e3c748e2972f6d940b7ba89043a2d6c2100256a1cf0f56a8c"
            "d35fc6ee205244876642f6f9c3820a3d9d2c8921df7d82aaadcaf2d7334d39893"
            "1ddbba553190b3a416099f3aa07fd5b26214645a828419e122cfb857ad73b",
            16)
    dP = d % (p - 1)
    dQ = d % (q - 1)
    qInv = invMod(q, p)
    message = bytearray(
            b'\xd7\x38\x29\x49\x7c\xdd\xbe\x41\xb7\x05\xfa\xac\x50\xe7' +
            b'\x89\x9f\xdb\x5a\x38\xbf\x3a\x45\x9e\x53\x63\x57\x02\x9e' +
            b'\x64\xf8\x79\x6b\xa4\x7f\x4f\xe9\x6b\xa5\xa8\xb9\xa4\x39' +
            b'\x67\x46\xe2\x16\x4f\x55\xa2\x53\x68\xdd\xd0\xb9\xa5\x18' +
            b'\x8c\x7a\xc3\xda\x2d\x1f\x74\x22\x86\xc3\xbd\xee\x69\x7f' +
            b'\x9d\x54\x6a\x25\xef\xcf\xe5\x31\x91\xd7\x43\xfc\xc6\xb4' +
            b'\x78\x33\xd9\x93\xd0\x88\x04\xda\xec\xa7\x8f\xb9\x07\x6c' +
            b'\x3c\x01\x7f\x53\xe3\x3a\x90\x30\x5a\xf0\x62\x20\x97\x4d' +
            b'\x46\xbf\x19\xed\x3c\x9b\x84\xed\xba\xe9\x8b\x45\xa8\x77' +
            b'\x12\x58')

    def setUp(self):
        self.rsa = Python_RSAKey(self.n, self.e, self.d, self.p, self.q,
                                 self.dP, self.dQ, self.qInv)

    def test_hashAndSign_RSAPKCS1_sha1(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1", "sha1")
        self.assertEqual(sigBytes, bytearray(
            b'\x17\x50\x15\xbd\xa5\x0a\xbe\x0f\xa7\xd3\x9a\x83\x53\x88' +
            b'\x5c\xa0\x1b\xe3\xa7\xe7\xfc\xc5\x50\x45\x74\x41\x11\x36' +
            b'\x2e\xe1\x91\x44\x73\xa4\x8d\xc5\x37\xd9\x56\x29\x4b\x9e' +
            b'\x20\xa1\xef\x66\x1d\x58\x53\x7a\xcd\xc8\xde\x90\x8f\xa0' +
            b'\x50\x63\x0f\xcc\x27\x2e\x6d\x00\x10\x45\xe6\xfd\xee\xd2' +
            b'\xd1\x05\x31\xc8\x60\x33\x34\xc2\xe8\xdb\x39\xe7\x3e\x6d' +
            b'\x96\x65\xee\x13\x43\xf9\xe4\x19\x83\x02\xd2\x20\x1b\x44' +
            b'\xe8\xe8\xd0\x6b\x3e\xf4\x9c\xee\x61\x97\x58\x21\x63\xa8' +
            b'\x49\x00\x89\xca\x65\x4c\x00\x12\xfc\xe1\xba\x65\x11\x08' +
            b'\x97\x50'))

    def test_hashAndSign_wrongRSaAlgorithm(self):
        with self.assertRaises(UnknownRSAType):
            self.rsa.hashAndSign(self.message,
                                            "PKC1", "sha1")

    def test_hashAndSign_RSAPKCS1_sha1_notSet(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1")
        self.assertEqual(sigBytes, bytearray(
            b'\x17\x50\x15\xbd\xa5\x0a\xbe\x0f\xa7\xd3\x9a\x83\x53\x88' +
            b'\x5c\xa0\x1b\xe3\xa7\xe7\xfc\xc5\x50\x45\x74\x41\x11\x36' +
            b'\x2e\xe1\x91\x44\x73\xa4\x8d\xc5\x37\xd9\x56\x29\x4b\x9e' +
            b'\x20\xa1\xef\x66\x1d\x58\x53\x7a\xcd\xc8\xde\x90\x8f\xa0' +
            b'\x50\x63\x0f\xcc\x27\x2e\x6d\x00\x10\x45\xe6\xfd\xee\xd2' +
            b'\xd1\x05\x31\xc8\x60\x33\x34\xc2\xe8\xdb\x39\xe7\x3e\x6d' +
            b'\x96\x65\xee\x13\x43\xf9\xe4\x19\x83\x02\xd2\x20\x1b\x44' +
            b'\xe8\xe8\xd0\x6b\x3e\xf4\x9c\xee\x61\x97\x58\x21\x63\xa8' +
            b'\x49\x00\x89\xca\x65\x4c\x00\x12\xfc\xe1\xba\x65\x11\x08' +
            b'\x97\x50'))

    def test_hashAndSign_RSAPKCS1_sha224(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1", "sha224")
        self.assertEqual(sigBytes, bytearray(
            b'\x57\x67\x7b\x08\x9e\x20\x54\x86\xdf\x4f\x56\x75\x59\x72' +
            b'\xe3\xaf\x88\xca\xbb\xc2\x3e\xfe\x29\x43\x9b\x8d\x1e\x60' +
            b'\xac\x22\x6e\x99\x0d\xa4\x87\x85\x73\x92\x85\x6d\x12\xcd' +
            b'\xce\xa3\x87\xa2\x69\xd1\xbb\xbc\x12\x85\x49\xa1\x13\x5a' +
            b'\xb0\x62\x20\x1c\xab\x8a\xc0\x88\x86\xa3\x13\xaf\x85\x54' +
            b'\x50\x6d\x7a\x93\x85\x5b\x84\x30\x86\xa1\xbf\x3d\xfb\xcb' +
            b'\x00\x4c\xcd\xe7\x79\xc0\x84\xff\xa1\x72\x4b\x41\xd1\x7e' +
            b'\x10\xc8\xdd\x67\xdc\x0d\xf2\x62\x00\x37\x65\x50\xed\xa1' +
            b'\x44\x55\xd9\xb0\xb3\x1f\x1d\x8c\x5e\x8b\xb1\xd3\xd9\x63' +
            b'\xd0\xd5'))

    def test_hashAndSign_RSAPKCS1_sha256(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1", "sha256")
        self.assertEqual(sigBytes, bytearray(
            b'\x0b\x20\xe5\x09\x3c\x2a\x92\x62\x33\x10\x8a\xfb\xdd\x85' +
            b'\x1b\x88\xee\xb5\x54\xf4\xbe\xaa\x7b\x18\xe5\x15\x19\xf7' +
            b'\xd0\xec\x53\xb1\x81\xa3\xb0\x3e\x84\x84\xba\x8d\xe2\xaa' +
            b'\x78\x64\xa4\x02\xe2\x20\x8e\x84\xec\x99\x14\xaf\x9d\x77' +
            b'\x6e\xd1\x3c\x48\xbd\xeb\x64\x84\x25\x4d\xe1\x69\x31\x8a' +
            b'\x87\xc4\x0f\x22\x65\xff\x16\x71\x4e\xae\x8a\xee\x2b\xc9' +
            b'\xc3\xcb\x4d\xee\x04\x5e\x4f\x5d\x9d\x62\x52\x10\x12\x1b' +
            b'\xfc\xf2\xbe\xd8\xd3\xff\xa6\x02\xce\x27\xff\xf4\xe6\x1c' +
            b'\xf9\xbb\x65\x0e\x71\xa6\x92\x1a\xe6\xff\xa2\x96\xcb\x11' +
            b'\xbd\xbb'))

    def test_hashAndSign_RSAPKCS1_sha384(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1", "sha384")
        self.assertEqual(sigBytes, bytearray(
            b'\x7e\x3c\xcb\x6a\xb0\x3b\x41\x9a\x3e\x54\xf8\x13\x37\xa3' +
            b'\xc3\xf7\x2e\x8c\x65\xbb\xd1\x9d\xdd\x50\x24\x6a\x36\xf5' +
            b'\x1f\x58\x74\x1e\xc2\x45\xd2\xd0\xf0\x76\x77\xa4\xf8\x8a' +
            b'\xa3\xb1\xca\xee\xcd\xff\xe5\xfd\x6e\xdc\xf8\xb8\xbc\xfb' +
            b'\x56\x96\x37\xad\x02\xeb\x15\x4d\x17\xb8\x7a\x8f\x00\xd0' +
            b'\xe6\x18\xa7\xf4\xa7\x0c\xe4\x07\xf2\x03\x59\x15\x3e\x5f' +
            b'\x4a\x4d\x97\x44\xf3\xf3\xff\x44\x12\x0c\x08\xa4\x60\x50' +
            b'\x0f\x03\x0f\xd3\x39\x8e\x97\xfc\xae\xf9\xd0\xa7\xe2\xac' +
            b'\xef\x19\xa8\x1f\x70\x68\x05\xbe\x5f\xc0\x03\xd7\x8e\x5b' +
            b'\x29\xc0'))

    def test_hashAndSign_RSAPKCS1_sha512(self):
        sigBytes = self.rsa.hashAndSign(self.message,
            "PKCS1", "sha512")
        self.assertEqual(sigBytes, bytearray(
            b'\x8b\x57\xa6\xf9\x16\x06\xba\x48\x13\xb8\x35\x36\x58\x1e' +
            b'\xb1\x5d\x72\x87\x5d\xcb\xb0\xa5\x14\xb4\xc0\x3b\x6d\xf8' +
            b'\xf2\x02\xfa\x85\x56\xe4\x00\x21\x22\xbe\xda\xf2\x6e\xaa' +
            b'\x10\x7e\xce\x48\x60\x75\x23\x79\xec\x8b\xaa\x64\xf4\x00' +
            b'\x98\xbe\x92\xa4\x21\x4b\x69\xe9\x8b\x24\xae\x1c\xc4\xd2' +
            b'\xf4\x57\xcf\xf4\xf4\x05\xa8\x2e\xf9\x4c\x5f\x8d\xfa\xad' +
            b'\xd3\x07\x8d\x7a\x92\x24\x88\x7d\xb8\x6c\x32\x18\xbf\x53' +
            b'\xc9\x77\x9e\xd0\x98\x95\xb2\xcf\xb8\x4f\x1f\xad\x2e\x5b' +
            b'\x1f\x8e\x4b\x20\x9c\x57\x85\xb9\xce\x33\x2c\xd4\x13\x56' +
            b'\xc1\x71'))

    def test_hashAndVerify_PKCS1_sha1_notSet(self):
        sigBytes = bytearray(
            b'\x17\x50\x15\xbd\xa5\x0a\xbe\x0f\xa7\xd3\x9a\x83\x53\x88' +
            b'\x5c\xa0\x1b\xe3\xa7\xe7\xfc\xc5\x50\x45\x74\x41\x11\x36' +
            b'\x2e\xe1\x91\x44\x73\xa4\x8d\xc5\x37\xd9\x56\x29\x4b\x9e' +
            b'\x20\xa1\xef\x66\x1d\x58\x53\x7a\xcd\xc8\xde\x90\x8f\xa0' +
            b'\x50\x63\x0f\xcc\x27\x2e\x6d\x00\x10\x45\xe6\xfd\xee\xd2' +
            b'\xd1\x05\x31\xc8\x60\x33\x34\xc2\xe8\xdb\x39\xe7\x3e\x6d' +
            b'\x96\x65\xee\x13\x43\xf9\xe4\x19\x83\x02\xd2\x20\x1b\x44' +
            b'\xe8\xe8\xd0\x6b\x3e\xf4\x9c\xee\x61\x97\x58\x21\x63\xa8' +
            b'\x49\x00\x89\xca\x65\x4c\x00\x12\xfc\xe1\xba\x65\x11\x08' +
            b'\x97\x50')

        self.assertTrue(self.rsa.hashAndVerify(sigBytes,
                                               self.message, "PKCS1"))

    def test_hashAndVerify_PKCS1_sha224(self):
        sigBytes = bytearray(
            b'\x57\x67\x7b\x08\x9e\x20\x54\x86\xdf\x4f\x56\x75\x59\x72' +
            b'\xe3\xaf\x88\xca\xbb\xc2\x3e\xfe\x29\x43\x9b\x8d\x1e\x60' +
            b'\xac\x22\x6e\x99\x0d\xa4\x87\x85\x73\x92\x85\x6d\x12\xcd' +
            b'\xce\xa3\x87\xa2\x69\xd1\xbb\xbc\x12\x85\x49\xa1\x13\x5a' +
            b'\xb0\x62\x20\x1c\xab\x8a\xc0\x88\x86\xa3\x13\xaf\x85\x54' +
            b'\x50\x6d\x7a\x93\x85\x5b\x84\x30\x86\xa1\xbf\x3d\xfb\xcb' +
            b'\x00\x4c\xcd\xe7\x79\xc0\x84\xff\xa1\x72\x4b\x41\xd1\x7e' +
            b'\x10\xc8\xdd\x67\xdc\x0d\xf2\x62\x00\x37\x65\x50\xed\xa1' +
            b'\x44\x55\xd9\xb0\xb3\x1f\x1d\x8c\x5e\x8b\xb1\xd3\xd9\x63' +
            b'\xd0\xd5')

        self.assertTrue(self.rsa.hashAndVerify(sigBytes,
                                               self.message, "PKCS1",
                                               'sha224'))

    def test_hashAndVerify_PKCS1_sha256(self):
        sigBytes = bytearray(
            b'\x0b\x20\xe5\x09\x3c\x2a\x92\x62\x33\x10\x8a\xfb\xdd\x85' +
            b'\x1b\x88\xee\xb5\x54\xf4\xbe\xaa\x7b\x18\xe5\x15\x19\xf7' +
            b'\xd0\xec\x53\xb1\x81\xa3\xb0\x3e\x84\x84\xba\x8d\xe2\xaa' +
            b'\x78\x64\xa4\x02\xe2\x20\x8e\x84\xec\x99\x14\xaf\x9d\x77' +
            b'\x6e\xd1\x3c\x48\xbd\xeb\x64\x84\x25\x4d\xe1\x69\x31\x8a' +
            b'\x87\xc4\x0f\x22\x65\xff\x16\x71\x4e\xae\x8a\xee\x2b\xc9' +
            b'\xc3\xcb\x4d\xee\x04\x5e\x4f\x5d\x9d\x62\x52\x10\x12\x1b' +
            b'\xfc\xf2\xbe\xd8\xd3\xff\xa6\x02\xce\x27\xff\xf4\xe6\x1c' +
            b'\xf9\xbb\x65\x0e\x71\xa6\x92\x1a\xe6\xff\xa2\x96\xcb\x11' +
            b'\xbd\xbb')

        self.assertTrue(self.rsa.hashAndVerify(sigBytes,
                                               self.message, "PKCS1",
                                               'sha256'))

    def test_hashAndVerify_PKCS1_sha384(self):
        sigBytes = bytearray(
            b'\x7e\x3c\xcb\x6a\xb0\x3b\x41\x9a\x3e\x54\xf8\x13\x37\xa3' +
            b'\xc3\xf7\x2e\x8c\x65\xbb\xd1\x9d\xdd\x50\x24\x6a\x36\xf5' +
            b'\x1f\x58\x74\x1e\xc2\x45\xd2\xd0\xf0\x76\x77\xa4\xf8\x8a' +
            b'\xa3\xb1\xca\xee\xcd\xff\xe5\xfd\x6e\xdc\xf8\xb8\xbc\xfb' +
            b'\x56\x96\x37\xad\x02\xeb\x15\x4d\x17\xb8\x7a\x8f\x00\xd0' +
            b'\xe6\x18\xa7\xf4\xa7\x0c\xe4\x07\xf2\x03\x59\x15\x3e\x5f' +
            b'\x4a\x4d\x97\x44\xf3\xf3\xff\x44\x12\x0c\x08\xa4\x60\x50' +
            b'\x0f\x03\x0f\xd3\x39\x8e\x97\xfc\xae\xf9\xd0\xa7\xe2\xac' +
            b'\xef\x19\xa8\x1f\x70\x68\x05\xbe\x5f\xc0\x03\xd7\x8e\x5b' +
            b'\x29\xc0')

        self.assertTrue(self.rsa.hashAndVerify(sigBytes,
                                               self.message, "PKCS1",
                                               'sha384'))

    def test_hashAndVerify_PKCS1_sha512(self):
        sigBytes = bytearray(
            b'\x8b\x57\xa6\xf9\x16\x06\xba\x48\x13\xb8\x35\x36\x58\x1e' +
            b'\xb1\x5d\x72\x87\x5d\xcb\xb0\xa5\x14\xb4\xc0\x3b\x6d\xf8' +
            b'\xf2\x02\xfa\x85\x56\xe4\x00\x21\x22\xbe\xda\xf2\x6e\xaa' +
            b'\x10\x7e\xce\x48\x60\x75\x23\x79\xec\x8b\xaa\x64\xf4\x00' +
            b'\x98\xbe\x92\xa4\x21\x4b\x69\xe9\x8b\x24\xae\x1c\xc4\xd2' +
            b'\xf4\x57\xcf\xf4\xf4\x05\xa8\x2e\xf9\x4c\x5f\x8d\xfa\xad' +
            b'\xd3\x07\x8d\x7a\x92\x24\x88\x7d\xb8\x6c\x32\x18\xbf\x53' +
            b'\xc9\x77\x9e\xd0\x98\x95\xb2\xcf\xb8\x4f\x1f\xad\x2e\x5b' +
            b'\x1f\x8e\x4b\x20\x9c\x57\x85\xb9\xce\x33\x2c\xd4\x13\x56' +
            b'\xc1\x71')

        self.assertTrue(self.rsa.hashAndVerify(sigBytes,
                                               self.message, "PKCS1",
                                               'sha512'))
    def test_verify_PKCS1_sha512(self):
        sigBytes = bytearray(
            b'\x8b\x57\xa6\xf9\x16\x06\xba\x48\x13\xb8\x35\x36\x58\x1e' +
            b'\xb1\x5d\x72\x87\x5d\xcb\xb0\xa5\x14\xb4\xc0\x3b\x6d\xf8' +
            b'\xf2\x02\xfa\x85\x56\xe4\x00\x21\x22\xbe\xda\xf2\x6e\xaa' +
            b'\x10\x7e\xce\x48\x60\x75\x23\x79\xec\x8b\xaa\x64\xf4\x00' +
            b'\x98\xbe\x92\xa4\x21\x4b\x69\xe9\x8b\x24\xae\x1c\xc4\xd2' +
            b'\xf4\x57\xcf\xf4\xf4\x05\xa8\x2e\xf9\x4c\x5f\x8d\xfa\xad' +
            b'\xd3\x07\x8d\x7a\x92\x24\x88\x7d\xb8\x6c\x32\x18\xbf\x53' +
            b'\xc9\x77\x9e\xd0\x98\x95\xb2\xcf\xb8\x4f\x1f\xad\x2e\x5b' +
            b'\x1f\x8e\x4b\x20\x9c\x57\x85\xb9\xce\x33\x2c\xd4\x13\x56' +
            b'\xc1\x71')
        self.assertTrue(self.rsa.verify(sigBytes,
                                        secureHash(self.message, "sha512"),
                                        hashAlg="sha512"))

    def test_verify_invalid_PKCS1_sha512(self):
        sigBytes = bytearray(
            b'\x0b\x57\xa6\xf9\x16\x06\xba\x48\x13\xb8\x35\x36\x58\x1e' +
            b'\xb1\x5d\x72\x87\x5d\xcb\xb0\xa5\x14\xb4\xc0\x3b\x6d\xf8' +
            b'\xf2\x02\xfa\x85\x56\xe4\x00\x21\x22\xbe\xda\xf2\x6e\xaa' +
            b'\x10\x7e\xce\x48\x60\x75\x23\x79\xec\x8b\xaa\x64\xf4\x00' +
            b'\x98\xbe\x92\xa4\x21\x4b\x69\xe9\x8b\x24\xae\x1c\xc4\xd2' +
            b'\xf4\x57\xcf\xf4\xf4\x05\xa8\x2e\xf9\x4c\x5f\x8d\xfa\xad' +
            b'\xd3\x07\x8d\x7a\x92\x24\x88\x7d\xb8\x6c\x32\x18\xbf\x53' +
            b'\xc9\x77\x9e\xd0\x98\x95\xb2\xcf\xb8\x4f\x1f\xad\x2e\x5b' +
            b'\x1f\x8e\x4b\x20\x9c\x57\x85\xb9\xce\x33\x2c\xd4\x13\x56' +
            b'\xc1\x71')
        self.assertFalse(self.rsa.verify(sigBytes,
                                         secureHash(self.message, "sha512"),
                                         hashAlg="sha512"))


# because RSAKey is an abstract class...
class TestRSAKey(unittest.TestCase):

    # random RSA parameters
    N = int("101394340507163232476731540998223559348384567842249950630680016"
            "729829651735259973644737329194901739140557378171784099933376993"
            "53519793819698299093375577631")
    e = 65537
    d = int("141745721972918790698280063566067268498148845185400775263435953"
            "111621933337897734637889622802200979017278309730638712431978569"
            "771023240787627463565420833")
    p = int("903614668974112441151570413608036278756730123846327797584414732"
            "71561046135679")
    q = int("112209710608480690748363491355148749700390327497055102381924341"
            "581861552321889")
    dP = int("37883511062045429960298073888481933556799848761465588242411735"
             "654811958185817")
    dQ = int("62620473256245674709410658602365234471246407950887183034263101"
             "286525236349249")
    qInv = int("479278327226690415958629934820002183615697717603796111150941"
               "44623120451328875")

    def test___init__(self):
        rsa = Python_RSAKey()

        self.assertIsNotNone(rsa)

    def test___init___with_values(self):
        rsa = Python_RSAKey(self.N, self.e, self.d, self.p, self.q, self.dP,
                            self.dQ, self.qInv)

        self.assertIsNotNone(rsa)

    def test_hashAndSign(self):
        rsa = Python_RSAKey(self.N, self.e, self.d, self.p, self.q, self.dP,
                            self.dQ, self.qInv)

        sigBytes = rsa.hashAndSign(bytearray(b'text to sign'))

        self.assertEqual(bytearray(
            b'K\x7f\xf2\xca\x81\xf0A1\x95\xb1\x19\xe3\xd7QTL*Q|\xb6\x04' +
            b'\xbdG\x88H\x12\xc3\xe2\xb3\x97\xd2\xcd\xd8\xe8^Zn^\x8f\x1a' +
            b'\xae\x9a\x0b)\xb5K\xe8\x98|R\xac\xdc\xdc\n\x7f\x8b\xe7\xe6' +
            b'HQ\xc3hS\x19'), sigBytes)

    def test_hashAndSign_PSS(self):
        rsa = Python_RSAKey(self.N, self.e, self.d, self.p, self.q, self.dP,
                            self.dQ, self.qInv)

        sigBytes = rsa.hashAndSign(bytearray(b'text to sign'), "PSS", "sha1")
        self.assertEqual(bytearray(b'op\xfa\x1d\xfa\xe8i\xf2zV\x9a\xf4\x8d' +
                                   b'\xf1\xaf:\x1a\xb6\xce\xae3\xd1\xc2E[EG' +
                                   b'\x8ba\xfe.\x8e\x9dJ\xc9<Q\x05\xeaO\x8c' +
                                   b'\x8b\x01\xaer\x0f\xd8R\xb1\x1f\xb0\x06' +
                                   b'\x95\\\x8c\xae\xc9\xec\xa5{\x13' +
                                   b'\xa2ms'), sigBytes)

    def test_hashAndVerify(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'K\x7f\xf2\xca\x81\xf0A1\x95\xb1\x19\xe3\xd7QTL*Q|\xb6\x04' +
            b'\xbdG\x88H\x12\xc3\xe2\xb3\x97\xd2\xcd\xd8\xe8^Zn^\x8f\x1a' +
            b'\xae\x9a\x0b)\xb5K\xe8\x98|R\xac\xdc\xdc\n\x7f\x8b\xe7\xe6' +
            b'HQ\xc3hS\x19')

        self.assertTrue(rsa.hashAndVerify(sigBytes,
                                          bytearray(b'text to sign')))

    def test_hashAndVerify_PSS(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'op\xfa\x1d\xfa\xe8i\xf2zV\x9a\xf4\x8d\xf1\xaf:\x1a\xb6\xce' +
            b'\xae3\xd1\xc2E[EG\x8ba\xfe.\x8e\x9dJ\xc9<Q\x05\xeaO\x8c\x8b' +
            b'\x01\xaer\x0f\xd8R\xb1\x1f\xb0\x06\x95\\\x8c\xae\xc9\xec' +
            b'\xa5{\x13\xa2ms')

        self.assertTrue(rsa.hashAndVerify(sigBytes, bytearray(b'text to sign'),
                                          "PSS", 'sha1'))

    def test_verify_PSS(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'op\xfa\x1d\xfa\xe8i\xf2zV\x9a\xf4\x8d\xf1\xaf:\x1a\xb6\xce' +
            b'\xae3\xd1\xc2E[EG\x8ba\xfe.\x8e\x9dJ\xc9<Q\x05\xeaO\x8c\x8b' +
            b'\x01\xaer\x0f\xd8R\xb1\x1f\xb0\x06\x95\\\x8c\xae\xc9\xec' +
            b'\xa5{\x13\xa2ms')

        self.assertTrue(rsa.verify(sigBytes,
                                   secureHash(bytearray(b'text to sign'),
                                              'sha1'),
                                   "pss", 'sha1', 0))

    def test_verify_invalid_PSS(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'Xp\xfa\x1d\xfa\xe8i\xf2zV\x9a\xf4\x8d\xf1\xaf:\x1a\xb6\xce' +
            b'\xae3\xd1\xc2E[EG\x8ba\xfe.\x8e\x9dJ\xc9<Q\x05\xeaO\x8c\x8b' +
            b'\x01\xaer\x0f\xd8R\xb1\x1f\xb0\x06\x95\\\x8c\xae\xc9\xec' +
            b'\xa5{\x13\xa2ms')

        self.assertFalse(rsa.verify(sigBytes,
                                    secureHash(bytearray(b'text to sign'),
                                               'sha1'),
                                    "pss", 'sha1', 0))

    def test_hashAndVerify_without_NULL_encoding_of_SHA1(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'F\xe7\x8a>\x8a<;Cj\xdd\xea\x7f\x9d\x0c\xfd\xa7r\xd8\xa1O' +
            b'\xe1\xf5\x174\x0bR\xad:+\xc9C\x06\xf4\x88n\tp\x14FJ=\xfa' +
            b'\x8b\xefc\xe2\xdf\x00e\xc1\x1e\xe8\xd2\x97@\x8a\x96\xe2' +
            b'\x039Y_\x9c\xc9')

        self.assertTrue(rsa.hashAndVerify(sigBytes,
                                          bytearray(b'text to sign')))

    def test_hashAndVerify_with_invalid_signature(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(64)

        self.assertFalse(rsa.hashAndVerify(sigBytes,
                                           bytearray(b'text to sign')))

    def test_hashAndVerify_with_slightly_wrong_signature(self):
        rsa = Python_RSAKey(self.N, self.e)

        sigBytes = bytearray(
            b'K\x7f\xf2\xca\x81\xf0A1\x95\xb1\x19\xe3\xd7QTL*Q|\xb6\x04' +
            b'\xbdG\x88H\x12\xc3\xe2\xb3\x97\xd2\xcd\xd8\xe8^Zn^\x8f\x1a' +
            b'\xae\x9a\x0b)\xb5K\xe8\x98|R\xac\xdc\xdc\n\x7f\x8b\xe7\xe6' +
            b'HQ\xc3hS\x19')
        sigBytes[0] = 255

        self.assertFalse(rsa.hashAndVerify(sigBytes,
                                           bytearray(b'text to sign')))

    def test_addPKCS1SHA1Prefix(self):
        data = bytearray(b' sha-1 hash of data ')

        self.assertEqual(RSAKey.addPKCS1SHA1Prefix(data), bytearray(
            b'0!0\t\x06\x05+\x0e\x03\x02\x1a\x05\x00\x04\x14' + 
            b' sha-1 hash of data '))

    def test_addPKCS1SHA1Prefix_without_NULL(self):
        data = bytearray(b' sha-1 hash of data ')

        self.assertEqual(RSAKey.addPKCS1SHA1Prefix(data, False), bytearray(
            b'0\x1f0\x07\x06\x05+\x0e\x03\x02\x1a\x04\x14' +
            b' sha-1 hash of data '))

    def test_addPKCS1Prefix(self):
        data = bytearray(b' sha-1 hash of data ')

        self.assertEqual(RSAKey.addPKCS1Prefix(data, 'sha1'), bytearray(
            b'0!0\t\x06\x05+\x0e\x03\x02\x1a\x05\x00\x04\x14' +
            b' sha-1 hash of data '))


class TestRSADecrypt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        priv_key = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIzIOXFAmNpWyq
I2QPk9yJl8FjcpaPwbDG31ETwclOiyHkitIpfmVBkBG05tj15zsbeLJXQAMh0e9r
YC1OyM6NFByUkF60rTBmOaSSBlNLbn8mB0I+l9/9EzyI1yE5ne+8fpbM3L1/Oq4f
6JJxK/tJKYF9URZmRAofrLeiCPXqFlkQrdij8tSXICNgzLYyAk8NBxacGRjzFveU
sUOu9U7IdSKkwCl4+WiZgL/79knDB+gYGb/4hAljjUi9lL4VK1n/ZJ+gvWKdD/oY
E8Or9LVr08LqVGXf+hRYkpKp2KJK0mvn7gUQdBtjgtQ8g9W/pApGYT0GK+RFUX28
rwy04adpAgMBAAECggEAFFUBDg8tWHZjpmam/xzNu/Dt2BAGRtAqAjkikImSxK05
5VZZKXJu9lCMOnEVjvC2/3UdOdB1gLstLwYyEEQtBgP/UNu9ezX+LJuxmkehr4Wk
wkkB4CyotYt5GbIO3zKqz79RrbS8S2G5t+loyqTVcPcO8Y2AYyKIk+R9Q578p5Ml
m88s0Qij2GiM3weOeseZlp8jOdLB9SK5aWhGKakzuq7CaBYl6rhPTlb0RH6diPua
GZz3ECPg4lexREGzPITTvGfKgDHSYSYYEDp6CkCEQmL3XYiQzWFuUfkDVIj9bgmd
6P9tZaT/EYJUgHyfWNL7uouhUdyMaL40nJd6IE4EwQKBgQD49a1rqCiTG+pFm4o/
bcBB0jSCQJwlcelj8x90hgKiVjcbOIPtRZ7PlwUmRZ7dFuBVIvWkXZR1Gy7C2vJy
x/iBalLADRgIAXFjTaiZ15cyIvUbk3YwVIaWqffYwkpZSXwe/NRVz7l+6G0rbTSX
KzMv2jA/BJmbTra1zAuzPndh3QKBgQDOei47SakLljMKEtxoK9+9+66N1twDthR6
771XV0Pw9tpNhiNQYbca/ZytLTQCXlashrD3dD6zXhrLyiN4lUJEZbcG7SIXXlcY
yMcLZwPqj2tRD5Rb5I5aNrs8PJFzK1id/AXXLYCQMZRFK9ohNIZH7HKUPxGoRuYv
rr6OtTaw/QKBgHb+FfGK4jnN8d9rRFykvGu5aNeIwhkzpPXc0oADPWcSBizAim3y
BMH70L5GMHRD5t1KZFY3VCnU4DjKJW+vHJvekcaxe3b4GZX5HEjLvrx78ONJTAg1
nk6M1qWH17ltYiH9fg+1xVdfCC7ld2l5gHGyu7SjIjgVG0cxS7ZUeQMRAoGBAJmI
SLBVSZoQCcvH0pSzax/98gIObnNkBT6U3hoADck0BYf34nJ29ozfYI11O2M3ewO2
9AhNLAJ8SziWCmIzup7Zc4t28Q6nW+RWB4v3AfZ8xrPz/cGG5kM2x2s3LoCRDsgL
CtzCPQL7muEEhqKCSAdbTqflbd/POILkUVYUcaKRAoGAZDv3RkKffYNmegZTAhNH
77/AXmNR+CGp3rtg4OzN5QBa2ensMeVY9+ksKTKOdFadfO98dMq8KzVe1AGhoJFL
Tjy7BkhOWBlgURae0UyqLvpuoETgVNJhRMwWKcVQEFWKBOEz9Et8JE2sJb+RPFe4
kO5J9UglnNY0BP72hZ3Pl1o=
-----END PRIVATE KEY-----
"""
        cls.priv_key = parsePEMKey(priv_key, private=True)

        pub_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyMyDlxQJjaVsqiNkD5Pc
iZfBY3KWj8Gwxt9RE8HJTosh5IrSKX5lQZARtObY9ec7G3iyV0ADIdHva2AtTsjO
jRQclJBetK0wZjmkkgZTS25/JgdCPpff/RM8iNchOZ3vvH6WzNy9fzquH+iScSv7
SSmBfVEWZkQKH6y3ogj16hZZEK3Yo/LUlyAjYMy2MgJPDQcWnBkY8xb3lLFDrvVO
yHUipMApePlomYC/+/ZJwwfoGBm/+IQJY41IvZS+FStZ/2SfoL1inQ/6GBPDq/S1
a9PC6lRl3/oUWJKSqdiiStJr5+4FEHQbY4LUPIPVv6QKRmE9BivkRVF9vK8MtOGn
aQIDAQAB
-----END PUBLIC KEY-----
"""
        cls.pub_key = parsePEMKey(pub_key, public=True)

    def test_sanity(self):
        self.assertIsNotNone(self.priv_key)
        self.assertIsNotNone(self.pub_key)

        self.assertEqual(
            self.priv_key.d,
            bytesToNumber(a2b_hex(
                "1455010e0f2d587663a666a6ff1ccdbbf0edd8100646d02a023922908992"
                "c4ad39e5565929726ef6508c3a71158ef0b6ff751d39d07580bb2d2f0632"
                "10442d0603ff50dbbd7b35fe2c9bb19a47a1af85a4c24901e02ca8b58b79"
                "19b20edf32aacfbf51adb4bc4b61b9b7e968caa4d570f70ef18d80632288"
                "93e47d439efca793259bcf2cd108a3d8688cdf078e7ac799969f2339d2c1"
                "f522b969684629a933baaec2681625eab84f4e56f4447e9d88fb9a199cf7"
                "1023e0e257b14441b33c84d3bc67ca8031d2612618103a7a0a40844262f7"
                "5d8890cd616e51f9035488fd6e099de8ff6d65a4ff118254807c9f58d2fb"
                "ba8ba151dc8c68be349c977a204e04c1")))

    def test_simple_encypt_decrypt(self):
        # just verify that decrypting encrypted message gives the expected
        # message back
        self.assertEqual(
            self.priv_key.decrypt(self.pub_key.encrypt(b'message')),
            b'message')

    def test_decryption(self):
        # a random positive test case
        ciphertext = a2b_hex(remove_whitespace("""
8bfe264e85d3bdeaa6b8851b8e3b956ee3d226fd3f69063a86880173a273d9f2
83b2eebdd1ed35f7e02d91c571981b6737d5320bd8396b0f3ad5b019daec1b0a
ab3cbbc026395f4fd14f13673f2dfc81f9b660ec26ac381e6db3299b4e460b43
fab9955df2b3cfaa20e900e19c856238fd371899c2bf2ce8c868b76754e5db3b
036533fd603746be13c10d4e3e6022ebc905d20c2a7f32b215a4cd53b3f44ca1
c327d2c2b651145821c08396c89071f665349c25e44d2733cd9305985ceef643
0c3cf57af5fa224089221218fa34737c79c446d28a94c41c96e4e92ac53fbcf3
84dea8419ea089f8784445a492c812eb0d409467f75afd7d4d1078886205a066
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, b'lorem ipsum dolor sit amet')

    def test_valid_to_empty(self):
        ciphertext = a2b_hex(remove_whitespace("""
443ad9c5f00a1f4e9601717d274aacc93a824cb4d99b3c6a42e2b017e52e0184
43bd77d34a80703cd9b6acf523cd3b2cd1fea31940a68fba828836f1c3ed2fef
071e95e0922ff0f47d0e81dacc13ecdeda3db6476f41e5b3f9ccfcfdf9155800
7b68ffbbe5e93bb088f1e4f0bb39bc7d8600b38930ecd00a341d8cc76955837e
fff0f0797c4b46fb1b375bba49bcdc877f39aaadb045c56b836072383eec6627
ae280ad4f9a45d6e5b4cc7cf61d42b194ff0b9c9167c621e5380d8333e3b7f20
c8d564c9ec6c2805f77c0146adea2f688a943b67ce8889f4a6353e6396d551c3
6a6dbf19359a825d14b69ccc4fd747cf14a1ca8578d7f0a67dc14b37f5e17ca3
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-1]))
        self.assertEqual(dec[-1:], b'\x00')

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, b'')

    def test_positive_11_byte_long_with_null_padded_ciphertext(self):
        # ciphertext that starts with a null byte, decrypts to real 11 byte
        # long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
00a2e8f114ea8d05d12dc843e3cc3b2edc8229ff2a028bda29ba9d55e3cd0291
1902fef1f42a075bf05e8016e8567213d6f260fa49e360779dd81aeea3e04c2c
b567e0d72b98bf754014561b7511e083d20e0bfb9cd23f8a0d3c88900c49d2fc
d5843ff0765607b2026f28202a87aa94678aed22a0c20724541394cd8f44e373
eba1d2bae98f516c1e2ba3d86852d064f856b1daf24795e767a2b90396e50743
e3150664afab131fe40ea405dcf572dd1079af1d3f0392ccadcca0a12740dbb2
13b925ca2a06b1bc1383e83a658c82ba2e7427342379084d5f66b544579f0766
4cb26edd4f10fd913fdbc0de05ef887d4d1ec1ac95652397ea7fd4e4759fda8b
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'lorem ipsum'

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        self.assertEqual(len(plaintext), 11)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_empty(self):
        ciphertext = a2b_hex(remove_whitespace("""
20aaa8adbbc593a924ba1c5c7990b5c2242ae4b99d0fe636a19a4cf754edbcee
774e472fe028160ed42634f8864900cb514006da642cae6ae8c7d087caebcfa6
dad1551301e130344989a1d462d4164505f6393933450c67bc6d39d8f5160907
cabc251b737925a1cf21e5c6aa5781b7769f6a2a583d97cce008c0f8b6add5f0
b2bd80bee60237aa39bb20719fe75749f4bc4e42466ef5a861ae3a92395c7d85
8d430bfe38040f445ea93fa2958b503539800ffa5ce5f8cf51fa8171a91f36cb
4f4575e8de6b4d3f096ee140b938fd2f50ee13f0d050222e2a72b0a3069ff3a6
738e82c87090caa5aed4fcbe882c49646aa250b98f12f83c8d528113614a29e7
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-1:], b'\x00')

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, b'')

    def test_invalid_decrypting_to_max_length(self):
        # the last value from PRF is 245, which is exactly the max we
        # can return
        ciphertext = a2b_hex(remove_whitespace("""
48cceab10f39a4db32f60074feea473cbcdb7accf92e150417f76b44756b190e
843e79ec12aa85083a21f5437e7bad0a60482e601198f9d86923239c8786ee72
8285afd0937f7dde12717f28389843d7375912b07b991f4fdb0190fced8ba665
314367e8c5f9d2981d0f5128feeb46cb50fc237e64438a86df198dd0209364ae
3a842d77532b66b7ef263b83b1541ed671b120dfd660462e2107a4ee7b964e73
4a7bd68d90dda61770658a3c242948532da32648687e0318286473f675b412d6
468f013f14d760a358dfcad3cda2afeec5e268a37d250c37f722f468a70dfd92
d7294c3c1ee1e7f8843b7d16f9f37ef35748c3ae93aa155cdcdfeb4e78567303
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:11],
            b'\x78\x05\x5c\xc0\xd7\x02\xfe\xd7\x6a\xbe\x53')

        plaintext = a2b_hex(remove_whitespace("""
22d850137b9eebe092b24f602dc5bb7918c16bd89ddbf20467b119d205f9c2e4
bd7d2592cf1e532106e0f33557565923c73a02d4f09c0c22bea89148183e6031
7f7028b3aa1f261f91c979393101d7e15f4067e63979b32751658ef769610fe9
7cf9cef3278b3117d384051c3b1d82c251c2305418c8f6840530e631aad63e70
e20e025bcd8efb54c92ec6d3b106a2f8e64eeff7d38495b0fc50c97138af4b1c
0a67a1c4e27b077b8439332edfa8608dfeae653cd6a628ac550395f7e74390e4
2c11682234870925eeaa1fa71b76cf1f2ee3bda69f6717033ff8b7c95c9799e7
a3bea5e7e4a1c359772fb6b1c6e6c516661dfe30c3
"""))
        self.assertEqual(len(plaintext), numBytes(self.pub_key.n) - 2 - 8 - 1)
        self.assertEqual(len(plaintext), 2048 // 8 - 2 - 8 - 1)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_zero_padded_ciphertext(self):
        ciphertext = a2b_hex(remove_whitespace("""
006f89db685c0a132700c6a17f88a37a6635d0ab89de4c45dc09736c891ca5bf
3401ce34c6e5d51e94ed2f518857ddc12d9f9f9e68e01cdc30d86ae5dd83988c
0c46a8e39daa1b328a23def551d67fa1964fb15242c83ddd7dd5b1aec720a391
d0b86cb16cf4d3c466850c3df88a3ed85993900d1287a0c90c4b04d34ba29e59
967661f3f10e0c998f64e14e777e8e81371eca5318b4e0b53414292130c82147
7c51e2bff844836ab10dff293d82e4f40d345968ef268c92ed0bc238f31d50f4
d3f759c23964923e135d15527556410fbd2c451d6a2aa852dc88b01139c6fdd8
26736d8cd3780601b2977b09c080bd8c0fa471606ad59f053ad33d9eeb905f20
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:3],
            b'\x15\x1c\x6d')

        plaintext = a2b_hex(remove_whitespace("""
2b5dd72df3cae37f1aef
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_length_second_to_last_from_prf(self):
        # the last value from the PRF is 246, which is longer than the max
        # allowed length: 245, so it needs to select second to last: 2
        ciphertext = a2b_hex(remove_whitespace("""
1439e08c3f84c1a7fec74ce07614b20e01f6fa4e8c2a6cffdc3520d8889e5d9a
950c6425798f85d4be38d300ea5695f13ecd4cb389d1ff5b82484b494d6280ab
7fa78e645933981cb934cce8bfcd114cc0e6811eefa47aae20af638a1cd163d2
d3366186d0a07df0c81f6c9f3171cf3561472e98a6006bf75ddb457bed036dcc
e199369de7d94ef2c68e8467ee0604eea2b3009479162a7891ba5c40cab17f49
e1c438cb6eaea4f76ce23cce0e483ff0e96fa790ea15be67671814342d0a23f4
a20262b6182e72f3a67cd289711503c85516a9ed225422f98b116f1ab080a80a
bd6f0216df88d8cfd67c139243be8dd78502a7aaf6bc99d7da71bcdf627e7354
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        kdk = calc_kdk(self.priv_key, ciphertext)

        lengths = calc_lengths(self.priv_key, kdk)
        max_len = numBytes(self.pub_key.n) - 1 - 1 - 8 -1

        # the last_len is too long
        self.assertGreater(lengths[-1], max_len)
        self.assertEqual(lengths[-1], 246)

        # while second to last is short enough
        self.assertLessEqual(lengths[-2], max_len)
        self.assertEqual(2, lengths[-2])

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertEqual(dec[-3:], b'\xd1\x90\x17')

        plaintext = a2b_hex(remove_whitespace("""
0f9b
"""))

        self.assertEqual(len(plaintext), 2)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_wrong_version_byte(self):
        # an otherwise correct plaintext, but with wrong first byte
        # (0x01 instead of 0x00), generates a random 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
9b2ec9c0c917c98f1ad3d0119aec6be51ae3106e9af1914d48600ab6a2c0c0c8
ae02a2dc3039906ff3aac904af32ec798fd65f3ad1afa2e69400e7c1de81f572
8f3b3291f38263bc7a90a0563e43ce7a0d4ee9c0d8a716621ca5d3d081188769
ce1b131af7d35b13dea99153579c86db31fe07d5a2c14d621b77854e48a8df41
b5798563af489a291e417b6a334c63222627376118c02c53b6e86310f728734f
fc86ef9d7c8bf56c0c841b24b82b59f51aee4526ba1c4268506d301e4ebc498c
6aebb6fd5258c876bf900bac8ca4d309dd522f6a6343599a8bc3760f422c10c7
2d0ad527ce4af1874124ace3d99bb74db8d69d2528db22c3a37644640f95c05f
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x01\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
a1f8c9255c35cfba403ccc
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_wrong_type_byte(self):
        # an otherwise correct plaintext, but with wrong second byte
        # (0x01 instead of 0x02), generates a random 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
782c2b59a21a511243820acedd567c136f6d3090c115232a82a5efb0b178285f
55b5ec2d2bac96bf00d6592ea7cdc3341610c8fb07e527e5e2d20cfaf2c7f23e
375431f45e998929a02f25fd95354c33838090bca838502259e92d86d568bc2c
db132fab2a399593ca60a015dc2bb1afcd64fef8a3834e17e5358d822980dc44
6e845b3ab4702b1ee41fe5db716d92348d5091c15d35a110555a35deb4650a5a
1d2c98025d42d4544f8b32aa6a5e02dc02deaed9a7313b73b49b0d4772a3768b
0ea0db5846ace6569cae677bf67fb0acf3c255dc01ec8400c963b6e49b106772
8b4e563d7e1e1515664347b92ee64db7efb5452357a02fff7fcb7437abc2e579
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x01')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
e6d700309ca0ed62452254
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_11_bytes_long_with_null_padded_ciphertext(self):
        # an invalid ciphertext, with a zero byte in first byte of
        # ciphertext, decrypts to a random 11 byte long synthethic
        # plaintext
        ciphertext = a2b_hex(remove_whitespace("""
0096136621faf36d5290b16bd26295de27f895d1faa51c800dafce73d001d607
96cd4e2ac3fa2162131d859cd9da5a0c8a42281d9a63e5f353971b72e36b5722
e4ac444d77f892a5443deb3dca49fa732fe855727196e23c26eeac55eeced826
7a209ebc0f92f4656d64a6c13f7f7ce544ebeb0f668fe3a6c0f189e4bcd5ea12
b73cf63e0c8350ee130dd62f01e5c97a1e13f52fde96a9a1bc9936ce734fdd61
f27b18216f1d6de87f49cf4f2ea821fb8efd1f92cdad529baf7e31aff9bff407
4f2cad2b4243dd15a711adcf7de900851fbd6bcb53dac399d7c880531d06f25f
7002e1aaf1722765865d2c2b902c7736acd27bc6cbd3e38b560e2eecf7d4b576
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertNotEqual(dec[-12:-11], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
ba27b1842e7c21c0e7ef6a
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_null_byte_at_eight_byte_of_padding(self):
        # an otherwise correct plaintext, but with a null byte on tenth
        # position (eight byte of padding), generates a random 11 byte long
        # plaintext
        ciphertext = a2b_hex(remove_whitespace("""
a7a340675a82c30e22219a55bc07cdf36d47d01834c1834f917f18b517419ce9
de2a96460e745024436470ed85e94297b283537d52189c406a3f533cb405cc6a
9dba46b482ce98b6e3dd52d8fce2237425617e38c11fbc46b61897ef200d01e4
f25f5f6c4c5b38cd0de38ba11908b86595a8036a08a42a3d05b79600a97ac18b
a368a08d6cf6ccb624f6e8002afc75599fba4de3d4f3ba7d208391ebe8d21f82
82b18e2c10869eb2702e68f9176b42b0ddc9d763f0c86ba0ff92c957aaeab76d
9ab8da52ea297ec11d92d770146faa1b300e0f91ef969b53e7d2907ffc984e9a
9c9d11fb7d6cba91972059b46506b035efec6575c46d7114a6b935864858445f
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:9]))
        self.assertEqual(dec[9:10], b'\x00')
        self.assertTrue(all(i != 0 for i in dec[10:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
63cb0bf65fc8255dd29e17
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b"lorem ipsum")
        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_missing_null_separator(self):
        # an otherwise correct plaintext, but with missing zero separator
        # decrypts to 11 byte random synthethic plaintext
        ciphertext = a2b_hex(remove_whitespace("""
3d1b97e7aa34eaf1f4fc171ceb11dcfffd9a46a5b6961205b10b302818c1fcc9
f4ec78bf18ea0cee7e9fa5b16fb4c611463b368b3312ac11cf9c06b7cf72b54e
284848a508d3f02328c62c2999d0fb60929f81783c7a256891bc2ff4d91df2af
96a24fc5701a1823af939ce6dbdc510608e3d41eec172ad2d51b9fc61b4217c9
23cadcf5bac321355ef8be5e5f090cdc2bd0c697d9058247db3ad613fdce87d2
955a6d1c948a5160f93da21f731d74137f5d1f53a1923adb513d2e6e1589d44c
c079f4c6ddd471d38ac82d20d8b1d21f8d65f3b6907086809f4123e08d86fb38
729585de026a485d8f0e703fd4772f6668febf67df947b82195fa3867e3a3065
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        for val in dec[2:-12]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-12:], b'\x01lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
6f09a0b62699337c497b0b
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_length_third_to_last_from_prf(self):
        # the last three numbers from prf are: 2, 247, 255, so we need to
        # pick 2, the third one from the end
        ciphertext = a2b_hex(remove_whitespace("""
1690ebcceece2ce024f382e467cf8510e74514120937978576caf684d4a02ad569e8d76cbe36
5a060e00779de2f0865ccf0d923de3b4783a4e2c74f422e2f326086c390b658ba47f31ab013a
a80f468c71256e5fa5679b24e83cd82c3d1e05e398208155de2212993cd2b8bab6987cf4cc12
93f19909219439d74127545e9ed8a706961b8ee2119f6bfacafbef91b75a789ba65b8b833bc6
149cf49b5c4d2c6359f62808659ba6541e1cd24bf7f7410486b5103f6c0ea29334ea6f4975b1
7387474fe920710ea61568d7b7c0a7916acf21665ad5a31c4eabcde44f8fb6120d8457afa1f3
c85d517cda364af620113ae5a3c52a048821731922737307f77a1081"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertEqual(dec[-3:], b'\xee\xaf\xde')

        plaintext = a2b_hex(remove_whitespace("4f02"))

        self.assertEqual(len(plaintext), 2)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_11_byte_long(self):
        # ciphertext that generates a fake 11 byte plaintext, but decrypts
        # to real 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
6213634593332c485cef783ea2846e3d6e8b0e005cd8293eaebbaa5079712fd681579bdfbbda
138ae4d9d952917a03c92398ec0cb2bb0c6b5a8d55061fed0d0d8d72473563152648cfe640b3
35dc95331c21cb133a91790fa93ae44497c128708970d2beeb77e8721b061b1c44034143734a
77be8220877415a6dba073c3871605380542a9f25252a4babe8331cdd53cf828423f3cc70b56
0624d0581fb126b2ed4f4ed358f0eb8065cf176399ac1a846a31055f9ae8c9c24a1ba050bc20
842125bc1753158f8065f3adb9cc16bfdf83816bdf38b624f12022c5a6fbfe29bc91542be8c0
208a770bcd677dc597f5557dc2ce28a11bf3e3857f158717a33f6592"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'lorem ipsum'

        self.assertEqual(len(plaintext), 11)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_11_byte_long_with_double_null_padded_ciphertext(self):
        # ciphertext that starts with two null bytes, decrypts to real 11 byte
        # long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
00001f71879b426127f7dead621f7380a7098cf7d22173aa27991b143c46d53383c209bd0c9c
00d84078037e715f6b98c65005a77120070522ede51d472c87ef94b94ead4c5428ee108a3455
61658301911ec5a8f7dd43ed4a3957fd29fb02a3529bf63f8040d3953490939bd8f78b2a3404
b6fb5ff70a4bfdaac5c541d6bcce49c9778cc390be24cbef1d1eca7e870457241d3ff72ca44f
9f56bdf31a890fa5eb3a9107b603ccc9d06a5dd911a664c82b6abd4fe036f8db8d5a070c2d86
386ae18d97adc1847640c211d91ff5c3387574a26f8ef27ca7f48d2dd1f0c7f14b81cc9d33ee
6853031d3ecf10a914ffd90947909c8011fd30249219348ebff76bfc"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'lorem ipsum'

        self.assertEqual(len(plaintext), 11)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_11_byte_long_with_zero_generated_length(self):
        # valid ciphertext that generates a zero length fake plaintext
        ciphertext = a2b_hex(remove_whitespace("""
b5e49308f6e9590014ffaffc5b8560755739dd501f1d4e9227a7d291408cf4b753f292322ff8
bead613bf2caa181b221bc38caf6392deafb28eb21ad60930841ed02fd6225cc9c463409adbe
7d8f32440212fbe3881c51375bb09565efb22e62b071472fb38676e5b4e23a0617db5d14d935
19ac0007a30a9c822eb31c38b57fcb1be29608fcf1ca2abdcaf5d5752bbc2b5ac7dba5afcff4
a5641da360dd01f7112539b1ed46cdb550a3b1006559b9fe1891030ec80f0727c42401ddd6cb
b5e3c80f312df6ec89394c5a7118f573105e7ab00fe57833c126141b50a935224842addfb479
f75160659ba28877b512bb9a93084ad8bec540f92640f63a11a010e0"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        plaintext = b'lorem ipsum'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_11_byte_long_with_245_generated_length(self):
        # valid ciphertext that generates a 245 byte long fake plaintext
        ciphertext = a2b_hex(remove_whitespace("""
1ea0b50ca65203d0a09280d39704b24fe6e47800189db5033f202761a78bafb270c5e25abd1f
7ecc6e7abc4f26d1b0cd9b8c648d529416ee64ccbdd7aa72a771d0353262b543f0e436076f40
a1095f5c7dfd10dcf0059ccb30e92dfa5e0156618215f1c3ff3aa997a9d999e506924f5289e3
ac72e5e2086cc7b499d71583ed561028671155db4005bee01800a7cdbdae781dd32199b8914b
5d4011dd6ff11cd26d46aad54934d293b0bc403dd211bf13b5a5c6836a5e769930f437ffd863
4fb7371776f4bc88fa6c271d8aa6013df89ae6470154497c4ac861be2a1c65ebffec139bf7aa
ba3a81c7c5cdd84da9af5d3edfb957848074686b5837ecbcb6a41c50"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        plaintext = b"lorem ipsum"

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long(self):
        # a random ciphertext that generates a fake 11 byte plaintext
        # and fails padding check
        ciphertext = a2b_hex(remove_whitespace("""
5f02f4b1f46935c742ebe62b6f05aa0a3286aab91a49b34780adde6410ab46f7386e05748331
864ac98e1da63686e4babe3a19ed40a7f5ceefb89179596aab07ab1015e03b8f825084dab028
b6731288f2e511a4b314b6ea3997d2e8fe2825cef8897cbbdfb6c939d441d6e04948414bb69e
682927ef8576c9a7090d4aad0e74c520d6d5ce63a154720f00b76de8cc550b1aa14f016d63a7
b6d6eaa1f7dbe9e50200d3159b3d099c900116bf4eba3b94204f18b1317b07529751abf64a26
b0a0bf1c8ce757333b3d673211b67cc0653f2fe2620d57c8b6ee574a0323a167eab1106d9bc7
fd90d415be5f1e9891a0e6c709f4fc0404e8226f8477b4e939b36eb2"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-12:-11], b'\x00')

        plaintext = a2b_hex(remove_whitespace("af9ac70191c92413cb9f2d"))

        self.assertEqual(len(plaintext), 11)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_11_bytes_long_with_null_truncated_ciphertext(self):
        # same as test_negative_11_bytes_long_with_null_padded_ciphertext
        # but with the zero bytes at the beginning removed
        ciphertext = a2b_hex(remove_whitespace("""
96136621faf36d5290b16bd26295de27f895d1faa51c800dafce73d001d60796cd4e2ac3f
a2162131d859cd9da5a0c8a42281d9a63e5f353971b72e36b5722e4ac444d77f892a5443deb
3dca49fa732fe855727196e23c26eeac55eeced8267a209ebc0f92f4656d64a6c13f7f7ce54
4ebeb0f668fe3a6c0f189e4bcd5ea12b73cf63e0c8350ee130dd62f01e5c97a1e13f52fde96
a9a1bc9936ce734fdd61f27b18216f1d6de87f49cf4f2ea821fb8efd1f92cdad529baf7e31a
ff9bff4074f2cad2b4243dd15a711adcf7de900851fbd6bcb53dac399d7c880531d06f25f70
02e1aaf1722765865d2c2b902c7736acd27bc6cbd3e38b560e2eecf7d4b576
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n)-1)

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(b"\x00" + ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertNotEqual(dec[-12:-11], b'\x00')

        plaintext = a2b_hex(remove_whitespace("ba27b1842e7c21c0e7ef6a"))

        msg = self.priv_key.decrypt(ciphertext)

        # tlslite-ng considers a too short ciphertext a publicly known error
        # so it returns an error (None)
        self.assertEqual(msg, None)

    def test_negative_11_byte_long_with_double_null_padded_ciphertext(self):
        # an invalid ciphertext, with two zero byte in first bytes of
        # ciphertext, that decrypts to a random 11 byte long synthethic
        # plaintext
        ciphertext = a2b_hex(remove_whitespace("""
0000587cccc6b264bdfe0dc2149a988047fa921801f3502ea64624c510c6033d2f427e3f136
c26e88ea9f6519e86a542cec96aad1e5e9013c3cc203b6de15a69183050813af5c9ad797031
36d4b92f50ce171eefc6aa7988ecf02f319ffc5eafd6ee7a137f8fce64b255bb1b8dd19cfe7
67d64fdb468b9b2e9e7a0c24dae03239c8c714d3f40b7ee9c4e59ac15b17e4d328f1100756b
ce17133e8e7493b54e5006c3cbcdacd134130c5132a1edebdbd01a0c41452d16ed7a0788003
c34730d0808e7e14c797a21f2b45a8aa1644357fd5e988f99b017d9df37563a354c788dc0e2
f9466045622fa3f3e17db63414d27761f57392623a2bef6467501c63e8d645"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertNotEqual(dec[-12:-11], b'\x00')

        plaintext = a2b_hex(remove_whitespace("d5cf555b1d6151029a429a"))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)


    def test_negative_11_byte_long_null_type_byte(self):
        # an otherwise correct plaintext, but with wrong second byte
        # (0x00 instead of 0x02), and a 0x02 on third position, generates a
        # random 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
1786550ce8d8433052e01ecba8b76d3019f1355b212ac9d0f5191b023325a7e7714b7802f8e9
a17c4cb3cd3a84041891471b10ca1fcfb5d041d34c82e6d0011cf4dc76b90e9c2e0743590579
d55bcd7857057152c4a8040361343d1d22ba677d62b011407c652e234b1d663af25e2386251d
7409190f19fc8ec3f9374fdf1254633874ce2ec2bff40ad0cb473f9761ec7b68da45a4bd5e33
f5d7dac9b9a20821df9406b653f78a95a6c0ea0a4d57f867e4db22c17bf9a12c150f809a7b72
b6db86c22a8732241ebf3c6a4f2cf82671d917aba8bc61052b40ccddd743a94ea9b538175106
201971cca9d136d25081739aaf6cd18b2aecf9ad320ea3f89502f955"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[3:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("3d4a054d9358209e9cbbb9"))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_null_byte_first_byte_of_padding(self):
        # an otherwise correct plaintext, but with a null byte on third
        # position (first byte of padding), generates a random 11 byte
        # long payload
        ciphertext = a2b_hex(remove_whitespace("""
179598823812d2c58a7eb50521150a48bcca8b4eb53414018b6bca19f4801456c5e36a940037
ac516b0d6412ba44ec6b4f268a55ef1c5ffbf18a2f4e3522bb7b6ed89774b79bffa22f7d3102
165565642de0d43a955e96a1f2e80e5430671d7266eb4f905dc8ff5e106dc5588e5b0289e49a
4913940e392a97062616d2bda38155471b7d360cfb94681c702f60ed2d4de614ea72bf1c5316
0e63179f6c5b897b59492bee219108309f0b7b8cb2b136c346a5e98b8b4b8415fb1d713bae06
7911e3057f1c335b4b7e39101eafd5d28f0189037e4334f4fdb9038427b1d119a6702aa82333
19cc97d496cc289ae8c956ddc84042659a2d43d6aa22f12b81ab884e"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertTrue(all(i != 0 for i in dec[3:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex("1f037dd717b07d3e7f7359")

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b"lorem ipsum")
        self.assertEqual(msg, plaintext)



class TestRSA2049Decrypt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        priv_key = """
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQFV+IlVahd18cen
eGpQsYvCjJ6Ybt5WZ8qzm4QSTpDrp1wdsIOsPkQ7upTcI1YPdeOoFpOipDvcdCbY
xOr+aMhd4P51f25Ju57UR+YCQwgA27BM6yLn+lehjTOPtmAmzbRn5wzAQOfTZ+9A
PHvx499iRlAJRjHyHq/S+1vJFf8EN5rNERL3MsC0ZgfBeNOKIPUu2lCfL5wEBdUQ
aegMz5QVVNBHBGdQXDz1QeoIl9/J9ADOyymP/HUzctn2kzrxdMxA7ZbUZwMXM7l/
jN3T+SvDoD6oV2xBfyQAe15PdQEQW1RN6frc3/rfmN+0uwW4GZ8/haz9kfepoJS5
o4P1BJCXAgMBAAECggEBARnCs/UKetYVJnnX/1EJWKwtjKbwAoWS8zLVWhZzYXio
5n8X5wXOMA4+h1RyUQBgE/l00KPbSe80TKWiajTARQcE0OQi4M4jppQlwV/vtvJu
EG7v9kzIuddELk2k6MhQCOrrNlhZoilPo5N7wmvlYzLn2B4sFg72NcxSiqe+VeYz
pyPbweFrop5SsprvL55WVP3AZmuw/CVKy+gOY4dPD18CB4Ljydz8JSDQycSntjTk
UD+7ST4ar+6z+IvXoTOYcl2ub+OZ53XNXUzwn8g4NHxMmNqxpIg8zmIFE2Fa+qEK
YzaObXt530FmqxYnOe9RWkQC7h4GAcWlW8cd8OMO34ECgYEBiPaTYPAeGNmi3ilS
U9JSwx5Eds6l/3v4QT33/eNWUjzcl2gF+E/A3ex3DfBs7QZcgRNIdUs0avFpdWh3
/Ts9VoaCyHh9CzFO9qxn1l6BMzmLYqCDwPh2XFrUDVqB+bvc4lJ+1+lQCMsQKctM
q9H56b7fwobJZVIlXafqsZIXjvcCgYEA3sfPEdreg6TEPS+AGX8h/V1G/Ve0MfRP
6Bod439qCR/8BGTtlx3IUIg1rebMX1ZvOWVhOos2eYyS5uI/Uu+QfpVn40G+vFM3
GJYl+76rHzt7P5L/smgebvWnhKjC1498LYmqqiTSztvQZoHP5lw2x7+jxboTUWIi
LvXC6RTJg2ECgYASCT86c8rt2Q9gowTkVAL4casyyMlVsJr0Y6O+Q3Dy1VhKmrur
af2wMepE+YQGXQRh6ECrIYiGYA43FVRsiwuFrSbTjLQwj1LQf5lEfZHwh/Od00A4
2y6TjpetBTpx++1ndeHchxjlTmyvfmVGfZy63cfnZchYniyY39wlyk7KgQKBgQCM
zmE0ec+WCPf3bCRc+Ru0ldYeneZIhJBUtN0bQxbz+YFCDcCVeL95Fv5Gkc+ummTm
NAuGAyNFI/Jdd7ZqZvw+5ZOp8Y3qXfY+1fff650gummlvvVZ/7DslNtyX2/26ruj
1JVHwMp08D4B7B5JDROaoKeUe41mLM5KPA8bXoYXQQKBgQD5lZs0xLyozkiIeBsx
sem12K310NPj7VReg2fT+FRbpkQyuIcwNe+IHCvN4A0YCfksQNh4N7XE+az0iza4
3FOllWGkVlI0AtHo+jrzAOVMkbY+bO4G/m3mZvOSlYKgPh9FTneJ+weBpNb7tSbv
iBYh/R6s0hRm5M3Ziu0Q9OdveQ==
-----END PRIVATE KEY-----
"""
        cls.priv_key = parsePEMKey(priv_key, private=True)

        pub_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEBVfiJVWoXdfHHp3hqULGL
woyemG7eVmfKs5uEEk6Q66dcHbCDrD5EO7qU3CNWD3XjqBaToqQ73HQm2MTq/mjI
XeD+dX9uSbue1EfmAkMIANuwTOsi5/pXoY0zj7ZgJs20Z+cMwEDn02fvQDx78ePf
YkZQCUYx8h6v0vtbyRX/BDeazRES9zLAtGYHwXjTiiD1LtpQny+cBAXVEGnoDM+U
FVTQRwRnUFw89UHqCJffyfQAzsspj/x1M3LZ9pM68XTMQO2W1GcDFzO5f4zd0/kr
w6A+qFdsQX8kAHteT3UBEFtUTen63N/635jftLsFuBmfP4Ws/ZH3qaCUuaOD9QSQ
lwIDAQAB
-----END PUBLIC KEY-----
"""
        cls.pub_key = parsePEMKey(pub_key, public=True)

    def test_sanity(self):
        self.assertIsNotNone(self.priv_key)
        self.assertIsNotNone(self.pub_key)

        self.assertEqual(
            self.priv_key.d,
            bytesToNumber(a2b_hex(
                "0119c2b3f50a7ad6152679d7ff510958ac2d8ca6f0028592f332d55a1673"
                "6178a8e67f17e705ce300e3e87547251006013f974d0a3db49ef344ca5a2"
                "6a34c0450704d0e422e0ce23a69425c15fefb6f26e106eeff64cc8b9d744"
                "2e4da4e8c85008eaeb365859a2294fa3937bc26be56332e7d81e2c160ef6"
                "35cc528aa7be55e633a723dbc1e16ba29e52b29aef2f9e5654fdc0666bb0"
                "fc254acbe80e63874f0f5f020782e3c9dcfc2520d0c9c4a7b634e4503fbb"
                "493e1aafeeb3f88bd7a13398725dae6fe399e775cd5d4cf09fc838347c4c"
                "98dab1a4883cce620513615afaa10a63368e6d7b79df4166ab162739ef51"
                "5a4402ee1e0601c5a55bc71df0e30edf81")))

    def test_simple(self):
        msg = b'some long message'
        self.assertEqual(
            msg,
            self.priv_key.decrypt(self.pub_key.encrypt(msg)))

    def test_positive_11_bytes_long(self):
        # a valid ciphertext that decrypts to 11 byte long message
        ciphertext = a2b_hex(remove_whitespace("""
013300edbf0bb3571e59889f7ed76970bf6d57e1c89bbb6d1c3991d9df8e65ed
54b556d928da7d768facb395bbcc81e9f8573b45cf8195dbd85d83a59281cddf
4163aec11b53b4140053e3bd109f787a7c3cec31d535af1f50e0598d85d96d91
ea01913d07097d25af99c67464ebf2bb396fb28a9233e56f31f7e105d71a23e9
ef3b736d1e80e713d1691713df97334779552fc94b40dd733c7251bc522b673d
3ec9354af3dd4ad44fa71c0662213a57ada1d75149697d0eb55c053aaed5ffd0
b815832f454179519d3736fb4faf808416071db0d0f801aca8548311ee708c13
1f4be658b15f6b54256872c2903ac708bd43b017b073b5707bc84c2cd9da70e9
67
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = b'lorem ipsum'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_empty_message(self):
        ciphertext = a2b_hex(remove_whitespace("""
00cc52e83755a4526fea5e62450450638430a84a5878fd12c2a571f33c55729c
fab6e35c2e1703c452cff65731249460919aeb1b40084bdef573407851e48b3c
72923e48d5c4f3e80990c462bc291a3e635515636ab9ebeb317ca0d75b04b80c
17e2f4851f8929f72c9bea4ec4a6a1fbc5155837813567062d6b4b2a6b6e40be
545d25da39b08c52f3543e2f2cdfa314832dcbf475fcbb8d3565a64bb09b55f9
22e6ec6cd8bb5203a11e2fa0c1b383674c4f0b63acd78f3690e3a16ad1b71f6c
fe48c56533e2ae42b1393b2d156c2323272490a574ce4f14055249b6a34c3e08
d4a417039450910ec34bd5f08eb06078f51bdd6e50334ee64c9695a5bde52938
e3
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-1]))
        self.assertEqual(dec[-1:], b'\x00')

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, b"")

    def test_positive_11_bytes_long_with_null_padded_ciphertext(self):
        # a valid ciphertext that starts with a null byte, decrypts to 11 byte
        # long value
        ciphertext = a2b_hex(remove_whitespace("""
0002aadf846a329fadc6760980303dbd87bfadfa78c2015ce4d6c5782fd9d3f1
078bd3c0a2c5bfbdd1c024552e5054d98b5bcdc94e476dd280e64d6500893265
42ce7c61d4f1ab40004c2e6a88a883613568556a10f3f9edeab67ae8dddc1e6b
0831c2793d2715de943f7ce34c5c05d1b09f14431fde566d17e76c9feee90d86
a2c158616ec81dda0c642f58c0ba8fa4495843124a7235d46fb4069715a51bf7
10fd024259131ba94da73597ace494856c94e7a3ec261545793b0990279b15fa
91c7fd13dbfb1df2f221dab9fa9f7c1d21e48aa49f6aaecbabf5ee76dc6c2af2
317ffb4e303115386a97f8729afc3d0c89419669235f1a3a69570e0836c79fc1
62
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        plaintext = b'lorem ipsum'

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_empty(self):
        ciphertext = a2b_hex(remove_whitespace("""
0128a1f7837e53b21ee37f0b4d08c76180305d5d854a1bcf3885471610646795
f1e4c85ce7fce0f71ac3504598afdfc26792dea8ac55c7da10f96d26236ae652
b282459d679ec84847d523f07213e81d1c713fb159eded43112eab68b610e3f8
71d9c0009fde783ad7bcdca5568f7a86a716be6b96219c34b061f68718abad7c
947ed107097dc68341b865d73f2e857a345f5cf05c53bb2899d2895565009125
c7b5fe1c35a73c03bb0f59e7faf381c784988bb71194307ee9a8ac122990fabb
5cc1fd877aaa79039ac163d084c7ee1642aaf05befb9d7ed0e29558f11f0708c
8e83f804f92fd41310a6fd21d91c3ceb88ceee3e424a3fcdda57fe3abb8b7bae
7d
"""))

        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        # while the first byte is valid, it's because the modulus allows
        # only for two acceptable values (0 and 1) for the MSB
        self.assertEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-1:], b'\x00')

        plaintext = b''

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_max_length(self):
        ciphertext = a2b_hex(remove_whitespace("""
013a60aa202dedad2d9e78c0c99077ccc17b7d0533aeaf184dcb8c9a81ca4de5
715ada598d59b926606dcb005935421f6ebfd32e62802f0e2de8df08f1ae00e4
aced6ebf361a38df817c892309bd07c92c4f2f7be89f286f99711372e3dd959c
cb0a150b28578f29040b39ecf989c26eb77a3480c2d4d363b9563a70f0a0789c
c4300af1e600de39dae4a49335d35ac0156f5395ebebf35531c819c9cf498a97
e67ee2299d84564444f7bcd51f9f08d6bac0872439ad57eb9a8134dc665add1f
813d5031484c905a433c115bf889dc46ac672a8898fe235bf463b1b46345299b
6f100b48fa954fc262ce58e83f95955b321c1e86bbfe398b588dd5c75c2c6853
2b
"""))

        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:11],
            b'\x00\xaaG}\x8c\x02<jJ[\x7f')

        plaintext = a2b_hex(remove_whitespace("""
5c5345594cec69769af002af6513415a0848a4d45601c44b9e84b6e0a42c1356
cfc20604df8d334de53fafc6de2125f2eae2ec9864b0b0d03ef1539017ecf312
460cbb3c7c49fe124cf1becce8903f227ec85daaae73fe256acdf39f47b46c14
fbd289d7f9b9e22ee0e7c5d77cbbf22a2f9fbf4e26c5999a7b8335f6478912ed
fb77a373a82dabbc8233e585ea5ddfef3d0d872a4a007018005014a887349595
1210a4b90209b8286466030e56b1050ed600c777b4dbdb64f86516ef269a3ba7
7285f9be9afebcaad35226f7b3296932baf8dbfea3d77eb6520da203ffc06722
32761e2a8a05186181b8dd1f77f069f7af8de118aa18
"""))
        self.assertEqual(len(plaintext), numBytes(self.pub_key.n) - 2 - 8 - 1)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_zero_padded_ciphertext(self):
        ciphertext = a2b_hex(remove_whitespace("""
000a56cfd7abf21e2c65a28b8145fee663818b6cd218601e9e62bed7de5ac74c
eb07b435b305c99e3e286152036086b4a13eb26164f6f4bf79ac7d6c3fbcdcd7
4c6dc324c04949a0c88cbf616626cb171a4e333a0e124524b44f78e2d8100c03
e231791523b7d76db2d464e6b5e64244e04ad21128a5feb56092b4ceda35ebfb
84f7fafa8e1c098d9923d66e541b36307574db8912630fcf734af7bcd4118f1f
700804c5001a5950780188fc7862384fb3fc0708eaf3cb2b119177bb6928758f
a75e644d258ac02748dcae7a78ec6c8679598fa9deee4663f1efe27efe8bd155
72ff40676b95469aaa42eab4226d86c1160343255cce4fb7728f7349da27ed09
6b
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:3],
            b'\x00\x13\xb7')

        plaintext = a2b_hex(remove_whitespace("""
fc874af235e261083c2c
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_length_second_to_last_from_prf(self):
        # the last value from the PRF is 247, which is longer than the max
        # allowed length: 246, so it needs to select second to last: 52
        ciphertext = a2b_hex(remove_whitespace("""
011644d88f2955389b6d215fc3acd733265d82348fa15178d99e38fd2842030d
4e31d1ab15b0f00a80add1a9bfe112f9c42e827c487193c360dc5888c8c42d54
59b1f2c1952dca679ded08f190b6a78bbb6ea00438ebb8b03dc56e45cb36bee4
9a385c71fbf9bbcceda7b130ad6cee2106eff34dd224fba8e9990edf893ae52b
0910cdadf44bf29812a98bb9dc1638815112950bb9e7bad11c610d6406dd2d1c
36cddd639e024205a1a2bd82ec97059ef61b5226e3246ca672962194d1222cc0
32003fe34bf5ca0227f1c86439dcfba5203cf57099884276b0fbbf9b9cec9339
2673d8290a1a3452f3791c3881c9be6a1eef23841a8a5fde255cbbd3c4fc3382
7c
"""))

        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        kdk = calc_kdk(self.priv_key, ciphertext)

        lengths = calc_lengths(self.priv_key, kdk)
        max_len = numBytes(self.pub_key.n) - 1 - 1 - 8 - 1

        # the last_len is too long
        self.assertGreater(lengths[-1], max_len)
        self.assertEqual(lengths[-1], 247)

        # while second to last is short enough
        self.assertLessEqual(lengths[-2], max_len)
        self.assertEqual(52, lengths[-2])

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        #self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-3:], b'\xea\x67\xcb')

        plaintext = a2b_hex(remove_whitespace("""
9b9b496e44544456e70d9be86bd398dae00c7c05d6ea76c45d12f050b1c61c21
9b2fe47749451e44d96d11916f6ec4cf9eea67cb
"""))

        self.assertEqual(len(plaintext), 52)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_wrong_version_byte(self):
        # an otherwise correct plaintext, but with wrong first byte
        # (0x01 instead of 0x00), generates a random 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
002c9ddc36ba4cf0038692b2d3a1c61a4bb3786a97ce2e46a3ba74d03158aeef
456ce0f4db04dda3fe062268a1711250a18c69778a6280d88e133a16254e1f0e
30ce8dac9b57d2e39a2f7d7be3ee4e08aec2fdbe8dadad7fdbf442a29a8fb408
57407bf6be35596b8eefb5c2b3f58b894452c2dc54a6123a1a38d642e2375174
6597e08d71ac92704adc17803b19e131b4d1927881f43b0200e6f95658f559f9
12c889b4cd51862784364896cd6e8618f485a992f82997ad6a0917e32ae5872e
af850092b2d6c782ad35f487b79682333c1750c685d7d32ab3e1538f31dcaa5e
7d5d2825875242c83947308dcf63ba4bfff20334c9c140c837dbdbae7a8dee72
ff
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x01\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
f6d0f5b78082fe61c04674
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_wrong_type_byte(self):
        # an otherwise correct plaintext, but with wrong second byte
        # (0x01 instead of 0x02), generates a random 11 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
00c5d77826c1ab7a34d6390f9d342d5dbe848942e2618287952ba0350d7de672
6112e9cebc391a0fae1839e2bf168229e3e0d71d4161801509f1f28f6e1487ca
52df05c466b6b0a6fbbe57a3268a970610ec0beac39ec0fa67babce1ef2a86bf
77466dc127d7d0d2962c20e66593126f276863cd38dc6351428f884c1384f67c
ad0a0ffdbc2af16711fb68dc559b96b37b4f04cd133ffc7d79c43c42ca4948fa
895b9daeb853150c8a5169849b730cc77d68b0217d6c0e3dbf38d751a1998186
633418367e7576530566c23d6d4e0da9b038d0bb5169ce40133ea076472d0550
01f0135645940fd08ea44269af2604c8b1ba225053d6db9ab43577689401bdc0
f3
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x01')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = a2b_hex(remove_whitespace("""
1ab287fcef3ff17067914d
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_negative_48_bytes_long_with_null_padded_ciphertext(self):
        # an invalid ciphertext, with a zero byte in first byte of
        # padding string, decrypts to a random 11 byte long synthethic
        # plaintext
        ciphertext = a2b_hex(remove_whitespace("""
011e24da411e182d85e7c350a7dbff898c3e17bee1573fe3d0c0d3be53a384a6
5d597d52247e56d10b01cf1a51533e47c37f38bc62490e449b5f4ea35aec422a
63142c95da26e800e14504ce704edc7e38faaff697b74814c14d19f7f6f4d942
c1db61eca70266748ed83195bffa2eb85f49047a7bc7aae7f927ff445f15136b
28b4cad396312ae09a62ef894688ad50bc53d6977236b76d30c9bb2dacd0d583
00f2b3dc69a7c3212c6dcf6db583c59d94e7550ecc871991139259a9a0014516
35c777c7ac46db113a2460f157f9f830c186f0a0c47ca3012c8d309bea899852
febe76b87874292b8230be9de5c88fb94a0f19b2df71ca1efeb5f772b2d9b380
16
"""))

        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertEqual(dec[-12:-11], b'\x00')
        self.assertNotEqual(dec[-2:], b'\xfc\xce')

        plaintext = a2b_hex(remove_whitespace("""
5659f49338cfcd423dfcce
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_null_byte_at_eight_byte_of_padding(self):
        # an otherwise correct plaintext, but with a null byte on tenth
        # position (eight byte of padding), generates a random 11 byte long
        # plaintext
        ciphertext = a2b_hex(remove_whitespace("""
014b47d00714b92e98eacd73b07816ef530f8355fca68de6ba56828afab9d43b
96fcb11bee0e900e966a51705b95e82599f3df202d51d520c96adf32e1c0758a
7e0a8694699af8cfd9ed2850678f70e952f029a4b461ac8a8e049ef9ffc483eb
dc9a525bae3ddf8d69f8f711d30135fd9cce0c3d09d1a75c5b837d9f0d86827a
5f9edccd56af835572ba099a44a69277f31999753cd9887fe46ae7c7eb98d589
4692847179dac0ba305ed584f2887f7a6e88c843e6f0d4e99ffdcf51e2661983
01dab2bcb7b07944207c71a89f1449f3690cf09b9f15a5588a2c16d18ef43787
6285e9d04fd01ff30dea46a3eb17151e63b784548f1c65eeb08bec9901b93534
32
"""))

        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:9]))
        self.assertEqual(dec[9:10], b'\x00')
        self.assertTrue(all(i != 0 for i in dec[10:-12]))
        self.assertEqual(dec[-12:-11], b'\x00')
        self.assertNotEqual(dec[-2:], b'\x86\x57')

        plaintext = a2b_hex(remove_whitespace("""
c917a56bd800b8d9578657
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long_missing_null_separator(self):
        # an otherwise correct plaintext, but with missing zero separator
        # decrypts to 11 byte random synthethic plaintext
        ciphertext = a2b_hex(remove_whitespace("""
01541f0012b2dfd2d2b91cd22570dd577af0d27c29baa4d7a3cec2ddf8cdb957
257d8d436455d331e35730d1df7058cbb01649beb236154858843e2e14ae54fd
53496883163b8cb30fea540778726453204a846b04535878bebe9e60f8783b77
e5dfd4d346cd688aa2ee9e0ba9ac2bfd16005de994ea4a9c40adbafcf79dac48
59480a8e6e6849077b07f5e3dce8b97f678fc4b1da7e72004cfae36f01cb23f6
9180a46e3b9488f3b595e83510c9c4b298c953971d82610562976271e756f97e
f317b440271be9847178a482098447516ea29bd599592dbf22e35c91f8e2155b
d2f6289bac31c4c608b80bc208608a17cc45f7cff774549782882cf72baf0feb
2f
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:]))

        plaintext = a2b_hex(remove_whitespace("""
a4e88815652839f2482a8f
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_11_bytes_long_with_double_null_padded_ciphertext(self):
        # a valid ciphertext that starts with two null bytes, decrypts to
        # 11 byte long value
        ciphertext = a2b_hex(remove_whitespace("""
0000f36da3b72d8ff6ded74e7efd08c01908f3f5f0de7b55eab92b5f875190809c39d4162e1e
6649618f854fd84aeab03970d16bb814e999852c06de38d82b95c0f32e2a7b5714021fe30338
9be9c0eac24c90a6b7210f929d390fabf903d44e04110bb7a7fd6c383c275804721efa6d7c93
aa64c0bb2b18d97c5220a846c66a4895ae52adddbe2a9996825e013585adcec4b32ba61d7827
37bd343e5fabd68e8a95b8b1340318559860792dd70dffbe05a1052b54cbfb48cfa7bb3c19ce
a52076bddac5c25ee276f153a610f6d06ed696d192d8ae4507ffae4e5bdda10a625d6b67f32f
7cffcd48dee2431fe66f6105f9d17e611cdcc674868e81692a360f4052"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        plaintext = b'lorem ipsum'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_11_byte_long(self):
        # a random ciphertext that generates a fake 11 byte plaintext
        # and fails the padding check
        ciphertext = a2b_hex(remove_whitespace("""
00f910200830fc8fff478e99e145f1474b312e2512d0f90b8cef77f8001d09861688c156d1cb
af8a8957f7ebf35f724466952d0524cad48aad4fba1e45ce8ea27e8f3ba44131b7831b62d60c
0762661f4c1d1a88cd06263a259abf1ba9e6b0b172069afb86a7e88387726f8ab3adb30bfd6b
3f6be6d85d5dfd044e7ef052395474a9cbb1c3667a92780b43a22693015af6c513041bdaf87d
43b24ddd244e791eeaea1066e1f4917117b3a468e22e0f7358852bb981248de4d720add2d15d
ccba6280355935b67c96f9dcb6c419cc38ab9f6fba2d649ef2066e0c34c9f788ae49babd9025
fa85b21113e56ce4f43aa134c512b030dd7ac7ce82e76f0be9ce09ebca"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-12:-11], b'\x00')

        plaintext = a2b_hex(remove_whitespace("1189b6f5498fd6df532b00"))

        self.assertEqual(len(plaintext), 11)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'lorem ipsum')
        self.assertEqual(msg, plaintext)

    def test_with_ciphertext_length_from_third_prf_value(self):
        # malformed plaintext that generates a fake plaintext of length
        # specified by 3rd length from the end of PRF output
        ciphertext = a2b_hex(remove_whitespace("""
00b26f6404b82649629f2704494282443776929122e279a9cf30b0c6fe8122a0a9042870d97c
c8ef65490fe58f031eb2442352191f5fbc311026b5147d32df914599f38b825ebb824af0d63f
2d541a245c5775d1c4b78630e4996cc5fe413d38455a776cf4edcc0aa7fccb31c584d60502ed
2b77398f536e137ff7ba6430e9258e21c2db5b82f5380f566876110ac4c759178900fbad7ab7
0ea07b1daf7a1639cbb4196543a6cbe8271f35dddb8120304f6eef83059e1c5c5678710f904a
6d760c4d1d8ad076be17904b9e69910040b47914a0176fb7eea0c06444a6c4b86d674d19a556
a1de5490373cb01ce31bbd15a5633362d3d2cd7d4af1b4c5121288b894"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertEqual(dec[-2:], b'\xc8\xfa')

        plaintext = b'\x42'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)


class TestRSA3072Decrypt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        priv_key = """
-----BEGIN PRIVATE KEY-----
MIIG/gIBADANBgkqhkiG9w0BAQEFAASCBugwggbkAgEAAoIBgQCv1xyq1en1uMbD
ZwcKR/Gdfmau3hilsnQfs8TTNDRWBpKi2QnvaIjsYC/2uTryWO50MDwwGvzU7b7E
MxHdyN2/AN2744bTO40OIrG0STbcSJhxuFI3s0znR62P2wxOTR2qeq3wc4XFyHMs
y31aSeLlDIg8fXrBDtanTZrJDfkSmQWhfUoIchD8eLbQSx65aUgsEabut5xQ5bFv
PyVPdXFSiy8XFquBbW7KBye96pgFkylzDrjDPOcdYd1Kw5O2JW4HrB0STwIA0cPg
Wkwbx/HtL8g+Vxmc/lkIsQCH4n+9l9LCQhRhnHFHyPvvyjm8JWdipoI1MffiNNaO
rnoNn68Q3RXpUjeAx9WuWAlK1SWpBjtMM/leEAbaLrEtN0NolJXB8gI+QHNTxes+
TKHEjP+BoQkA0Ugg64Aa9PGllsS5zppTH8+KVNn/1yQli27sIBCN9v39dtSuA7p+
pZjcsOSigISVhyhvTX8lbOheXrVnmx2swfkJVkm3Ll+gcq6wA3kCAwEAAQKCAYAl
F+rLOv70v/rmA5jfmVel0qFUqDNo2OFYQrL1nuCfeRl70u8emt2vh4b2tBJ0R0Be
MEKyHy9Qt6pzdxaAw7vLbCJaXV/2tWxHHBiCoKM7CvFlo+1sJJ3HeD5rx1isN+ZX
LTP+MlB47ZUmUPLrlgSQLvmaURoRGdE8T8mkOhddzfv7GhQA/hcJO2nNPNuJX2VD
LqIZX5BRHHM2tYpoXaz/La9MXpLlZbFmWuYOUSuqmWW4CNX/EZzrfNaSy/kgBnr6
zYCfZr5wbaJoEKx5DbFWyUjm/lgbyYSRV/TaST86ZLDG4RngMbEH+ENs4pFgtFi4
+fEJX96xkmM4T/U4dVe8TxC0A03oQXA7rSwedpwjhT62MKNtEGHdRuKmu690Opfw
syw29QwaNyLe86OU2RwuB4vwnXlezeXla4IC+XQCb3X8Vumg3WqI8ufLeO8SmMxs
ZSB8pFvTcYiAe0/NseYN2OW4Vkj7fvqLb91Ejzl0Go2YCf4WOvPeRbrCSlqEHIEC
gcEA5KPYMNc+izHGguJ0/8n9EqwxPS3QUT1QVw2360di/qGT57tUC5SpSl3ddCrP
c/XeucrjG9I6xWC7J5T9aCYfggP1cZKCkE9GHqzuLOfgoAl6p8jbq9M/G/JpkSoH
gnFPqTtJ6sQ26z3nNKfW/9/YwsFDXoQ/xwn5BI5UKhl8SFQr6yuF6tD15kqmPQ7A
FSs/hWEt3Ka/3qvzF11ZfUBWPg4GLZHLAoiACC/p+PCRvb3aMW7rHoWMpE0rAorp
zeOpAoHBAMThzQ7PQphhXh94m6feIv1QlK9K0awpUO6WMDhaIECaKAxlOKL+7QMU
SOJuItZwk6cfncdOvRq8DpzoPWcLAnarHIWsc03Yv5x0zH/svXMtHXX4ie9GCkgZ
ul4bAd4jMlVRgbdvqWVEkxmKYG8Ayv2KkzVuRW8iO3Ub1bXKl64rObp3+3wXTILs
AhhlYNXie/GKJjzCEtnMZrAdHaJnPyl9TBvtRFtO/F2wYTbsqr2Cy1TQ/MQmmdTW
CgInv+ADUQKBwEDzDkHpkznFXQfnPqc/AOYiBibD8e5yBXWFTx7F+6grzDFC9MAJ
bgHTIkqSsrXVPXz31oYbtVhGf0PiPg4s7jxn1Xx6yx4ldtzV8R7Oi+/KYY5yL3zj
GIVe2oBDOTjj6WZAkmHfdV5kCl7Z4uhy9Ud10SZzWQ64lYWmzN/ct4Jwbr1ycqte
ysutnwWvP/+Ddpr0HSwWLmEZ5YdYnEhJU3ZzU2v0g3/nuL8apVNzO2N0IBx0ztOv
ymEODs69GWfEaQKBwQC5iEwUG66XKJJpN9//dm8kpg4njms+QQUagP/Z6tyf5GW/
IJgZygASOchhUQaVbCtIf5vQ2VuNWRCwPo62jwJ4T9GmCpfyEUKoLs0T9EWnxykP
JfLeP/OqdExTKEI/Uo25JwEFmz1XyCKTG/q6QFYKTc9ht5PJIcpEFsHy+YKsx+Ez
3qNoEhCxA7UJxmdVx4OjX9uewAjBpERUzGtDwuYbtA7H9nTHUwyxQWirOKXBxwLT
38mDExk+H6H42/qOILECgcEA4SpCAUB9J1HJrrQssfnmrzTc1EUxqa4qI9tUkvPC
Ip9uM6KKimZA5L8vHGojN4xeVhXg6xK/FOgbuZxM4VG1TmEoIr63yp5BClr92wym
IeWXACudHIGMhWAvmUUpGkdQYuxq9T9PUgea2BrFmjfZ1e9wCHX6d0IdUHBsdM4X
hyicD6D5SynhtlJJafmdTigiLO9JWkbtIZ7QaeB3Ef1Sx2pu/NyKnUQp4dFNmscg
RiYH7HQtpEgHd3Bk2J0rdOQr
-----END PRIVATE KEY-----
"""
        cls.priv_key = parsePEMKey(priv_key, private=True)

        pub_key = """
-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAr9ccqtXp9bjGw2cHCkfx
nX5mrt4YpbJ0H7PE0zQ0VgaSotkJ72iI7GAv9rk68ljudDA8MBr81O2+xDMR3cjd
vwDdu+OG0zuNDiKxtEk23EiYcbhSN7NM50etj9sMTk0dqnqt8HOFxchzLMt9Wkni
5QyIPH16wQ7Wp02ayQ35EpkFoX1KCHIQ/Hi20EseuWlILBGm7recUOWxbz8lT3Vx
UosvFxargW1uygcnveqYBZMpcw64wzznHWHdSsOTtiVuB6wdEk8CANHD4FpMG8fx
7S/IPlcZnP5ZCLEAh+J/vZfSwkIUYZxxR8j778o5vCVnYqaCNTH34jTWjq56DZ+v
EN0V6VI3gMfVrlgJStUlqQY7TDP5XhAG2i6xLTdDaJSVwfICPkBzU8XrPkyhxIz/
gaEJANFIIOuAGvTxpZbEuc6aUx/PilTZ/9ckJYtu7CAQjfb9/XbUrgO6fqWY3LDk
ooCElYcob01/JWzoXl61Z5sdrMH5CVZJty5foHKusAN5AgMBAAE=
-----END PUBLIC KEY-----"""
        cls.pub_key = parsePEMKey(pub_key, public=True)

    def test_sanity(self):
        self.assertIsNotNone(self.priv_key)
        self.assertIsNotNone(self.pub_key)

        self.assertEqual(
            self.priv_key.d,
            bytesToNumber(a2b_hex(
                "2517eacb3afef4bffae60398df9957a5d2a154a83368d8e15842b2f59ee0"
                "9f79197bd2ef1e9addaf8786f6b4127447405e3042b21f2f50b7aa737716"
                "80c3bbcb6c225a5d5ff6b56c471c1882a0a33b0af165a3ed6c249dc7783e"
                "6bc758ac37e6572d33fe325078ed952650f2eb9604902ef99a511a1119d1"
                "3c4fc9a43a175dcdfbfb1a1400fe17093b69cd3cdb895f65432ea2195f90"
                "511c7336b58a685dacff2daf4c5e92e565b1665ae60e512baa9965b808d5"
                "ff119ceb7cd692cbf920067afacd809f66be706da26810ac790db156c948"
                "e6fe581bc9849157f4da493f3a64b0c6e119e031b107f8436ce29160b458"
                "b8f9f1095fdeb19263384ff5387557bc4f10b4034de841703bad2c1e769c"
                "23853eb630a36d1061dd46e2a6bbaf743a97f0b32c36f50c1a3722def3a3"
                "94d91c2e078bf09d795ecde5e56b8202f974026f75fc56e9a0dd6a88f2e7"
                "cb78ef1298cc6c65207ca45bd37188807b4fcdb1e60dd8e5b85648fb7efa"
                "8b6fdd448f39741a8d9809fe163af3de45bac24a5a841c81")))

    def test_simple(self):
        msg = b'some long message'
        self.assertEqual(
            msg,
            self.priv_key.decrypt(self.pub_key.encrypt(msg)))

    def test_simple_max_len(self):
        msg = b's' * (numBytes(self.pub_key.n)-2-8-1)
        self.assertEqual(
            msg,
            self.priv_key.decrypt(self.pub_key.encrypt(msg)))

    def test_simple_with_empty(self):
        self.assertEqual(
            b'',
            self.priv_key.decrypt(self.pub_key.encrypt(b'')))

    def test_positive_9_bytes_long(self):
        ciphertext = a2b_hex(remove_whitespace("""
6c60845a854b4571f678941ae35a2ac03f67c21e21146f9db1f2306be9f13645
3b86ad55647d4f7b5c9e62197aaff0c0e40a3b54c4cde14e774b1c5959b6c2a2
302896ffae1f73b00b862a20ff4304fe06cea7ff30ecb3773ca9af27a0b54547
350d7c07dfb0a39629c7e71e83fc5af9b2adbaf898e037f1de696a3f328cf45a
f7ec9aff7173854087fb8fbf34be981efbd8493f9438d1b2ba2a86af082662aa
46ae9adfbec51e5f3d9550a4dd1dcb7c8969c9587a6edc82a8cabbc785c40d9f
bd12064559fb769450ac3e47e87bc046148130d7eaa843e4b3ccef3675d06305
00803cb7ffee3882378c1a404e850c3e20707bb745e42b13c18786c4976076ed
9fa8fd0ff15e571bef02cbbe2f90c908ac3734a433b73e778d4d17fcc28f4918
5ebc6e8536a06d293202d94496453bfdf1c2c7833a3f99fa38ca8a81f42eaa52
9d603b890308a319c0ab63a35ff8ebac965f6278f5a7e5d622be5d5fe55f0ca3
ec993d55430d2bf59c5d3e860e90c16d91a04596f6fdf60d89ed95d88c036dde
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-10]))
        self.assertEqual(dec[-10:], b'\x00forty two')

        plaintext = b'forty two'

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_empty_message(self):
        ciphertext = a2b_hex(remove_whitespace("""
4a454e0dbba01df544fd2fec0099ffd533301e1a4481597f83b8587ff638c029
ab434c59ce72bc4b13d0d4901945ad8cef4ef913626b09c9cad69336a9e409e8
5f59b0d60df25267443009e8e53b4aeed87c5301649db5f7b38d688850f5a408
b1c6608af1428f5e8b9262a8638cf89c28babf7df6d3d55101ff18ebf1bdf3c9
2e66b5ca279f6f4f759d4163f42e49bd836474ca3d48f4a40a5a2974e64c99d2
ee282e1b089aa6b360c4c815f743dda33ac12dfb0fe7a2653d753ee5cd8a4129
790ca888767f4128d61340bdecc579c3f9f36b1b256b51c1a66c46149f963bc8
fd0771ad2cb4b23054f5cc5fcf5534bc97de55bcc831894baaca7c40d46e056a
836523c52a84de3d7642ff4ce02f508b7ca1f485a028ca34f4c57417023cb724
87ee5fa60fc9caadf29b3fe3ef632abf89baae921fd43ca275b3026e286720f2
3422203eec63a9b737f9d18987736abf241c46b748a60f68a8dddfc9664312b3
6ec52b8a7ce8060b830a4de5f2475e14ed0570c631d608935e75da9b091084db
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-1]))
        self.assertEqual(dec[-1:], b'\x00')

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, b"")

    def test_positive_9_bytes_long_with_null_padded_ciphertext(self):
        # a valid ciphertext that starts with a null byte and decrypts to
        # 9 byte long value
        ciphertext = a2b_hex(remove_whitespace("""
00f4d565a3286784dbb85327db8807ae557ead229f92aba945cecda5225f606a
7d6130edeeb6f26724d1eff1110f9eb18dc3248140ee3837e6688391e78796c5
26791384f045e21b6b853fb6342a11f309eb77962f37ce23925af600847fbd30
e6e07e57de50b606e6b7f288cc777c1a6834f27e6edace508452128916eef778
8c8bb227e3548c6a761cc4e9dd1a3584176dc053ba3500adb1d5e1611291654f
12dfc5722832f635db3002d73f9defc310ace62c63868d341619c7ee15b20243
b3371e05078e11219770c701d9f341af35df1bc729de294825ff2e416aa11526
612852777eb131f9c45151eb144980d70608d2fc4043477368369aa0fe487a48
bd57e66b00c3c58f941549f5ec050fca64449debe7a0c4ac51e55cb71620a703
12aa4bd85fac1410c9c7f9d6ec610b7d11bf8faeffa20255d1a1bead9297d0aa
8765cd2805847d639bc439f4a6c896e2008f746f9590ff4596de5ddde000ed66
6c452c978043ff4298461eb5a26d5e63d821438627f91201924bf7f2aeee1727
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'forty two'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_positive_9_bytes_long_with_double_null_padded_ciphertext(self):
        # a valid ciphertext that starts with two null bytes and decrypts to
        # 9 byte long value
        ciphertext = a2b_hex(remove_whitespace("""
00001ec97ac981dfd9dcc7a7389fdfa9d361141dac80c23a060410d472c16094
e6cdffc0c3684d84aa402d7051dfccb2f6da33f66985d2a259f5b7fbf39ac537
e95c5b7050eb18844a0513abef812cc8e74a3c5240009e6e805dcadf532bc1a2
702d5acc9e585fad5b89d461fcc1397351cdce35171523758b171dc041f412e4
2966de7f94856477356d06f2a6b40e3ff0547562a4d91bbf1338e9e049facbee
8b20171164505468cd308997447d3dc4b0acb49e7d368fedd8c734251f30a834
91d2506f3f87318cc118823244a393dc7c5c739a2733d93e1b13db6840a94299
47357f47b23fbe39b7d2d61e5ee26f9946c4632f6c4699e452f412a26641d475
1135400713cd56ec66f0370423d55d2af70f5e7ad0adea8e4a0d904a01e4ac27
2eba4af1a029dd53eb71f115bf31f7a6c8b19a6523adeecc0d4c3c107575e385
72a8f8474ccad163e46e2e8b08111132aa97a16fb588c9b7e37b3b3d7490381f
3c55d1a9869a0fd42cd86fed59ecec78cb6b2dfd06a497f5afe3419691314ba0
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'forty two'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_with_zero_length(self):
        # and invalid ciphertext that generates a synthethic plaintext
        # that's zero bytes in length
        ciphertext = a2b_hex(remove_whitespace("""
5e956cd9652f4a2ece902931013e09662b6a9257ad1e987fb75f73a0606df2a4
b04789770820c2e02322c4e826f767bd895734a01e20609c3be4517a7a2a589e
a1cdc137beb73eb38dac781b52e863de9620f79f9b90fd5b953651fcbfef4a9f
1cc07421d511a87dd6942caab6a5a0f4df473e62defb529a7de1509ab99c596e
1dff1320402298d8be73a896cc86c38ae3f2f576e9ea70cc28ad575cb0f854f0
be43186baa9c18e29c47c6ca77135db79c811231b7c1730955887d321fdc0656
8382b86643cf089b10e35ab23e827d2e5aa7b4e99ff2e914f302351819eb4d16
93243b35f8bf1d42d08f8ec4acafa35f747a4a975a28643ec630d8e4fa5be59d
81995660a14bb64c1fea5146d6b11f92da6a3956dd5cb5e0d747cf2ea23f8161
7769185336263d46ef4c144b754de62a6337342d6c85a95f19f015724546ee3f
c4823eca603dbc1dc01c2d5ed50bd72d8e96df2dc048edde0081284068283fc5
e73a6139851abf2f29977d0b3d160c883a42a37efba1be05c1a0b1741d7ddf59
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(b'', msg)

    def test_negative_with_max_len(self):
        # an invalid ciphertext that generates a plaintext of maximum size
        # for this key size
        ciphertext = a2b_hex(remove_whitespace("""
1715065322522dff85049800f6a29ab5f98c465020467414b2a44127fe9446da
47fa18047900f99afe67c2df6f50160bb8e90bff296610fde632b3859d4d0d2e
644f23835028c46cca01b84b88231d7e03154edec6627bcba23de76740d83985
1fa12d74c8f92e540c73fe837b91b7d699b311997d5f0f7864c486d499c3a79c
111faaacbe4799597a25066c6200215c3d158f3817c1aa57f18bdaad0be1658d
a9da93f5cc6c3c4dd72788af57adbb6a0c26f42d32d95b8a4f95e8c6feb2f8a5
d53b19a50a0b7cbc25e055ad03e5ace8f3f7db13e57759f67b65d143f08cca15
992c6b2aae643390483de111c2988d4e76b42596266005103c8de6044fb7398e
b3c28a864fa672de5fd8774510ff45e05969a11a4c7d3f343e331190d2dcf24f
b9154ba904dc94af98afc5774a9617d0418fe6d13f8245c7d7626c176138dd69
8a23547c25f27c2b98ea4d8a45c7842b81888e4cc14e5b72e9cf91f56956c93d
bf2e5f44a8282a7813157fc481ff1371a0f66b31797e81ebdb09a673d4db96d6
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')

        plaintext = a2b_hex(remove_whitespace("""
7b036fcd6243900e4236c894e2462c17738acc87e01a76f4d95cb9a328d9acde
81650283b8e8f60a217e3bdee835c7b222ad4c85d0acdb9a309bd2a754609a65
dec50f3aa04c6d5891034566b9563d42668ede1f8992b17753a2132e28970584
e255efc8b45a41c5dbd7567f014acec5fe6fdb6d484790360a913ebb9defcd74
ff377f2a8ba46d2ed85f733c9a3da08eb57ecedfafda806778f03c66b2c5d287
4cec1c291b2d49eb194c7b5d0dd2908ae90f4843268a2c45563092ade08acb6a
b481a08176102fc803fbb2f8ad11b0e1531bd37df543498daf180b12017f4d4d
426ca29b4161075534bfb914968088a9d13785d0adc0e2580d3548494b2a9e91
605f2b27e6cc701c796f0de7c6f471f6ab6cb9272a1ed637ca32a60d117505d8
2af3c1336104afb537d01a8f70b510e1eebf4869cb976c419473795a66c7f5e6
e20a8094b1bb603a74330c537c5c0698c31538bd2e138c1275a1bdf24c5fa8ab
3b7b526324e7918a382d1363b3d463764222150e04
"""))
        self.assertEqual(len(plaintext), 373)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_zero_padded_ciphertext(self):
        ciphertext = a2b_hex(remove_whitespace("""
00128e116c0d348217c1d5756611be833caec3bd19f3d2ed383c4523ef3d8a5c
d1130bdb3fcd3ba1c0265322fc98c767b3b971054f5e3067a32b4878bbf7e17d
b80a855427e2e7d2ec26294b79edbb6352c7812270040e3cbaf560de1486171d
a649af786551ae0e5b6ef1fa1e22196c1c3039a50cfe09620da09716e75e9a9b
5ad164953c5a7e48f77ef9e0f59e962cf3985dc572ded966e8241632a9a5a420
3500a50d70491d80846b72019c456bfbdf7f15f740af0c2ef2a46787c54dcd90
a0e91257642f2c10b21052024b1d28ad14d78c0d9702a14b9ab9552f023bfb71
6f9c9a1f691959057f52b197086fb9bc24d45e2b063ffb235b54d3ab7575c7f3
e411398ddb30945c15f3f5d5ebbe302f22f60047d139d402f5b8a959421d1946
cf748c84065c5d0f0302f7ade6335014ab4467698ad827684d2bdeeb4757d276
f131340438506473f271c3fe24ca58e1c60dcc17aff8b0373637d897f627ea57
1da148a81d399ced9d65a4564bb6d23fbf4c14674d7551283a4293de51a1516a
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:3],
            b'\x16\x71\x75')

        plaintext = a2b_hex(remove_whitespace("""
732f025d1adea74649b4
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, plaintext)

    def test_negative_with_max_len_plus_one_in_first_value_from_prf(self):
        # an invalid ciphertext that generates last length that's one byte
        # too long for the key size, so the second to last value needs to get
        # used
        ciphertext = a2b_hex(remove_whitespace("""
7db0390d75fcf9d4c59cf27b264190d856da9abd11e92334d0e5f71005cfed86
5a711dfa28b791188374b61916dbc11339bf14b06f5f3f68c206c5607380e13d
a3129bfb744157e1527dd6fdf6651248b028a496ae1b97702d44706043cdaa7a
59c0f41367303f21f268968bf3bd2904db3ae5239b55f8b438d93d7db9d1666c
071c0857e2ec37757463769c54e51f052b2a71b04c2869e9e7049a1037b84292
06c99726f07289bac18363e7eb2a5b417f47c37a55090cda676517b3549c873f
2fe95da9681752ec9864b069089a2ed2f340c8b04ee00079055a817a3355b46a
c7dc00d17f4504ccfbcfcadb0c04cb6b22069e179385ae1eafabad5521bac2b8
a8ee1dfff59a22eb3fdacfc87175d10d7894cfd869d056057dd9944b869c1784
fcc27f731bc46171d39570fbffbadf082d33f6352ecf44aca8d9478e53f5a5b7
c852b401e8f5f74da49da91e65bdc97765a9523b7a0885a6f8afe5759d58009f
bfa837472a968e6ae92026a5e0202a395483095302d6c3985b5f5831c521a271
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        kdk = calc_kdk(self.priv_key, ciphertext)

        lengths = calc_lengths(self.priv_key, kdk)
        max_len = numBytes(self.pub_key.n) - 1 - 1 - 8 - 1

        # the last_len is too long
        self.assertEqual(lengths[-1], max_len + 1)

        # while second to last is short enough
        self.assertLessEqual(lengths[-2], max_len)
        self.assertEqual(15, lengths[-2])

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')

        plaintext = a2b_hex(remove_whitespace("""
56a3bea054e01338be9b7d7957539c
"""))

        self.assertEqual(len(plaintext), 15)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_from_second_prf_value(self):
        # malformed plaintext that generates a fake plaintext of length
        # specified by 2nd to last value from PRF
        ciphertext = a2b_hex(remove_whitespace("""
758c215aa6acd61248062b88284bf43c13cb3b3d02410be4238607442f1c0216
706e21a03a2c10eb624a63322d854da195c017b76fea83e274fa371834dcd2f3
b7accf433fc212ad76c0bac366e1ed32e25b279f94129be7c64d6e162adc08cc
ebc0cfe8e926f01c33ab9c065f0e0ac83ae5137a4cb66702615ad68a35707d86
76d2740d7c1a954680c83980e19778ed11eed3a7c2dbdfc461a9bbef671c1bc0
0c882d361d29d5f80c42bdf5efec886c34138f83369c6933b2ac4e93e7642653
51b4a0083f040e14f511f09b22f96566138864e4e6ff24da4810095da98e0585
410951538ced2f757a277ff8e17172f06572c9024eeae503f176fd46eb6c5cd9
ba07af11cde31dccac12eb3a4249a7bfd3b19797ad1656984bfcbf6f74e8f99d
8f1ac420811f3d166d87f935ef15ae858cf9e72c8e2b547bf16c3fb09a8c9bf8
8fd2e5d38bf24ed610896131a84df76b9f920fe76d71fff938e9199f3b8cd0c1
1fd0201f9139d7673a871a9e7d4adc3bbe360c8813617cd60a90128fbe34c9d5
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-10:-9], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
043383c929060374ed
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_from_third_prf_value(self):
        # malformed plaintext that generates a fake plaintext of length
        # specified by 3rd to last value from PRF
        ciphertext = a2b_hex(remove_whitespace("""
7b22d5e62d287968c6622171a1f75db4b0fd15cdf3134a1895d235d56f8d8fe6
19f2bf4868174a91d7601a82975d2255190d28b869141d7c395f0b8c4e2be2b2
c1b4ffc12ce749a6f6803d4cfe7fba0a8d6949c04151f981c0d84592aa2ff25d
1bd3ce5d10cb03daca6b496c6ad40d30bfa8acdfd02cdb9326c4bdd93b949c9d
c46caa8f0e5f429785bce64136a429a3695ee674b647452bea1b0c6de9c5f1e8
760d5ef6d5a9cfff40457b023d3c233c1dcb323e7808103e73963b2eafc928c9
eeb0ee3294955415c1ddd9a1bb7e138fecd79a3cb89c57bd2305524624814aaf
0fd1acbf379f7f5b39421f12f115ba488d380586095bb53f174fae424fa4c8e3
b299709cd344b9f949b1ab57f1c645d7ed3c8f81d5594197355029fee8960970
ff59710dc0e5eb50ea6f4c3938e3f89ed7933023a2c2ddffaba07be147f68682
8bd7d520f300507ed6e71bdaee05570b27bc92741108ac2eb433f028e138dd6d
63067bc206ea2d826a7f41c0d613daed020f0f30f4e272e9618e0a8c39018a83
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-10:-9], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
70263fa6050534b9e0
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long(self):
        ciphertext = a2b_hex(remove_whitespace("""
5c8555f5cef627c15d37f85c7f5fd6e499264ea4b8e3f9112023aeb722eb38d8
eac2be3751fd5a3785ab7f2d59fa3728e5be8c3de78a67464e30b21ee23b5484
bb3cd06d0e1c6ad25649c8518165653eb80488bfb491b20c04897a6772f69292
222fc5ef50b5cf9efc6d60426a449b6c489569d48c83488df629d695653d409c
e49a795447fcec2c58a1a672e4a391401d428baaf781516e11e323d302fcf20f
6eab2b2dbe53a48c987e407c4d7e1cb41131329138313d330204173a4f3ff06c
6fadf970f0ed1005d0b27e35c3d11693e0429e272d583e57b2c58d24315c3978
56b34485dcb077665592b747f889d34febf2be8fce66c265fd9fc3575a6286a5
ce88b4b413a08efc57a07a8f57a999605a837b0542695c0d189e678b53662ecf
7c3d37d9dbeea585eebfaf79141118e06762c2381fe27ca6288edddc19fd67cd
64f16b46e06d8a59ac530f22cd83cc0bc4e37feb52015cbb2283043ccf5e78a4
eb7146827d7a466b66c8a4a4826c1bad68123a7f2d00fc1736525ff90c058f56
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-10:-9], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
257906ca6de8307728
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)


    def test_negative_9_bytes_long_wrong_version_byte(self):
        # an otherwise correct plaintext, but with wrong first byte
        # (0x01 instead of 0x00), generates a random 9 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
6db80adb5ff0a768caf1378ecc382a694e7d1bde2eff4ba12c48aaf794ded7a9
94a5b2b57acec20dbec4ae385c9dd531945c0f197a5496908725fc99d88601a1
7d3bb0b2d38d2c1c3100f39955a4cb3dbed5a38bf900f23d91e173640e4ec655
c84fdfe71fcdb12a386108fcf718c9b7af37d39703e882436224c877a2235e83
44fba6c951eb7e2a4d1d1de81fb463ac1b880f6cc0e59ade05c8ce35179ecd09
546731fc07b141d3d6b342a97ae747e61a9130f72d37ac5a2c30215b6cbd66c7
db893810df58b4c457b4b54f34428247d584e0fa71062446210db08254fb9ead
1ba1a393c724bd291f0cf1a7143f32df849051dc896d7d176fef3b57ab6dffd6
26d0c3044e9edb2e3d012ace202d2581df01bec7e9aa0727a6650dd373d374f0
bc0f4a611f8139dfe97d63e70c6188f4df5b672e47c51d8aa567097293fbff12
7c75ec690b43407578b73c85451710a0cece58fd497d7f7bd36a8a92783ef7dc
6265dff52aac8b70340b996508d39217f2783ce6fc91a1cc94bb2ac487b84f62
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid in precisely
        # one byte
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x01\x02')
        for val in dec[2:-10]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-10:], b'\x00forty two')

        plaintext = a2b_hex(remove_whitespace("""
6d8d3a094ff3afff4c
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_wrong_type_byte(self):
        # an otherwise correct plaintext, but with wrong second byte
        # (0x01 instead of 0x02), generates a random 9 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
417328c034458563079a4024817d0150340c34e25ae16dcad690623f702e5c74
8a6ebb3419ff48f486f83ba9df35c05efbd7f40613f0fc996c53706c30df6bba
6dcd4a40825f96133f3c21638a342bd4663dffbd0073980dac47f8c1dd8e97ce
1412e4f91f2a8adb1ac2b1071066efe8d718bbb88ca4a59bd61500e826f23652
55a409bece0f972df97c3a55e09289ef5fa815a2353ef393fd1aecfc888d611c
16aec532e5148be15ef1bf2834b8f75bb26db08b66d2baad6464f8439d1986b5
33813321dbb180080910f233bcc4dd784fb21871aef41be08b7bfad4ecc3b68f
228cb5317ac6ec1227bc7d0e452037ba918ee1da9fdb8393ae93b1e937a8d469
1a17871d5092d2384b6190a53df888f65b951b05ed4ad57fe4b0c6a47b5b22f3
2a7f23c1a234c9feb5d8713d949686760680da4db454f4acad972470033472b9
864d63e8d23eefc87ebcf464ecf33f67fbcdd48eab38c5292586b36aef5981ed
2fa07b2f9e23fc57d9eb71bfff4111c857e9fff23ceb31e72592e70c874b4936
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid in precisely
        # one byte
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x01')
        for val in dec[2:-10]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-10:], b'\x00forty two')

        plaintext = a2b_hex(remove_whitespace("""
c6ae80ffa80bc184b0
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_null_byte_in_first_byte_of_padding(self):
        # an otherwise correct plaintext, but with wrong third byte
        # (0x00 instead of non-zero), generates a random 9 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
8542c626fe533467acffcd4e617692244c9b5a3bf0a215c5d64891ced4bf4f95
91b4b2aedff9843057986d81631b0acb3704ec2180e5696e8bd15b217a0ec36d
2061b0e2182faa3d1c59bd3f9086a10077a3337a3f5da503ec3753535ffd25b8
37a12f2541afefd0cffb0224b8f874e4bed13949e105c075ed44e287c5ae03b1
55e06b90ed247d2c07f1ef3323e3508cce4e4074606c54172ad74d12f8c3a47f
654ad671104bf7681e5b061862747d9afd37e07d8e0e2291e01f14a95a1bb4cb
b47c304ef067595a3947ee2d722067e38a0f046f43ec29cac6a8801c6e3e9a23
31b1d45a7aa2c6af3205be382dd026e389614ee095665a611ab2e8dced2ee1c9
d08ac9de11aef5b3803fc9a9ce8231ec87b5fed386fb92ee3db995a89307bcba
844bd0a691c29ae51216e949dfc813133cb06a07265fd807bcb3377f6adb0a48
1d9b7f442003115895939773e6b95371c4febef29edae946fa245e7c50729e2e
558cfaad773d1fd5f67b457a6d9d17a847c6fcbdb103a86f35f228cefc06cea0
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid in precisely
        # one byte
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        for val in dec[3:-10]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-10:], b'\x00forty two')

        plaintext = a2b_hex(remove_whitespace("""
a8a9301daa01bb25c7
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_null_byte_in_eighth_byte_of_padding(self):
        # an otherwise correct plaintext, but with wrong tenth byte
        # (0x00 instead of non-zero), generates a random 9 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
449dfa237a70a99cb0351793ec8677882021c2aa743580bf6a0ea672055cffe8
303ac42855b1d1f3373aae6af09cb9074180fc963e9d1478a4f98b3b4861d3e7
f0aa8560cf603711f139db77667ca14ba3a1acdedfca9ef4603d6d7eb0645bfc
805304f9ad9d77d34762ce5cd84bd3ec9d35c30e3be72a1e8d355d5674a141b5
530659ad64ebb6082e6f73a80832ab6388912538914654d34602f4b3b1c78589
b4a5d964b2efcca1dc7004c41f6cafcb5a7159a7fc7c0398604d0edbd4c8f4f0
4067da6a153a05e7cbeea13b5ee412400ef7d4f3106f4798da707ec37a11286d
f2b7a204856d5ff773613fd1e453a7114b78e347d3e8078e1cb3276b3562486b
a630bf719697e0073a123c3e60ebb5c7a1ccff4279faffa2402bc1109f8d559d
6766e73591943dfcf25ba10c3762f02af85187799b8b4b135c3990793a6fd326
42f1557405ba55cc7cf7336a0e967073c5fa50743f9cc5e3017c172d9898d2af
83345e71b3e0c22ab791eacb6484a32ec60ebc226ec9deaee91b1a0560c2b571
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid in precisely
        # one byte
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        for val in dec[2:9]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[9], 0)
        for val in dec[10:-10]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-10:], b'\x00forty two')

        plaintext = a2b_hex(remove_whitespace("""
6c716fe01d44398018
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)

    def test_negative_9_bytes_long_missing_null_separator(self):
        # an otherwise correct plaintext, but with the null byte specifying
        # end of padding missing, generates a random 9 byte long plaintext
        ciphertext = a2b_hex(remove_whitespace("""
a7a5c99e50da48769ecb779d9abe86ef9ec8c38c6f43f17c7f2d7af608a4a1bd
6cf695b47e97c191c61fb5a27318d02f495a176b9fae5a55b5d3fabd1d8aae49
57e3879cb0c60f037724e11be5f30f08fc51c033731f14b44b414d11278cd3db
a7e1c8bfe208d2b2bb7ec36366dacb6c88b24cd79ab394adf19dbbc21dfa5788
bacbadc6a62f79cf54fd8cf585c615b5c0eb94c35aa9de25321c8ffefb8916bb
aa2697cb2dd82ee98939df9b6704cee77793edd2b4947d82e00e574966497073
6c59a84197bd72b5c71e36aae29cd39af6ac73a368edbc1ca792e1309f442aaf
cd77c992c88f8e4863149f221695cb7b0236e75b2339a02c4ea114854372c306
b9412d8eedb600a31532002f2cea07b4df963a093185e4607732e46d753b5409
74fb5a5c3f9432df22e85bb17611370966c5522fd23f2ad3484341ba7fd8885f
c8e6d379a611d13a2aca784fba2073208faad2137bf1979a0fa146c1880d4337
db3274269493bab44a1bcd0681f7227ffdf589c2e925ed9d36302509d1109ba4
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid in precisely
        # one byte
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        for val in dec[2:-10]:
            self.assertNotEqual(val, 0)
        self.assertEqual(dec[-10:], b'\x01forty two')

        plaintext = a2b_hex(remove_whitespace("""
aa2de6cde4e2442884
"""))

        self.assertEqual(len(plaintext), 9)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertNotEqual(msg, b'forty two')
        self.assertEqual(msg, plaintext)


class TestRSA4096Decrypt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        priv_key = """
-----BEGIN PRIVATE KEY-----
MIIJQQIBADANBgkqhkiG9w0BAQEFAASCCSswggknAgEAAoICAQCP3jlT5VxITxxC
Sq7JA99vOdMNsWBSloAaGC0650aOGSezhv550foWGyiU+Gixo3XzGcMGs7vaX8tF
oROlVw6yRzGAz+ERn6B8JeRojKJV4hWmrFa8EQfuJDPM6EXLb1X2u4wwDpwDs0IV
c4jUD6ekXTsNEFW0mjw7CkRLcnGXFUFDXj/J8pVveF5cxtFZi5+JwcE79MX+8TEH
8OAW9W11O9svcPFuzHUI0gv1BixcZIvVu0pzVcQpNeKv41ZZW20PNOpynI7JjOjC
f4ebGZx03y4i7jA2LpLznbjcmiT1Ge1a/NHS6BriA//9gCjcAvgdO/Sws7rEJLEH
JQ0gmMBuSt3yaQpOdrejmXNX2Cvz6ewQ16i4hiq8AramcyiRIVHjsfQJWMeirYX7
ZCsrCVRt0WGE9PPUxo/mDIZ3CpQ0IRwNxCwuJO35AqLtTUaFXhRW5l/W/hbVbaTj
yAmd2W57LCFjPh7S41zECRl6zuf7keGbad094Tkm8dr+/N47mAtP8C+Q2YBIEsxO
qYobVlAP/Rznsq6ScUyKagMdKby38EewybvOcN/g4fDbBs7a+Jdp1Y4cFT7ugTet
ig+yHJlJgjbQQYA8sjwAPeZRArmnMsOBvEG+F8tLIRmT9iIG7AV8cVdQ1c0xq2e+
bIZV6kq1pstAEcKJs2wS3hr3oI7dDQIDAQABAoICABUFM5wZ9XdNM8RN1CbjrXg7
WyZzha7bdYEaijVCiHEHpODatwDGmMM1GaNWfjmCOCAaYf/vL+HSwEj+pXexdiC/
PTDkbq6cA59QDATok2l3/JDbOlsFJAL8ACOOxm/YZxeDRJLa95mkzeGDfXj6hpSB
2LhqbBNUu7smn17krEsWXHBC65AOpR3h2Ou2Uu1B9L/0cs7XTzyWMgNGgv9nwaPw
6HAQkP4O2oS85+lXixC+0h2a3WBnph8dU+8+CKZKsO8ZXK39SPGS6IlOh9o2DkGX
QE7zPVEVUfxNTa7RyNeU/7SdHu0xY4glbHg2CwJGXskqsvBEemPhNopkM/xQxUDA
AoJ3HsNbpXsp+V4HjijdV47ncQBPr2O3Ln/V3nVqgJJ88MWqC3kfDMwtE+b8yLE3
RJ8Tqb+Rih0Zr/4AfRNlSZzzmUKbN39f9swLzv5BJMuBhbq2W/019xb+b+Jq/o5p
NgUKVImnvJ+Pm0tFaMHWKE3LHOib3o4D19bVHfkEXXeFwy2Dul/imDwOQqEu4Gei
3mkzIEEA2f4Tl17ta62kdNn73lgpdtEqE0DNq9yQpK7itxRjTlwGQShLzYJaD9bz
TIgx5H+0FIGO4yzO5BJelPSFNg646BpiZsKGPy9PhYhA2UKPvKwbYhdEub3pO4pu
aSn9WE6hFrtphmzrs0+DAoIBAQDJmfE5qhyZdUlhG4a6gCzirXlYRG0LESf5pqJT
IT7nfCV25j7ir3hXqVA3M4zXNDP0jtDUFUlmvs2Iwte4cvybmbnlCYYCaMvienq2
soT9S+wRWT1ituC+xg9w9JAdkrdm55A/r+ioxeAID1OKdlmOtGxyb9vusNvLM/xq
yjciOvx/hYzRTnVme2qVuCfxo3WgFneLmT3KgZqeKI4bklP5ZCiqmtWrVE5JV7FA
5yeuvqt5hpKwnYLCyWpyrX6ZiWW4NoZQEgT7nvyAxlJXsxibhXK0VLIJbFyFOyRF
XzHJblcyFKt2FEyqKY8Uo9vhFpm4YSU2/h4/BRpEbxZ60pPLAoIBAQC2sDpoWubg
FYJ76iZ0rLce+UnRw7fiySz73Pcirky7ohduawM83VuG6MlxYTgTrvNFKQxRt/kg
b9SZmqVj4TCdPG+rlbfh31nCs5o7tIXVwpXJYF6Zw+3XFcVQfs6yOKGED7kvcxlv
c0IogRY7VwL+2uUPY8P2pSubRh46ojCk2rBPnUvAOiywuVp/8ce4vWD4OE9qMGxL
tQCtWcNQc7IloopxD/6JxDvbi3AkLmhnZTwVQ1pvsTLxSftBeDMtBihwyYkzKp2q
LQ77z+ROQjxWNueGlJiyLiISy5OpfzftrEI7HbbRijFfIW1wpBLktjJc+V3TQpvw
81DfPWz7HSeHAoIBABbkhkH4ETtT2DtQtuHiwDYVYNwnGQLStelhhLlP4ybCMDbq
OmXfaxj5PwSls+6UHPo+ZXRP3n/uVsSa64gkdo7sy/E4PaF0aQKUye6JIxToVCw8
J/5Xqfm/3+0BuIPDL1ReI0E4JoFTxvbjVqc4fT75Of9cuGrIZo0SoC04PT6D2Dxa
2/zAnhA/H4FU4iRMXYUKSBTwF9YxFW+0Rz7WRPbi6sNExdKoxiMJ9DTciuMK/8nT
AEFSAZFA8feHwAKLWaOrfWEGSs6P5ThyTNNsoPS4GKhlnbn4NiFi7+F4x9yJzRkA
w9+qunHwOjEr0kIjIN2RGnq+LI0XdT4kJzdXRjUCggEAUs9hOmpyGwNFCXxjACJG
Q6EGiDIqiX9dh7FqyOqvV6Iq8t9JMW65jVa58U37SFjWZvQrZGN7ZuuqOBJ0g+jQ
y4VYrTOJjbZbjrkw4X176SByGz02xIaeqg9xSIKimQC4ng8uh0aqMe3SAGA7Ppy7
e+CnUimL66KFOLY4/6UDXcbPgtcvPixgk58BWdu0B5a4fOuxe9YFUO/0JZ/5u98l
0o9yJ7vzSmmMJIF5TL1IkA3AhXbpaJWvHNbHMK8Wq4MOE8oXCf14SGpyT0y2FY9K
oF305vk2mhX1VgW3om5LYM3jm75lX2g/5vpVDGkjM08vVxumHxwjab4xW3ARlWZq
wwKCAQBbs6Gt0843wVJcNkrQiOTLL8HewV8N9LNf3miAO4/2VgSYyO+Y8xjE/xyt
eQRE9ZKrqKb1L192w7vEgd7+a9vwoLlxeLbV7oUwG+gp+aVt5GNPW05mAgUynsEn
zNrdC+Ng9GkXzygYfky2b/ErNicJfQtoubfCSvcHL2R9Fk6dY3B9FdjkJvfjv/SL
se+aEl3AWJnAnpM3KtjY5qje+R/m6f5NkHvECiV/rCu0Bz8+gGpo4MlFKtsz27by
3NyzfWoQ0h6Fcz+AbrxqdMw3JRLoIRhhlC7XMnaCP2hphOd9exTRJYBvRSXTSyDY
q4gl5hM8H5F0iWcKq25nZYHamz7f
-----END PRIVATE KEY-----
"""
        cls.priv_key = parsePEMKey(priv_key, private=True)

        pub_key = """
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAj945U+VcSE8cQkquyQPf
bznTDbFgUpaAGhgtOudGjhkns4b+edH6FhsolPhosaN18xnDBrO72l/LRaETpVcO
skcxgM/hEZ+gfCXkaIyiVeIVpqxWvBEH7iQzzOhFy29V9ruMMA6cA7NCFXOI1A+n
pF07DRBVtJo8OwpES3JxlxVBQ14/yfKVb3heXMbRWYuficHBO/TF/vExB/DgFvVt
dTvbL3Dxbsx1CNIL9QYsXGSL1btKc1XEKTXir+NWWVttDzTqcpyOyYzown+Hmxmc
dN8uIu4wNi6S85243Jok9RntWvzR0uga4gP//YAo3AL4HTv0sLO6xCSxByUNIJjA
bkrd8mkKTna3o5lzV9gr8+nsENeouIYqvAK2pnMokSFR47H0CVjHoq2F+2QrKwlU
bdFhhPTz1MaP5gyGdwqUNCEcDcQsLiTt+QKi7U1GhV4UVuZf1v4W1W2k48gJndlu
eywhYz4e0uNcxAkZes7n+5Hhm2ndPeE5JvHa/vzeO5gLT/AvkNmASBLMTqmKG1ZQ
D/0c57KuknFMimoDHSm8t/BHsMm7znDf4OHw2wbO2viXadWOHBU+7oE3rYoPshyZ
SYI20EGAPLI8AD3mUQK5pzLDgbxBvhfLSyEZk/YiBuwFfHFXUNXNMatnvmyGVepK
tabLQBHCibNsEt4a96CO3Q0CAwEAAQ==
-----END PUBLIC KEY-----"""
        cls.pub_key = parsePEMKey(pub_key, public=True)


    def test_sanity(self):
        self.assertIsNotNone(self.priv_key)
        self.assertIsNotNone(self.pub_key)

        msg = b"message"
        self.assertEqual(msg, self.priv_key.decrypt(self.pub_key.encrypt(msg)))

    def test_normal_decrypt(self):
        ciphertext = a2b_hex(remove_whitespace("""
041f9bbe8372454ffadce0befc99ad4bd01cdbe016dffb5d0d84ee879e7ff64a
25dced4d504f48a14b700a34a1c148e4b4028eecc9158cf5e3469daad1dddb21
57b176dcf5716627aebd6072b965cfb67b42b149e88c0a8dc54703ec244637b3
039b80c06d1d4968aeb838f3afcd3dc675fc90736cf0f0adaba182e27a19a729
4cef500ed1fcca324c3ffa6ff02bd749a4a66f18da138d53ff549c4e6b3fff0b
9ee2029ea8293fcd72a03e1dee4445629979be7fd65e5dbe5e6e77ec2aa87879
a01c3e2502af0cc4bc04b637d17b175d92b4dcd70cfe83b6c1d4f91c61e911b8
1cb6d60b99146f17937d127054521b132acb9ca95cbc6f80cd926d709bd7219d
48ce7378e4416328a49be6c773dbdeb00ce23dc91f25f4807526cf4de8dd3fbb
13ae1011eefe3a2aad9982f6c9268883b4633057d119c97c1178aae671859af0
a488ab7b841c6583572d1261137a4292ba1c1caa4baf808be42075940d7e612e
fa56ac9a7ffff3e7dbf10b6193ea14c4841fc5c43e031a69ddbd79118ccd92b1
6a6ef66c7404c001ebc6402301a90248eb6562b7a2f549f52c058109dd5f2617
877719ad13e81d19425a4cd5cf9e56e8538f5cb09b6f7ab646910b8c2ff6bf8c
f17abdb4758bfba80df9f643950a6d4a8f60c6872700e5919d36503486667e43
28a6b74b774eb483a9922706baa7f456644781cc0d78add9024e28da2d5e9d81
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        plaintext = b'lorem ipsum'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_valid_empty(self):
        ciphertext = a2b_hex(remove_whitespace("""
31529676f990b750e8b742babe933346bd77610e7ea74a6b815bb06ee3c91a37
6848a4d8b148c2882d65ca0213e68600354b68b7790110ed744e34786fa5f7b7
03144a12f7f7a4d5402ef048f248fec83dede7f931bcb872054fd25cfe427984
0352f2c495bcb511cf20269d8177baba474e790a2d16b655c4e07b28ad6a61e8
1ce5db3845cb5395aa4affa413e3f1bdecf3fa0aa3073b40d23e9bb0aa7cf359
5bd73d1d38a2661d70a8e4ef525fd446f496ddbe5413657c06d51464977421e0
57387a92a5b9428d02d1a8fb0d50a1623e1b1d0685c371db24b63dd6a4aebf0e
31c637997ae26dbd3441b9f7dce164d948a156aee8c9dc4049286244c85178f7
b4f49d3ba0870f7c71f8f546a902a559fd860ed61e550c4143907d118a15f317
e9ccd84ce3893db372fff1d9a9e5182258d9f9d840a6b75b1618ce4999734d14
7f5334763c0b87ca1c8e57c6f923cff9c7107eea45cf5d4fae0ec0b94e892a6f
6790b07f9e24bff041620b1fb47bcefb956ba61949fea02db6ec785b4070e84f
390234d83d17dbf89819d5c6b52a488f36cd9f8d81e1811bbadbd6756b9ec5fb
dcc1d32728efc8ef4318463996c0f829f9064436580f9502af97b1e40c854b0e
f0a20da4368e5b94327b62c27a8a1cf6103bc780e06e5ee5232624fe5bee59fe
79a3956a7d782380a3398eab6d11f618fc2c698eb28a6029f846c378ecf2d102
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-1]))
        self.assertEqual(dec[-1:], b'\x00')

        plaintext = b''

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_valid_with_zero_padded_ciphertext(self):
        ciphertext = a2b_hex(remove_whitespace("""
00c40ab6440e544ced2c0bbd3f6db05fd0068eb8e9ed83099cf5843ea3d2cfd6
adf7ede1c61f1974a5696f503205346b51d7b00eca20432f0082abf2a3cd6743
3c5f860b32f1f6fe9985dcec65e7f19949999e142bc76ce5b2dcb80615d379e9
715ac24ef77fbbe3d969131c0f39666b3ad641fac669d53542ae9389d86f6f28
fe63ba272b1f6bd015b4187b6e2014fb74fc32bf4a2e48abfbfc0470956c7379
1c1d81db6c024f4d1cc81ba01be114b41ddb95572a832086c33fcaf90b32358b
5b13ef0bea74a6dd01d5c351a231d4e7d15d121cffff023e0c2bdac11c982fb2
419955a495e8dac3d84cbd8d71ac380072a02bb026ed61151f0d202b3133e603
0a2db7560ca926de3927f1ed578522edac441071498b4565fb0c8071886b79fc
9e8d8c14bec1d7a6106441c16e9b2bd3090dad1fe82d0e43f40b036f00506cea
36af61d5f10aac0d0591c12107ceb8999787e34943974025b9c47d16cb523a58
c5828da975fa74e431ace2dcf934e21613f877f65c67b729ca79ee25f27ea07a
74ff38c3b25bcaf22dfe2e9e5d0adecaa01d98d55b5cd0b20f80e672d1bedf4a
cda32184db0f5ce89dd64f538f038cbefb625347ef77a16ab9d48dbee9549f1c
8d55b5470a5c6693bec146f0190bbca5b93a66667150a661851add729b24dca7
8a1f051093ecd40a0ac43a593101f579597b7638065bdff4191bdc0cae12c052
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is valid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-12]))
        self.assertEqual(dec[-12:], b'\x00lorem ipsum')

        plaintext = b'lorem ipsum'

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_empty(self):
        ciphertext = a2b_hex(remove_whitespace("""
577d6457be536bf1fac80993f5f76e797607227a42e325deb246bf8bf475e1d1
819c5dfb6d288eb131ead32238b7a8796b76517e78f979b34f5c2272ae4d40e6
0b265ad3c897ecc4d26587c8ac32db431ed8d2996d64edadf7719baa4b4292b3
4e042f26693c90f04addffe8ba0e3c3f1cbabafbfd2e3a6bcd9203e9a1cebb1c
968caa73430556ea5743ecfa49edab656bfeadf7c114105f3e222fe60983d55b
c48cb738c5a307353281c573be6ffc69630185ae6de695c35fbf8cbc24b5590f
5e511adb68a38a37bc6dc74a5052e5063f20c30d2f331dafb07797f9e577cb3d
18280f318fe2a6116cef6846b7a8384663a5aaac32693b9b159f506d8812f76a
1ee405abb1e5e439a0aee4d1b51f435ea2d043fe4f4ef1a6ccf069201ceb7978
139eed579b01bcb5b4e525cce6b179f72fcb6aabbd916538d580ce3e1ed57a4d
3433efd826fffd75d8fdc43de69afab66dc32a4f4f81b14c0650a097709265e2
6b57f233008013b275e7b58817b02f4473a99bb48ec7d9562bc78d1f032340d3
083b762f19fb204be7f26d7ceef6c7ff712479a6cdf18123586b87c2751493f1
bb2585626b1aa486a2ec50a197728cf24d3968e6d9b9bdfedfda91db292abdef
fda2334c85fd359e65e7e662193b6feb5df6d70c7727880150c785d809ba3ffc
e3b2701aad313da60cd4affe85e85d32c4fe271b0b107e529a22cffbb01871c8
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-1:], b'\x00')

        plaintext = b''

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_max_length(self):
        ciphertext = a2b_hex(remove_whitespace("""
09be60b83b63aa1f2398c6ccd7ba602917dfffbc1a2ee01094221ef7140ba8b3
64b4979b7d068be084d34b70309bc48103d9e7dc76c042d1063ce6d7239d3542
ad511da821c6ad53dcaefdd9e950de889d1d462a5a8bcdda4e2ac579c0dc12ab
684a16a3c4075ec5062db79f95e5b436a8927fe7e3a795152cb6407faedf088a
e4531cca8482348a3c44267b1ea46fa3bfcb4754be735e434c4ef17b84f6fd6c
184e8c4adf91fbf00be6a6ff86351e6fd76c8929ef7fae14113370cbe6ba0181
ef6970855a2cfde5b366a44bf0575e7e5d5354676b5429a6916bb7065c234174
42150f8fa23a1ae284a27008980691eb886b693adb1bf4d38faae5037007900e
47124a695c67b51fe9e1e66153cb32fae0e7370151024fe49b2781e50ac5a31d
1c7de58923c0360ae61f4a3bcfd7839a104c23d95ddeb76bcaf2b1956f81c355
aeb11a46b48762baf072318727e56d4e682a3b71898d3725b00a334c94cb1adc
cea81525b28c2a1c2b82950b93786ea5b893ffe6dc0932a95b064c838d6f04ea
a8334f92b0dec8c7bbc1a5900d7e7680c24e66867ec2b837e30be18083c6fb2b
fc67ace569989171f05d312ce97307b477379837351e9199528e88671a93e558
68a577fb9eae76a2cbf3cc62c6aaabbee88cf6638012554ba92772e923fbe531
fe8aa2036ee7230954ffa24e802a399f531c8cad0a78262442c92089f06b06c7
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))
        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:4],
            b'\r\xfe\xa0t')

        plaintext = a2b_hex(remove_whitespace("""
7a57bf4c557abe6bdd45ed471260ec2749e66710b707ff4e4761738dbe2cdc19
267aec5070d2472f53ba0c86e8b607566c871b6c3de28772aa197e369fad293f
8218fd32178ecebe60cc7926e093bbdd629ed6a6a29b4a905eefe443f3621d89
582a41bac7d4f6b77f9c935681e892d17b2261151a4b4244506cfc49ba578b97
5840d88f637321d20c25950640d2b43aa660611cc07d016534324b84bada2244
85488af08a8d54af1698babccd76b87218b074987273dd3746eacd2dee8068d0
c4f5e8f219689d55deea3cccb86e52599cebf3777cab3bfc2da5ae31c9019973
9ba5d5e01816f8f8a21c7f6b6acdada8a2b2ab4f32502d6296a365267a768378
78d204a1b8cc5299708e9eb1b44d9663c75c9b8c17dd8f1a9f04109087e22329
769fcc5fa65506a0f6294d8bf4a362559c497a36b2a5c55ee12213bd9c42a2dc
0f6f35176e194641dcfbb334b13924e6883b4f68c88d016ecdc67bafdeff4b2e
4122777726e06b0e37642d42090be622288ce11a8af4261b5d186092002e7d71
cb43fc2182e4d341c610e6860904cbc526e74292aa1df81dd08d87b51a953c0b
e511346d604aa3a8e87f943db3e951a69cc4dcd1b996d3d8ab595aa9b7ca591a
e2e9b49798a9b98aa1c1c233f938937c88ad675e6297f36ba0fb161a8b42e9ee
9a98d8b781165ed75d30cc55d88e6df5c688c32390
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(len(msg), numBytes(self.pub_key.n) - 1 - 1 - 8 - 1)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_zero_padded_ciphertext(self):
        ciphertext = a2b_hex(remove_whitespace("""
00cd3bf408c742514e30ebfd001708e01f42de439a09d0d4b10044628becd8bc
690c45b967a6a900d6259c7d7d20ad49810c270d2fe1b75ffaa84f50071f64d1
696bce76e96dbcf2af054d77ded54c742aa38fadba52eebf7a5c8b6dbbf01f28
b3ebf4e9b3ca453c92ca8b65771c23671b9da85c51e7a2987395de45b125353d
430820b4c90b0ab9fc29e1c576a0ec35828c99c9880e208ecddf80bdaa9c3474
561e4c5bf67bf5d144b173f4f28edd1064a9dd8cf5f40b7c35e7e4dbeb370cca
bf06efb54e243645b902871a804c27904a620f31ef321af4d1589ca359de8895
24dfb43ddad51ab50617ab79a50a2d20e2325a05c9963602f2a1d7feaffc80d2
b8b88cbd3673531c399342f0bf1c04521d9a441c06593d9e95771129da942d83
bb81c627a50c8baafc2a731d97f2e1f638217f9f7b18f2644578fde5073a54a8
988fda357c64398a95965a7dd35ffdd7eb7495d4d1c9a950a0cd208a68371829
420633cb25e9da9e22b215e50f6ec2714f94ce6abb9a94fbbf6cd18f2fd5bfb7
8076034b88186957428fe0ea5e1dec7be31d753f155e2a8f7f4854a726612f43
ef91f88124011cd32f6841a347dc0411d708db65492ec277b81a335b76a86230
2acebf7db7cac724144c975ed4d91412eeec4cac3b2409696e3678cffcb7756b
de795c55f72da44f325b71dd6ac4e3c1ef512ee8ff24ab316507c6ac60031569
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(
            dec[0:3],
            b'\x63\x1b\x0c')

        plaintext = a2b_hex(remove_whitespace("""
59ccd9c2cfe740e9287b
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)
        self.assertEqual(msg, plaintext)

    def test_invalid_decrypting_to_length_second_to_last_from_prf(self):
        ciphertext = a2b_hex(remove_whitespace("""
09f010936fd77967dd2aa090be72ecdd8cb2b2a9fb954e644f08a1c1fd545000
7ece0b4e8e992831534309419c034b1c4b369269b808a890eac31d5bbfe73737
fd716e117e19638064292539e84dae20ec1d98ecd104e6c88d39d3544d5c43c9
fd4e9f4361c67116516fc2569f96e5df50a63e949d92009a7c865c7dd70ea89c
0002dd697dcd0e0304f8fa0738a3681322e672a9748f9d9eb1b7b8c1646a7bf2
a1967b2aa9793ae0ecdbaa2d601350fd931ea164bc02a33a9c22cee47f2d536d
92e465180b44e310bf044eec49cc54972d22e735123fbee76496a4c768acef89
66ae9e0ed46b753ec47e20a89af0ccf78c266aeb63aeb99d80e4c34bc4608e16
4aeffd93e886accd426e9e1cfee4f912f235940a9b8d4554953bee8753b8fe05
606fe5f46da70394b10f7e71dba3c10becf85a1f4ee619d421ef69fca837d8b1
b42598dea0232668b9c42223d77bae7fbe79a9dbf057eeaa51fceac114661a3b
572130776c36cfff9f134b08907ab2a6f927145806a779bc55bfb4215cb8c85d
ecaec5b15cd0a4be691b13e068a2381c33fb5adbdb564fd8be0938fdd710590c
08f95aa4ea90cc2cea195ef7a344e14715beff2186ad7d898e8f904861ab9133
817a13d8a6af23f83a89e5e1e7f8e163d6190e91a09c11939e3a7d48990b8e3b
5c0e01b773ba683f7df73b2f88746593c010cd9cab2ea3d9af5ebf30fba1ef0c
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        kdk = calc_kdk(self.priv_key, ciphertext)

        lengths = calc_lengths(self.priv_key, kdk)
        max_len = numBytes(self.pub_key.n) - 1 - 1 - 8 -1

        # the last_len is too long
        self.assertGreater(lengths[-1], max_len)
        self.assertEqual(lengths[-1], max_len + 1)

        # while second to last is short enough
        self.assertLessEqual(lengths[-2], max_len)
        self.assertEqual(10, lengths[-2])

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertNotEqual(dec[1:2], b'\x02')
        self.assertNotEqual(dec[-3:], b'\x6b\xc6\x86')

        plaintext = a2b_hex(remove_whitespace("""
0cfdf702efa4dc6bc686
"""))

        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_bad_version_byte(self):
        ciphertext = a2b_hex(remove_whitespace("""
0eb5e0c87c4ffffb760c8fac2a7f5b06f46301ab5b8374a59cc7006aa16e7f38
f27d957a4b475b41975246ffb5f2387ffdb62565411733331a4522a07a70bd40
ffe23f28f457be55a6cd1b6aab8c7127ec4b0c9d653c3d979fbd371854a80727
c0546d9852ccd6220b32a9081f6687fd2262dc806e55964ac799cfba56c0be1a
9fb3d4f46161cc5f251ddf3579a87c48c086da786d953829e513a525a87d8896
61606593600109a98159a91b606f138b9da1b2d427418d50647476fbdd17b521
11ca1a2ff9896167277d158d82ade196ad52ea6d381a63748e0068b160331c9c
b27c20afbeb696c1db16ea145e96a6e54a825c87c10f85b0d92fc299e254aa7f
74c73f17bc704407c31dba9fbda37e31f1231d06744beacb82a0130a9e7d004b
ed7e7036e33f1c89bd8ed0833def8e946efb53a9ea4abda91f1e1ed44e884d8e
45ea692e8f7e2b0f698024c8ed7ade62b251dcb91b249e937a85f823e6978e01
e8f7e9ed9c53f2f16d99afe58d3b77b3818aba64e139b3fcb0174542f348f9d2
c47dc9d78902a28e1a6613397a0f5938b860a3f6cd44e3b74a37ccdeda248cde
ee4a39497d76722e6860127eefdd80f447e69279bf177c1cd6c27ddd3f2f8992
4f21775df4824ece7f2a6f16266772a13669bfc04aa3b998ad03de17bbc27e62
9a495052e3e7f0b7b1c06dd4b429585a663172ba20527ad5186447bb74b5f368
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x01\x02')
        self.assertTrue(all(i != 0 for i in dec[2:-11]))
        self.assertEqual(dec[-11:-10], b'\x00')
        self.assertNotEqual(dec[-2:], b'\x59\x40')

        plaintext = a2b_hex(remove_whitespace("""
8bf3b682d8b950055940
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_wrong_padding_type(self):
        ciphertext = a2b_hex(remove_whitespace("""
714102bbe701855ec564853befd91262dc4cfbb3c417113c0c650b49c6878b10
1a76ba4822bde7ca538a2726c6eb9272a3dbda84119ec107d86d2b3a49d82de9
d176824f1c2d9cd9b432064c45dbfc60f1e71ec2772aef2669e756cae67ed757
b528cccc4ac6f1437a2d4bbedefece1bb5c21381eb4aebc1670c5bd65d408a19
c1329b9d9d236939da58a1285357e910edc83d428d1e5315c81cb070aecc24be
7fde807ce5d4f50dbe14478334c26be91ed4cb7335c63561b1a8c8c67e40844b
465fcf7df6e0df031572682427c62d3cd0c650ec5ef3875fd420516c5cb8089a
34757c81360dda37f7fbbd5ea9c8a54ff29f702741a0d496e268a8934b32cd16
bea2aa2628397097df0ba08545b9b23bc103a08077745239de34eec09f63fdcb
f3aece33a796adbd8dba0705ee3a1092d51f18f195e896b9c35b1a185752c627
55c4d9bf2069db141fddc6755c6927cae8d2811aef492f8324ca555b51a4eaf7
3001ddf88918798df67138a5475fd881b79a158dbe7dd61f241680039a7ae312
8a7b925ec7577cddbe116940e2f50ffa3ed36aee7e46ed6dc5b26e7c5f1d16cd
c199140742d3fe6bb7d2d4b74d0be675a3388c6fd6d09112dfdea93a701486e3
8f28add60fb674ac141b389eb4e09153167596a96d2e6618d98593278d22f560
5041882743ebafbeb18cdae093609ae6852498bedd8fb6b0a18ce358bfc9d6f2
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x01')
        self.assertTrue(all(i != 0 for i in dec[2:-11]))
        self.assertEqual(dec[-11:-10], b'\x00')
        self.assertNotEqual(dec[-2:], b'\x79\x0d')

        plaintext = a2b_hex(remove_whitespace("""
630fbcef34c1b72f790d
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_with_zero_byte_in_first_byte_of_PS(self):
        ciphertext = a2b_hex(remove_whitespace("""
1dd961276ba110ba4fdaf4f177780cbcb6373d2ae6769417a32c9b02eb00a48b
427e7e6edefac562fc42c5e2216c885af0f76bcfaf3da4db54ce9db0e22c498c
71e146561c1bbf7ff6246ffc6b0bfcd107830790c07ed9aeda70f2ead9e95799
2e3ed781e054f336e2ab08110f14ca3be11b92d77b0048c334d97d61c8bc4d82
db9c7236973d9ba4da066643440333b5a9e905e799f966c9164907866d9e6af2
d7f83466fe8409f24d5c9b3a06614af620087e838039355e65bde8f3ab7a8e06
943613e00fd143e21ec2684ac07e1dfdef85da32188a97e7585a667f89694111
6250f30e31bc0e2b20e536366e225759b12cdd578df18799dfee20b529189ad4
9789f60ce3649431889d740641df90d1dc372a62b4d77f9f5f9677b4f96770b0
7107ef37afe4e4dd6af4838ae18b61ce953eedcfc95d081951cbe0b097c6c334
489cf46fbba26009d7ebc8ecaa0b155ac60e1f40cc381cd9c85ac7fb25f8458d
964bd6e1fc85d6e18bc0fa5491c6995fa7225dcfe43d6a12bde24343d16ce421
46cf26a5ec1fd7fae5d829e1f274819a10445ac106f5a517ab89e62455c02469
271812be18e972af7d5ba3079dc427f1b7ff7eda2d0cba55f28edef280f5d924
3466d1c6f9c4b671777c75c9464e571e7115d97d0d86712781e6346a4472c98d
a976032ff1073850e7304b6bb4b60b019a7bd870c8d3fb26b212ddfd889b9fae
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:3], b'\x00\x02\x00')
        self.assertNotEqual(dec[-2:], b'\x60\xa8')

        plaintext = a2b_hex(remove_whitespace("""
778f208b90bef0f260a8
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_with_zero_byte_in_eight_byte_of_PS(self):
        ciphertext = a2b_hex(remove_whitespace("""
3d4477615f8b49c9453d31a5d5a228610d6d3e476737c163725106fa386440ff
23a9139f57977c09a1e885ddf2f180ddf0f0b0502ef60f0ff53d2ba444f03228
20f11acdd70e48543bd8ddd40d00ad9214d03487b265910cf423dea905af9088
36bf56ef872493b686aa15731714d1f0280e5cddad24ada53374c8aad063184d
62bbdc00efd4839b8f06de6c258d26149480b2fad6fcb2fc97cd78fb60305aa2
54cf1186fa134741a2340dc1d5243423c82c442f3afd915241f317607a2e2236
64601932e7b967d6793a7fde2819d475e2b8ab0117e3cc4854063a0c1ff1f5cd
9c9dc3e6c993d8861c11ee7155dd0ba2d4f47ff0ffc9c7fc8a891284789e5988
806fe7b5f5ec5783861fef756ef7339380215de11337ec8f2379b293c3cacf2f
81691c1ad75c9223a6c8edfb0451373d0b759d9d701f547b3c46d3fe1f3d24d3
3447a52bb55b9dd7050c41d11f3108ddccd5738a072905eb48067350e76a65f0
d274b0f4bde004cb673b715d4ab01dded4b6b7f69e133135ffcad4b1776e3610
830ae55a98d23610256865e305153ad7319ff905c16453297f5ebe64b8857bff
69c750d338368f6a55d73ae363a516fa4bf719cd01d46b609c134e3508d9616f
495ff2c869db7ad146376b102529c26407d8ffdedbfb005b7b220e0dcb089da3
682c9af7c278472cc19b6523b09661fe6f165bd7b7765ca2524eefa3526397b0
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        self.assertTrue(all(i != 0 for i in dec[2:9]))
        self.assertEqual(dec[9:10], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
364cfecf7e70a0829f28
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_invalid_with_no_padding_separator(self):
        ciphertext = a2b_hex(remove_whitespace("""
44c5b648e960aed2ad38497b6af118577a7978db288c0019cb6f8818578021ca
0d782c4e87bd6c3a73ef89e379311f0d449410c336bffdc9d970f995e7b59789
10c230b1ef11c06cc5de6ee79ca2f85f6f14e5c42cbb8269d40c032b91783755
fbfa7b87f16790bfea91933c67d2499a3d815cb70142285449757e606a438752
b803b0928c28dab4fd21125e5b79af04fe912fb444d32039e9e0e10210fbe017
4f43e2833ab862e4370b007025a919cf7b9c11241cf95ab10a9baa44a7ce7fa6
e802c5b8e5c466dba52704fc2325317526f36d25842e130fcdbbc3c631a1e4c6
7d23ffcb2218065863c178526616e8429916dff9101baf71857901bdaf305d26
9c944994f9cf0e02a5499432324b90a62c3c78bd7a7821420a11c43d0a80ee39
68ab8a363d6e6476f5424ae98bd59352aa9842e8f42cb0a34da68eac9dd16cf7
04573007efc4b3fc97161c342c836ff781c331c306f61052d3877ab190e307f4
f8d63c3bc8f6ab9a6920f9d1b9be482d3096b0b02447f53b0f974693e2a49b73
3684d8e33d7dfbb60d3b1aae02c222c395209b1e2647e7fcbf3c44cdee9c7332
9ce9ed255e011847d6d2e119d252d57c72572b2a309472f059cdae1f24e9cf1f
fddebc70b8b252229c7c0adfa763bda2243840bc9a553b6a4ea7737c0a002261
b36e198fca4314f659ca1071aceb2668079d663e4ed40e15e10d764aa8cb0c68
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:2], b'\x00\x02')
        for val in dec[2:]:
            self.assertNotEqual(val, 0)

        plaintext = a2b_hex(remove_whitespace("""
750d91268328712552cd
"""))
        self.assertEqual(len(plaintext), 10)

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_with_no_version_byte(self):
        ciphertext = a2b_hex(remove_whitespace("""
6b11bd1777ac4f1d8f36a3ebd01090a4c2be1e2deb928cef6427c107f8cb1d70
72c9d37d3b69de959c4d9f24ac92be7f584b0737416fcf9c58268b6eef5c52cf
bb3cd4ce241708f71fde98f9181ad5d8db734c61fe4bf2c5d1f11b08d71f84bc
448404041522387a67f7a2c7c9e24340343bcbf9b4d68487103d925751333cff
995d031492542d60e55cdab81dffc882079ed578ba35c33d456be27fc1f56f0e
2bc68d1bc35a0ce7b8a9a770816c7448013e56a1a8a9861885c99cf77b4beac6
82aa61822ffff61697e5afa566f10565644acd1080bef01ef14b498b329f4e0d
56f5c7c97b09398e557513c33354528eeccdb3dc167de119b0b9299e56bcc681
4cc5edbbf1b49769ec3487be04b10f3efa41e1a76eb9215ded0d2832923dcbc1
e6444967c6945d2c975456cc5d495f1b02b272d11ed46ddea4fa8d264709beda
36b252385ffc11679daa3fcdfe31f2980075f281dfbcfec2442092031a89323f
5d83caeacbaded9726de616fd9b034ac076fc4a72f0331f6b9efff91b79b440a
f115ea1a352ea2a9bfb4e74c0215aff27fd51dce2ac9e90332dbcc1e3de009ee
e079b4e70d2c0ce870aeca5c329471dc54a9e0c6c5e04275f1a8c0462971c6cd
a9c4b78ed362a8bdbb6f0de87b83cc4c1bcd813fde2741259cd1aad588d48440
3f63eca6d991b7302be939be2cf9408c6501037eeb56da342710df4b5406cba9
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertEqual(dec[0:1], b'\x02')
        self.assertTrue(all(i != 0 for i in dec[1:507]))
        self.assertEqual(dec[507:508], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
dd843a3331f5ca2035ac2ae0f87e544ec369e85514e295aba369179ea312fa07
4253d3670842ce05fa5a3f55c6e0dae35e0d81075319604267f513a62b44600f
2afe610ffa79ada034ca28682d3a4526f67e4243ad2c6d5456904e2aa6401d52
1e43c0e3753441a9db79a23eeb981c9627d6382145b09e682757213fa4f4466e
985e5d4975437c1d56803bc48ee269c99cd1e72c10c78fe4fc6119873d4d5ee5
5a159ab418ff0c87b8dfe54755cdc9e8997af9ceff432a0913c75a
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)

    def test_with_wrong_version_byte(self):
        ciphertext = a2b_hex(remove_whitespace("""
36e373c18770cdbb666723a84d16af1b97669f056111890863c1fa32af221e2f
6ab211643dcfb00a59f5ce241eba6622badcd49ca0889295d09330f6619f0d25
8ac29e1bbe6df83f664834a7c5d5337b3a870f79d2e055fc40674ec959799851
d269355cb51b8b42e382d66b20ca898a91afe9944dc233594dd6870ef9848958
396e169790751ea5679e48fa3f64da78cb99d6d8cd0e651e9d2bcdb6e0a60c92
dbdb193cd4a1013ae4d44af6bb9002e34b240ac825f26345a7f5db787e30036d
836b991f95e8cb2b1ebe6a722aceeabd98c6ebfc4ccd0d832ba4361f381790dc
84d18b78814d8174f41a42932626ea8073356f2edb8af0cdcb09bdb03244c405
f52207791aa95e783ac5bd8d4aa78de41be84be6077e3e312e1775044c57b7be
fd5f34370fc9238bb8a9d3b8e18acfc2783442f121e1f9a47f4f2f688a1aebc4
237afde71e070e4097ee05fa8bd20a80433d344a1409ad22c6109cd4799d2f32
38586519efa37640cd615bb90ef55e29bed75f40e9315b8b80a9c9b09251c9cf
206cbc8a34edb3be4c7a0a538f4ffa20f76def706660fdd152e89b1b22660371
e2a27b0f8d046a4f76dd355c5e250264317a5f52da6c438673158e3bc7cdf958
80a7b93f3a1ddb1841a4b819841ecc22be19bd92acf5b63b395fce376f72fb60
9a333486a3cc287f710370dcd57179a84d895c51ea6e1def763a0c2ff138ceb5
"""))
        self.assertEqual(len(ciphertext), numBytes(self.pub_key.n))

        # sanity check that the decrypted ciphertext is invalid
        dec = self.priv_key._raw_private_key_op_bytes(ciphertext)
        self.assertNotEqual(dec[0:1], b'\x00')
        self.assertEqual(dec[1:2], b'\x02')
        self.assertTrue(all(i != 0 for i in dec[2:507]))
        self.assertEqual(dec[507:508], b'\x00')

        plaintext = a2b_hex(remove_whitespace("""
51aa94d54ec9a891d92eb7e69cbfe6fd05a6561ea3f9768cb5224cbb1dcb9dec
c0278361147e6979bc3769b9ae741fc2928e94d7a0f8625e296f2039f23dde67
ea90adcf1afd52424d02228189fe4c3603134ce07f72994bdd929cc5a2a4
"""))

        msg = self.priv_key.decrypt(ciphertext)

        self.assertEqual(msg, plaintext)
