def fact(num):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total


if __name__ == '__main__':
    num = int(input())
    print(fact(num))
