import sys


def solve():
    test = []
    with open(sys.argv[1], 'r') as file:
        test = file.readline().split(",")
        plus = int(file.readline())
        minus = int(file.readline())
    nums = [int(numeric_string) for numeric_string in test]
    nums.sort()
    nums.reverse()
    total = 0
    test = True
    for i in nums:
        if(i == nums[0] and test):
            total = i
            test = False
        elif(plus > 0):
            total = total + i
            plus = plus - 1
        else:
            total = total - i
    return total


print(solve())
