def solution(n, lost, reserve):
    
    new_reserve = [a for a in reserve if a not in lost]
    new_lost = [a for a in lost if a not in reserve]
    answer = n - len(new_lost)
    new_reserve.sort()
    new_lost.sort()
    
    for a in new_reserve:
        for lose in new_lost:
            data = [a-1, a, a+1]
            if lose in data:
                answer += 1
                new_lost = new_lost[1:]
                new_reserve = new_reserve[1:]
                break
    return answer