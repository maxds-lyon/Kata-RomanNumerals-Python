from roman_numerals import to_roman, from_roman


def test_to_roman_1():
    assert to_roman(1) == "I"


def test_to_roman_2():
    assert to_roman(2) == "II"


def test_to_roman_3():
    assert to_roman(3) == "III"


def test_to_roman_4():
    assert to_roman(4) == "IV"


def test_to_roman_5():
    assert to_roman(5) == "V"


def test_to_roman_9():
    assert to_roman(9) == "IX"


def test_to_roman_12():
    assert to_roman(12) == "XII"


def test_to_roman_16():
    assert to_roman(16) == "XVI"


def test_to_roman_29():
    assert to_roman(29) == "XXIX"


def test_to_roman_44():
    assert to_roman(44) == "XLIV"


def test_to_roman_45():
    assert to_roman(45) == "XLV"


def test_to_roman_68():
    assert to_roman(68) == "LXVIII"


def test_to_roman_83():
    assert to_roman(83) == "LXXXIII"


def test_to_roman_97():
    assert to_roman(97) == "XCVII"


def test_to_roman_99():
    assert to_roman(99) == "XCIX"


def test_to_roman_500():
    assert to_roman(500) == "D"


def test_to_roman_501():
    assert to_roman(501) == "DI"


def test_to_roman_649():
    assert to_roman(649) == "DCXLIX"


def test_to_roman_798():
    assert to_roman(798) == "DCCXCVIII"


def test_to_roman_891():
    assert to_roman(891) == "DCCCXCI"


def test_to_roman_1000():
    assert to_roman(1000) == "M"


def test_to_roman_1004():
    assert to_roman(1004) == "MIV"


def test_to_roman_1006():
    assert to_roman(1006) == "MVI"


def test_to_roman_1023():
    assert to_roman(1023) == "MXXIII"


def test_to_roman_2014():
    assert to_roman(2014) == "MMXIV"


def test_to_roman_3999():
    assert to_roman(3999) == "MMMCMXCIX"


def test_from_roman_I():
    assert from_roman("I") == 1


def test_from_roman_IV():
    assert from_roman("IV") == 4


def test_from_roman_VII():
    assert from_roman("VII") == 7


def test_from_roman_IX():
    assert from_roman("IX") == 9


def test_from_roman_XLIV():
    assert from_roman("XLIV") == 44


def test_from_roman_XLV():
    assert from_roman("XLV") == 45


def test_from_roman_LXVIII():
    assert from_roman("LXVIII") == 68


def test_from_roman_LXXXIII():
    assert from_roman("LXXXIII") == 83


def test_from_roman_XCVII():
    assert from_roman("XCVII") == 97


def test_from_roman_XCIX():
    assert from_roman("XCIX") == 99


def test_from_roman_D():
    assert from_roman("D") == 500


def test_from_roman_DI():
    assert from_roman("DI") == 501


def test_from_roman_DCXLIX():
    assert from_roman("DCXLIX") == 649


def test_from_roman_DCCXCVIII():
    assert from_roman("DCCXCVIII") == 798


def test_from_roman_DCCCXCI():
    assert from_roman("DCCCXCI") == 891


def test_from_roman_M():
    assert from_roman("M") == 1000


def test_from_roman_MIV():
    assert from_roman("MIV") == 1004


def test_from_roman_MVI():
    assert from_roman("MVI") == 1006


def test_from_roman_MXXIII():
    assert from_roman("MXXIII") == 1023


def test_from_roman_MMXIV():
    assert from_roman("MMXIV") == 2014


def test_from_roman_MMMCMXCIX():
    assert from_roman("MMMCMXCIX") == 3999
