def solution(a,b,c,d):
    dice = [a,b,c,d] # 리스트 생성
    dice.sort() # 굴린결과 정렬

    if dice[0] == dice[3]: # a=b=c=d면
        return 1111 * dice[0] # 1111곱하기
    elif dice[0] == dice[1] and dice[2] == dice[3]: # aabb 인경우
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2]) #(p + q) × |p - q|
    # aaab or abbb
    elif (dice[0] == dice[1] == dice[2]) or (dice[1] == dice[2] == dice[3]):
        if dice[0] == dice[1] == dice[2]:
            # aaab
            same_dice = dice[0]
            diff_dice = dice[3]
        else:
            # abbb
            same_dice = dice[1]
            diff_dice = dice[0]
        
        # (10 × same + diff)2 점수 계산
        return (10 * same_dice + diff_dice)**2
    # 각자 다른 주사위면
    elif dice[0] != dice[1] and dice[1] != dice[2] and dice[2] != dice[3]:
        return dice[0]
    #aabc일경우
    else:
        if dice[0] == dice[1]: # b * c
            return dice[2] * dice[3]
        elif dice[1] == dice [2]:
            return dice[0] * dice[3]
        else:
            return dice[0] * dice[1]
    
print(solution(6,3,3,6))