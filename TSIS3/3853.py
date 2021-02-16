
if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    move = int(input())
    if move == 0:
        for i in nums:
            print(i, end=' ')
    elif move > 0:
        for i in nums[-move:]:
            print(i, end=' ')
        for i in nums[0:move-1]:
            print(i, end=' ')
    else:
        for i in nums[move+1:]:
            print(i, end=' ')
        for i in nums[:-move]:
            print(i, end=' ')
#5 3 7 4 6
#4 6 5 3 7