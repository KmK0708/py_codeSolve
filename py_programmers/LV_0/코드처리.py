# 문자열 code 가 주어진다. code를 앞부터 읽으면서 문자가 "1" 이면 mode를 전환한다. mode 에는 0 과 1 이 있다.
# 문자열을 읽으면서 새로운 문자열(new code)을 만든다.
# mode가 0이면 문자열 짝수 인덱스에 있는 문자를 new code에 넣는다.
# 1이면 홀수 인덱스 문자를 new code에 추가 
# 시작할때 mode는 0, 만약 문자열이 아무것도 못받앗다면 EMPTY 출력하게한다.
def solution(code):
    mode = 0 
    answer = '' # 새로운 문자열
    for idx,char in enumerate(code): # 받은 문자열을 enumerate로 인덱스와 문자를 순회한다
        if char == '1': # 문자에 1이 들어가있다면
            if mode == 0: # 그리고 mode 가 0 이면
                mode = 1 # 1로 바꿈
            else:
                mode = 0 # 0으로 바꿈
        else: # 문자열에 1없으면
            if mode == 0 and idx % 2 == 0: # mode 가 0 이고 idx가 짝수면
                answer += char # 짝수 인덱스 문자 추가
            elif mode == 1 and idx % 2 == 1: # 1이고 홀수면
                answer += char # 홀수 인덱스 문자 추가

    if answer == '': # 저 위 조건을 만족못해서 아무것도 저장못했으면
        return 'EMPTY' # empty 반환
    
    return answer

s = "te1st1qwe"

print(solution(s))