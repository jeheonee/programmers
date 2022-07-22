def solution(numbers, hand):
    answer = ''
    data = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    now_left_hand = data['*']
    now_right_hand = data['#']
    for a in numbers:
        if a in [1, 4, 7]:
            now_left_hand = data[a]
            answer += 'L'
        elif a in [3, 6, 9]:
            now_right_hand = data[a]
            answer += 'R'
        else:
            dist_left = abs(now_left_hand[0] - data[a][0]) + abs(now_left_hand[1] - data[a][1])
            dist_right = abs(now_right_hand[0] - data[a][0]) + abs(now_right_hand[1] - data[a][1])
            
            if  dist_left > dist_right:
                now_right_hand = data[a]
                answer += 'R'
            elif dist_left < dist_right:
                now_left_hand = data[a]
                answer += 'L'
            else:
                if hand == 'left':
                    answer += 'L'
                    now_left_hand = data[a]
                else:
                    hand == 'right'
                    answer += 'R'
                    now_right_hand = data[a]
    return answer