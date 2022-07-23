def solution(nums):
    answer = 0
    data = {a: 0 for a in nums}
    for a in nums:
        data[a] += 1
    
    if len(nums) // 2 > len(data):
        answer = len(data)
    else:
        answer = len(nums) // 2
    return answer