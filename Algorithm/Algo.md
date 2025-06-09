## Stack
LIFO (Last In, First Out) 구조로 가장 나중에 들어간 데이터가 가장 먼저 나옵니다<br>
list를 사용하여 append()로 추가, pop()으로 제거하거나 collections.deque를 사용할 수 있습니다<br>
함수 호출 스택, 괄호 검사, 되돌리기(undo) 기능 등에 활용됩니다<br>

## Queue
FIFO (First In, First Out) 구조로 가장 먼저 들어간 데이터가 가장 먼저 나옵니다<br>
collections.deque를 사용하여 append()로 추가, popleft()로 제거하거나 queue.Queue 클래스를 사용할 수 있습니다<br>
작업 대기열, 프린터 스풀링, BFS 알고리즘 등에 활용됩니다<br>

## deque
양쪽 끝에서 삽입과 삭제가 모두 가능한 이중 종료 큐(Double-Ended Queue)입니다<br>
collections.deque를 사용하여 append()/appendleft()로 추가, pop()/popleft()로 제거할 수 있습니다<br>
슬라이딩 윈도우, 회전 배열, 양방향 탐색 등에 활용됩니다<br>