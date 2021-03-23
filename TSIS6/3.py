def multiplyNumbers(*nums):
    total = 1
    for number in nums:
        total *= number
    return total


if __name__ == '__main__':
    listOfNumbers = list(map(int, input().split()))
    print(multiplyNumbers(*listOfNumbers))
