def solution(s):
    a = s.split() # 문자열 분리
    
    for i in range(len(a)):
        a[i] = int(a[i]) # a 정수형 변환
        
    return str(min(a)) + " " + str(max(a))