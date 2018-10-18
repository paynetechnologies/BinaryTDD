from collections.abc import Sequence

class Binary:
    def __init__(self, value=0):
        print('Binary')
        if isinstance(value, Sequence):
            print(f'isinstance {value}')
            if len(value) > 2:
                if value[0:2] == '0b':
                    self._value = int(value, base=2)
                elif value[0:2] == '0x':
                    self._value = int(value, base=16)
                else:
                    self._value = int(''.join([str(i) for i in value]), base=2)
            print (f'Binary : {self._value}')
        else:
            try:
                self._value = int(value)
                if self._value < 0:
                    raise ValueError("Binary cannot accept negative numbers. Use SizedBinary instead")
            except ValueError:
                raise ValueError("Cannot convert value {} to Binary".format(value))

    def __int__(self):
        return self._value