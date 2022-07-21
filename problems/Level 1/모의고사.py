def solution(answers):
    answer = []
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 1, 2, 3, 2, 4, 2, 5]
    data3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0] * 3
    res = 0
    
    for idx, x in enumerate(answers):
        if x == data1[idx % len(data1)]:
            cnt[0] += 1
        if x == data2[idx % len(data2)]:
            cnt[1] += 1
        if x == data3[idx % len(data3)]:
            cnt[2] += 1
        
    res = max(cnt)    
    for idx, a in enumerate(cnt):
        if a == res:
            answer.append(idx + 1)
    return answer