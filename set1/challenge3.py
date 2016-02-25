"""

Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
Evaluate each output and choose the one with the best score.
Achievement Unlocked

You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

"""
import binascii


def scoreXOR(ciphertext):
    """
    Score all possible keys for the giving ciphertext. Scoring is based the number of letters in the possible plaintext
    and normalized with ciphertext size
    Returns a list with possible plaintexts and respective score.
    Minimum score is 50%
    """
    min_ascii = 0x20
    max_ascii = 0x7F
    A = 0x41
    Z = 0x5A
    a = 0x61
    z = 0x7A
    # 60% minimum score
    min_score = 0.5
    cp_size = len(ciphertext)

    scores = []
    # Test all possible keys
    for k in range(1, 0x100):
        score = 0
        temp = [bytes([c ^ k]) for c in ciphertext]
        for t in temp:
            # Non printable ASCII, throw it out
            if ord(t) < min_ascii:
                score = -1
                break
            # Score letters and spaces
            if A < ord(t) < Z or a < ord(t) < z or ord(t) == min_ascii:
                score += 1
            # Penalize non-letters and numbers
            elif min_ascii < ord(t) < A or z < ord(t) < max_ascii:
                score -= 2
        # Normalize the obtained score, must be above minimum
        normalized_score = float(score) / cp_size
        if normalized_score > min_score:
            scores.append((k, normalized_score))

    # Try to decrypt ct with the best scores
    result = []
    for s in scores:
        plaintext = ''
        for c in ciphertext:
            plaintext += chr(ord(bytes([c ^ s[0]])))
        result.append((plaintext, s[1]))
    # List of possible plaintexts with score (min_score, 1)
    return result


if __name__ == '__main__':
    original = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(scoreXOR(original))
