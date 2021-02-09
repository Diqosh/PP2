if __name__ == '__main__':
    cnt = 0
    nums = [int(i) for i in input().split()]
    for n in nums:
        if n == 0:
            cnt += 1
    for n in nums:
        if n > 0:
            print(n, end=' ')
    else:
        for i in range(cnt):
            print('0', end=' ')
