def solution(s):
    cnt1 = 0
    cnt2 = 0
    
    while s != '1':
        cnt1 += s.count('0')
        length = s.count('1')
        
        s = bin(length)[2:]
        cnt2 += 1
        
    answer = [cnt2, cnt1]
    return answer