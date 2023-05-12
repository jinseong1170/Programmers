# 다른 풀이
def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)  # i가 '('일 경우 추가
        else:
            try :
                stack.pop() # i가 ')'일 경우 리스트에서 하나 꺼냄
            except: 
                return False # 리스트에 꺼낼게 없으면 false
            
    if len(stack) == 0 :
        return True # 문자열 순회가 끝나고 리스트가 비어있다면 True
    else: 
        return False # 값이 있으면 False
