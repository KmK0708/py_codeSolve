# 스택을 활용하여 미로를 탈출하라 (깊이 우선 탐색 알고리즘)
map = [['1', '1', '1', '1', '1', '1'], # 미로 설정
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]
map_size = 6 # 맵 크기 지정

def find_start(maze):
  #시작점 e의 좌표 찾기 (문자여서 찾아줘야함)
  for y in range(len(maze)):
    for x in range(len(maze[0])):
      if maze[y][x] == 'e':
        return y,x
      
def DFS_algorithm(maze):
    start = find_start(maze)
    if not start:
        print("시작점 없음")
        return False

    stack = [start] # 스택에 시작위치 넣고 시작
    print("시작위치: ",stack)
    # 지나왔던곳 좌표 저장
    visited = []
    # 상하좌우 이동 방향
    movedir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 시작 지점이 1,0  -1,0 이 위 / 1,0 이 아래 / 0,-1 이 왼쪽

  
    while stack:
        # 현재 위치 꺼내기
        y, x = stack.pop()
        print(f"현재 위치: ({y}, {x})")
        # 지나온 곳이면 계속
        if (y, x) in visited:
            continue
        # 방문 표시 (집합에 현재 위치 추가)
        visited.append((y, x))
        print("지나간 위치 : ",visited)

        # 도착점('1')을 찾았는지 확인
        if maze[y][x] == 'x':  # y,x 위치에 x 가 있으면
            print(f"도착점 발견! ({y}, {x})")     # 위치 보여주고 멈추기
            return True 
        
        for dy,dx in movedir:
            ny = y + dy
            nx = x + dx
        # 유효한 범위인지 확인 (미로 범위 내에 있는지)
            if 0 <= ny < map_size and 0 <= nx < map_size:
            # 방문 안했고 벽이 아닌 경우
                if (ny,nx) not in visited and maze[ny][nx] == '0' or maze[ny][nx] == 'x':
                    stack.append((ny,nx))
                    

    print("도착 불가")
    return False

test = DFS_algorithm(map)
print("탐색 결과:", test)

