def dividers(num):
    cnt = 0
    i = 1
    while i <= num:
        if num % i == 0:
            cnt += 1
        i += 1
    return cnt

if __name__ == '__main__':
    num = int(input())
    print(dividers(num))
