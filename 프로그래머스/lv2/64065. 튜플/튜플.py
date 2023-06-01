# 다른 풀이
def solution(s):
    answer = []
    s = eval(s.replace("{", "[").replace("}", "]"))

    s.sort(key=lambda x: len(x))

    for i in s:
        for j in i:
            if not int(j) in answer:
                answer.append(int(j))

    return answer