from collections import deque  # 큐 자료구조 사용을 위해 deque 가져오기

# 미로 탐색(넓이 우선 탐색)
class BFS_Exitor:
    def __init__(self):
        self.maze =[
    ['1', '1', '1', '1', '1', '1'], # 미로 설정 미로 정보: 6x6
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
    ]
        
        self.rows = len(self.maze) # 행 (row)의 개수
        self.cols = len(self.maze[0]) # 열(column)의 개수

        # 상, 하, 좌, 우
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        self.start = None
        self.end = None
        # 시작점 찾기
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == 'e':
                    self.start = (row, col)
                elif self.maze[row][col] == 'x':
                    self.end = (row, col)

        # 방문한 곳을 기록하는 2차원 리스트 만들기
        self.visited = []
        for _ in range(self.rows):
            row = [False] * self.cols
            self.visited.append(row)

        # 시작점 또는 도착점이 없으면 에러
        if self.start is None:
            raise ValueError("미로에 시작점(e)이 없습니다.")
        if self.end is None:
            raise ValueError("미로에 도착점(x)이 없습니다.")
        
    def bfs(self):
        queue = deque()
        # 시작 위치를 큐에 넣고 시작
        start_row, start_col = self.start
        queue.append((start_row, start_col, 0))
        self.visited[start_row][start_col] = True

        while queue:
            row, col, dist = queue.popleft() # 큐의 최하단 요소를 현재 위치로 저장하고 큐에서 제거

            # 현재 위치가 도착점이면 성공
            if (row, col) == self.end:
                print("도착했습니다! 최단 거리:", dist)
                return

            # 네 방향으로 탐색
            for dr, dc in self.directions:
                new_row = row + dr
                new_col = col + dc

                # 미로 범위 안에 있고, 길이고, 아직 방문 안 한 곳이라면
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                        if self.maze[new_row][new_col] != '0' and not self.visited[new_row][new_col]:
                            self.visited[new_row][new_col] = True
                            queue.append((new_row, new_col, dist + 1))

        print("도착할 수 없습니다.") # while이 끝났는데 못 도착했을 경우

# 실행
solver = BFS_Exitor()
solver.bfs()