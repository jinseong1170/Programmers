# 다른 풀이
def solution(people, limit):
    people.sort()
    j = 0 
    i = len(people)-1
    while (i > j):
        if (people[i] + people[j]<= limit):
            j+=1
        i-= 1
    return len(people)-j