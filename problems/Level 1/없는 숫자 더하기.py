def solution(numbers):
    data = [i for i in range(10)]
    answers = [a for a in data if a not in numbers]
    return sum(answers)