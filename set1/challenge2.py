"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""
import binascii


def fixedXOR(a, b):
    assert len(a) == len(b)
    result = bytearray()
    for (x, y) in zip(a, b):
        result.append(x ^ y)
    return result


if __name__ == '__main__':
    raw1 = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
    raw2 = binascii.unhexlify('686974207468652062756c6c277320657965')
    expected = binascii.unhexlify('746865206b696420646f6e277420706c6179')
    result = fixedXOR(raw1, raw2)
    assert expected == result
    print(binascii.hexlify(result))
