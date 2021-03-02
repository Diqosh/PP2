if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = max(arr)
    while max(arr) == max1:
        arr.remove(max1)
    print(max(arr))



