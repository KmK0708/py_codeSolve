# 문자열에서 괄호가 올바르게 짝을 이루는지 확인하는 함수
# 예: "(())" → True, "(()" → False

# 여는 괄호가 들어있으면 여는 괄호 스택에 추가
# 반대로 닫는 괄호면 스택에서 여는 괄호 제거

def check_brackets(str):
    stack = [] # 스택 리스트 생성

    for char in str:
        if char == '(': # 여는 괄호면
            stack.append(char) # 스택 추가
        elif char == ')': # 닫는 괄호가 나왔고
            if len(stack) == 0: # 스택이 비어있으면
                return False # 짝이 안맞는거라 false
            stack.pop() # 있으면 스택에서 제거

    if len(stack) == 0: # 짝이 다맞으면(스택에 아무것도 없으면)
        return True # True 반환
    else:
        return False


# 테스트
print(check_brackets("()"))
print(check_brackets("(())"))
print(check_brackets("(()"))
print(check_brackets("(())(()"))