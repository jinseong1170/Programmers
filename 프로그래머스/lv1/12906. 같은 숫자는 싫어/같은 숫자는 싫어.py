# 다른방법 풀이
def solution(arr):
    answer = []
    j = -1
    for i in arr:
        if i != j:
            j = i
            answer.append(i)

    return answer