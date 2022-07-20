def solution(numbers):
    data = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            data.add(sum)
    
    answer = list(data)
    answer.sort()
    return answer