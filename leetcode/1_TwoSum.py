class Solution:
    def twoSum(self, nums, target):
        myList = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    myList.append(i)
                    myList.append(j)
                    return myList




