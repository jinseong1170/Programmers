# 다른 풀이
def solution(n, t, m, p):
    answer = ''
    # n=진법, t=미리구할숫자갯수, m=게임참가인원, p=튜브의순서
    # 2, 4, 2, 1 => 0111
    end = p + t * m
    # p, p+m, p+2m, ... p+tm 번째 숫자를 출력
    cnt = 0
    num = 0

    num_list = []
    exp_index = '0123456789ABCDEF'
    while cnt <= end :
        # num을 n진법으로 표현
        import copy
        num_copy = copy.copy(num)

        nexp = ''
        while num_copy > 0 :
            rest = num_copy % n
            num_copy = num_copy // n
            nexp += exp_index[rest]
        nexp = nexp[::-1]

        for exp in nexp :
            num_list.append(exp)

        num += 1 # 숫자(0, 1, 2, 3, ...)
        cnt += len(nexp) # n = num_list에 몇개가 append 되었는지

    num_list.insert(0, '0')
    tubes = [num_list[p-1 + i*m] for i in range(0, t)]
    answer = ''.join(tubes)

    return answer
