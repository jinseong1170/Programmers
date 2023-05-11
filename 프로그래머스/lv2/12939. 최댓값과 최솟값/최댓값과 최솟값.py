def solution(s):
    a = s.split()
    
    for i in range(len(a)):
        a[i] = int(a[i])
    return str(min(a)) + " " + str(max(a))