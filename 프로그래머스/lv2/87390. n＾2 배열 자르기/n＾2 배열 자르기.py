#다른 풀이
def solution(n, left, right):
    list = []
    for i in range(left,right+1):
        a = i//n
        b = i%n
        list.append(max(a,b)+1)
    return list