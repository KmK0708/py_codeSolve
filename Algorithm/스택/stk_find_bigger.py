# 뒤에서 처음으로 나보다 큰 수 찾기
# 정수로 이루어진 리스트가 있을 때,
# 각 숫자에 대해 오른쪽에 있는 수들 중에서 처음으로 나보다 큰 수를 찾아 출력하세요.
# 만약 그런 수가 없다면 -1을 출력하세요.

# 입력: [2, 1, 3, 5, 4]
# 출력: [3, 3, 5, -1, -1]
import time
import random

def find_bigger_nums(stacks):
    stk = [] # 결과 저장 스택

    for i in range(len(stacks)):
        found = False # i보다 큰 수 찾았나. 찾으면 True

         # 현재 위치 i의 오른쪽을 모두 검사
        for j in range(i+1, len(stacks)):
            if stacks[j] > stacks[i]:
                stk.append(stacks[j])
                found = True
                break

        if found == False: # i보다 큰 수가 없으면 -1 추가하기
            stk.append(-1)

    return stk

testlist = [2,3,1,6,4,9,11]

# 테스트 실행
print(find_bigger_nums(testlist))
