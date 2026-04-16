from beautiful_dsa_algos_coding_interviews.strings.encode_decode_strings import decode, encode


def test_encode_decode_strings_round_trip():
    values = ["lint", "code", "#hash", ""]
    assert decode(encode(values)) == values
