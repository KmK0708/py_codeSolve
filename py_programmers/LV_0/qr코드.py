def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
        else:
            continue
    return answer
codes = "rlawndud"
print(solution(3,1,codes))

