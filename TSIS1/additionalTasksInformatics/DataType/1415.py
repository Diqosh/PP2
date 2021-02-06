text = input()
num = int(input())


def func(i):
    ascii_code = ord(i) - num
    return chr(ascii_code + 26) if ascii_code < 65 else chr(ascii_code)

if __name__ == '__main__':
    print(''.join([func(i) for i in text]))

