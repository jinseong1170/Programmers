def solution(n):
    answer = 0
    m = n
    array = [i for i in range(1,n+1)]

    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += array[end]
            end += 1
        if interval_sum == m:
            count += 1
        interval_sum -= array[start]
    answer = count
    return answer