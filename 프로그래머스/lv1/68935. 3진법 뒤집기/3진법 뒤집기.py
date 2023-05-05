# 블로그 참고 다른 풀이

# 1. 삼진법을 계산하기 위해서 %3으로 나머지를 구합니다.
# 2. 낮은 숫자부터 1, 3, 9, 27을 곱하기 위해 arr을 역순으로 정렬합니다.
# 3. 십진법으로 다시 변환합니다.

def solution(n):
    answer = 0
    lst = ""    # 삼진법을 임시 저장할 문자열

    while n > 0:    # 삼진법 계산
        lst += str(n % 3)
        n //= 3

    lst = lst[::-1]     # 문자열을 반대로 정렬
    count = 1

    for i in lst:   # 다시 십진법으로 계산
        answer += int(i) * count
        count *= 3
        
    return answer
