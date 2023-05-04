def solution(numbers):
    numlist = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    return sum(numlist - set(numbers))