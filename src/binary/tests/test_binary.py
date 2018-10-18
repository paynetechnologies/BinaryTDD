import pytest
from src.binary.binary import Binary

#CLASS TESTMETHOD(OBJECT):
class TestMethod(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

# def test_path():
#     import sys
#     for p in sys.path:
#         print(p)

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0

# def func(x):
#     return x + 1

# def test_answer():
#     assert func(3) == 5

'''
def test_binary_init_int():
    binary = Binary(6)
    assert int(binary) == 6

def test_binary_int():
    binary = Binary(6)
    assert int(binary) == 6    

def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = Binary(-4)



def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6

def test_binary_str():
    binary = Binary(6)
    assert str(binary) == '110'


def test_binary_init_binstr():
    binary = Binary('0b110')
    assert int(binary) == 6

def test_binary_bin():
    binary = Binary(6)
    assert bin(binary) == '0b110'


def test_binary_init_hexstr():
    binary = Binary('0x6')
    assert int(binary) == 6

def test_binary_init_hex():
    binary = Binary(0x6)
    assert int(binary) == 6

def test_binary_hex():
    binary = Binary(6)
    assert hex(binary) == '0x6'


def test_binary_init_intseq():
    binary = Binary([1, 1, 0])
    assert int(binary) == 6

def test_binary_init_strseq():
    binary = Binary(['1', '1', '0'])
    assert int(binary) == 6


'''
'''
   
    # Conversions

    def test_binary_eq():
        assert Binary(4) == Binary(4)


    '''


# if __name__ == '__main__':
#     test_where_AM_I()