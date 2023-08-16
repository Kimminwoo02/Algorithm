def solution(cards1, cards2, goal):
    answer = ''
    
    p1 = p2 = 0
    
    for i in goal:
        if len(cards1)>p1 and cards1[p1] ==i:
            p1+=1
            
        elif len(cards2)>p2 and cards2[p2] == i:
            p2+=1
            
        else:
            answer+="No"
            break
    if answer=='':
        answer+="Yes"
    return answer