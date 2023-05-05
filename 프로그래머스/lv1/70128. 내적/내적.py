# 다른 풀이
def solution(a, b):
    ab = []
    
    for i in range(len(a)):
       ab.append(a[i] * b[i])
    
    return sum(ab)