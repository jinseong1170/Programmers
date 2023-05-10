# 다른 풀이
def solution (number) :
    #  지정된 개수의 요소를 조합한 모든 경우의 수를 반환하는 함수
    from itertools import combinations 
    
    cnt = 0
    
    # 3개의 요소를 조합한 모든 경우의 수를 반환
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1  # 각 경우마다 합이 0인지 확인, 합이 0이면 cnt + 1
    return cnt