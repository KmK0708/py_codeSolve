# 정수 하나가 주어지면, 각 자릿수를 스택을 이용해서 거꾸로 출력하는 프로그램을 만들어보세요.
# input = 12345 output = 5 4 3 2 1
def revNum():
    stk = [] # 빈 스택
    nums = int(input("숫자를 넣으세요 : "))

    for digit in str(nums):
        stk.append(digit)

    while stk:
        print(stk.pop())

revNum()    


