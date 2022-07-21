def solution(s):
    data = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    
    for idx, a in enumerate(data):
        if a in s:
            s = s.replace(a, str(idx))
        answer = s
    return int(answer)