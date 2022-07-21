def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for a in new_id:
        if a.isalpha() or a.isdigit() or a == '-' or a == '_' or a == '.':
            answer += a
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] == '.' and len(answer) >= 2:
        answer = answer[1:]
        
    if answer[-1] == '.':
        answer = answer[:-1]
    
    if answer == '':
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    while len(answer) < 3:
            answer += answer[-1]
    return answer