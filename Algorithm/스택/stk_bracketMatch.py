# 문자열에서 괄호가 올바르게 짝을 이루는지 확인하는 함수
# 예: "[({})]" → True, "(({)" → False

# 여는 괄호가 들어있으면 여는 괄호 스택에 추가
# 반대로 닫는 괄호면 스택에서 여는 괄호 제거

# 내 작성답안
def check_brackets(str):
    stack = [] # 스택 리스트 생성

    for char in str:
        if char == '(' or char == '{' or char == '[': # 여는 괄호면
            stack.append(char) # 스택 추가
        elif char == ')'or char == '}' or char == ']': # 닫는 괄호가 나왔고
            if len(stack) == 0: # 스택이 비어있으면
                return False # 짝이 안맞는거라 false
            stack.pop() # 있으면 스택에서 제거

    if len(stack) == 0: # 짝이 다맞으면(스택에 아무것도 없으면)
        return True # True 반환
    else:
        return False

# 위 처럼하니까 "([)]" 이것도 True 가 뜸

# 고친 정답
def check_all_brackets(dap):
    stk = [] # 괄호 저장 스택

    # 괄호 짝 딕셔너리
    # 닫는 괄호 → 여는 괄호
    pairs = {')': '(', '}': '{', ']': '['}

    # 입력한 괄호들 검사
    for char in dap:
        if char in '({[': # 여는 괄호면 
            stk.append(char) # 스택에 저장
        elif char in ')}]': # 닫는괄호인데
            if len(stk) == 0: # 스택이 비어있다면
                return False # 짝이 안맞는거라 False
            top = stk.pop()  # 스택에서 마지막 여는 괄호 꺼내기
            if pairs[char] != top: # 꺼낸 여는 괄호가 짝이 안맞으면 False
                return False

    if len(stk) == 0:
        return True
    else:
        return False

# 테스트
print(check_all_brackets("({[]})"))    # ✅ True
print(check_all_brackets("([)]"))      # ❌ False
print(check_all_brackets("(((())))"))  # ✅ True
print(check_all_brackets("{[}"))       # ❌ False