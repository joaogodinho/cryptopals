"""
Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule

Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

"""
import binascii


BASE_CODES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hexToBase64(string):
    raw = string
    size = len(raw)
    result = ''

    # Handle 24 bits at a time (3 x 8 = 4 x 6)
    for i in range(0, size, 3):
        # Handle upper 6 bits
        b = (raw[i] & 0xFC) >> 2
        result += BASE_CODES[b]

        # Get the remaining 2 bits from byte
        b = (raw[i] & 0x03) << 4

        # At least one more byte to handle
        if i + 1 < size:
            # Get the upper 4 bits from the next byte (another 6 bit group)
            b |= (raw[i+1] & 0xF0) >> 4
            result += BASE_CODES[b]

            # Get the remaining 4 bits from byte
            b = (raw[i+1] & 0x0F) << 2

            # Last group is 24 bits
            if i + 2 < size:
                # Get 2 bits from the next byte (another 6 bit group)
                b |= (raw[i+2] & 0xC0) >> 6
                result += BASE_CODES[b]

                # Get the remaining 6 bits from the last byte
                b = (raw[i+2] & 0x3F)
                result += BASE_CODES[b]

            # Last group is 16 bits
            else:
                result += BASE_CODES[b]
                result += "="

        # Last group is 8 bits
        else:
            result += BASE_CODES[b]
            result += "=="
    return result


def test_hexToBase64():
    import base64
    import random
    import os
    for i in range(100):
        raw = binascii.b2a_hex(os.urandom(random.randrange(50)))
        libEnc = base64.b64encode(raw).decode('utf-8')
        userEnc = hexToBase64(raw)
        assert libEnc == userEnc


if __name__ == '__main__':
    test_hexToBase64()
    original = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    result = hexToBase64(binascii.unhexlify(original))
    assert result == expected
    print(result)
