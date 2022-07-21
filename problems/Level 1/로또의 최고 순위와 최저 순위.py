def solution(lottos, win_nums):
    answer = []
    count = [a for a in lottos if a in win_nums]
    zero_num = lottos.count(0)
    min_count = len(count)
    max_count = len(count) + zero_num
    
    if 2 <= max_count <= 6:
        answer.append(7 - max_count)
    else:
        answer.append(6)
    
    if 2 <= min_count <= 6:
        answer.append(7 - min_count)
    else:
        answer.append(6)
    return answer