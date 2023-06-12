from collections import deque
def solution(cacheSize, cities):
    stack = deque([])
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    time = 0
    if cacheSize == 0:
        time = len(cities)*5
    else:
        for i in cities:
            if i not in stack:
                stack.append(i)
                time += 5
                if len(stack) > cacheSize:
                    stack.popleft()
            else:
                stack.remove(i)
                stack.append(i)
                time += 1
                if len(stack) > cacheSize:
                    stack.popleft()

    answer = time
    return answer