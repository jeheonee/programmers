import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    count = 0

    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                answer = (nums[i] + nums[j] + nums[k])
                if is_prime(answer):
                    count += 1
    return count