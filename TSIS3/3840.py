if __name__ == '__main__':
    temp = 1
    nums = [int(i) for i in input().split()]
    for i in range(0,len(nums),2):
        if i + 2 > len(nums):
            break
        temp = nums[i+1]
        nums[i+1] = nums[i]
        nums[i]  = temp
    for a in nums:
        print(a, end=' ')


