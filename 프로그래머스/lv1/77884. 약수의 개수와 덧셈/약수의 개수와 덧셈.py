# 다른 풀이
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:  # 제곱수라면
            answer -= i # 약수의 개수는 홀수개

        else :
            answer += i

    return answer