# 리스트를 사용해서 간단한 스택 만들기
# push, pop, peek, is_empty 기능

stack = []

# 스택에 넣기
def push(items):
    stack.append(items)

# 스택에서 값 제거하고 반환하기
def pop():
    if not is_empty():
        return stack.pop()
    else:
        return "스택이 비어있음"

def peek():
    if not is_empty():
        return stack[-1]
    else:
        return "스택이 비어있음"

#비어있는지 확인하기
def is_empty():
    return len(stack) == 0

push(1)
push(2)
push(3)
print("현재 스택:",stack)

print("현재 맨 위 값 (peek):", peek())

print("스택에서 꺼낸 값:", pop())
print("스택에서 꺼낸 값:", pop())


# 스택이 비었는지 확인
print("스택이 비었나??", is_empty())