def solution(participant, completion):
    answer = ''
    data = {a: 0 for a in participant}
    for a in participant:
        data[a] += 1
    for a in completion:
        data[a] -= 1
    for a in data:
        if data[a] != 0:
            answer = a
    return answer