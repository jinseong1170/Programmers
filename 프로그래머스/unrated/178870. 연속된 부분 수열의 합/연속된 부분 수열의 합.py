# 다른풀이
def solution(sequence, k):
    L = len(sequence)
    right = 0
    partial_sum = sequence[0]
    result = []

    for left in range(L):
        while right + 1 < L and partial_sum < k:
            right += 1
            partial_sum += sequence[right]

        if partial_sum == k:
            if not result:
                result = [left, right]
            else:
                result_left, result_right = result
                if right - left < result_right - result_left:
                    result = [left, right]

        partial_sum -= sequence[left]

    return result