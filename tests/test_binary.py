import pytest
from src.binary.cbinary import CBinary

########################################
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5
########################################

########################################
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
########################################

########################################
class TestMethod(object):
    def test_one(self):
        x = "this"
        assert 'h' in x
    
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
########################################

########################################
# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0
########################################

    # def test_path():
    #     import sys
    #     for p in sys.path:
    #         print(p)


    # def test_zero_division():
    #     with pytest.raises(ZeroDivisionError):
    #         1 / 0

########################################

'''
@pytest.mark.skip(reason="testing the skip function")
def test_binary_init_int():
    binary = CBinary(6)
    assert int(binary) == 6
'''

def test_binary_int():
    binary = CBinary(6)
    assert int(binary) == 6    
'''
def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = CBinary(-4)



def test_binary_init_bitstr():
    binary = CBinary('110')
    assert int(binary) == 6

def test_binary_str():
    binary = CBinary(6)
    assert str(binary) == '110'


def test_binary_init_binstr():
    binary = CBinary('0b110')
    assert int(binary) == 6

def test_binary_bin():
    binary = CBinary(6)
    assert bin(binary) == '0b110'


def test_binary_init_hexstr():
    binary = CBinary('0x6')
    assert int(binary) == 6

def test_binary_init_hex():
    binary =CBinary(0x6)
    assert int(binary) == 6

def test_binary_hex():
    binary = CBinary(6)
    assert hex(binary) == '0x6'


def test_binary_init_intseq():
    binary = CBinary([1, 1, 0])
    assert int(binary) == 6

def test_binary_init_strseq():
    binary = CBinary(['1', '1', '0'])
    assert int(binary) == 6


# Conversions

def test_binary_eq():
    assert CBinary(4) == CBinary(4)


def test_binary_int():
    binary = CBinary(6)
    assert int(binary) == 6



def test_binary_bin():
    binary = CBinary(6)
    assert bin(binary) == '0b110'

def test_binary_hex():
    binary = CBinary(6)
#     print (f'test_binary_hex:{binary}')
    assert hex(binary) == '0x6'


def test_binary_str():
    binary = CBinary(6)
    assert str(binary) == '110'
'''