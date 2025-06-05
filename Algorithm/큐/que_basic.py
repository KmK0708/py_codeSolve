# 선입선출(FIFO, First-In First-Out) 형태의 자료구조버퍼링(buffering)
# • 실시간 비디오 스트리밍
# • 시뮬레이션
# • 은행 대기표
# • 공항 비행기 활주로 이용
# • 인터넷 데이터 패킷 모델링

queue = []  # 큐를 저장할 리스트

# 큐에 값 추가 (enqueue)
def enqueue(item):
    queue.append(item)

# 큐에서 값 제거하고 반환 (dequeue)
def dequeue():
    if not is_empty():
        return queue.pop(0)  # 가장 앞에 있는 항목 제거
    else:
        return "큐가 비어있음"

# 큐의 맨 앞 값 확인 (peek) 제거 X
def peek():
    if not is_empty():
        return queue[0]
    else:
        return "큐가 비어있음"

# 큐가 비었는지 확인
def is_empty():
    return len(queue) == 0

# 테스트
enqueue(10)
enqueue(20)
enqueue(30)

print("맨 앞:", peek())        # 10
print("꺼낸 값:", dequeue())   # 10
print("다음 값:", dequeue())   # 20
print("큐가 비었나?", is_empty())  # False
print("꺼낸 값:", dequeue())   # 30
print("큐가 비었나?", is_empty())  # True
print("꺼낸 값:", dequeue())   # 큐가 비어있음