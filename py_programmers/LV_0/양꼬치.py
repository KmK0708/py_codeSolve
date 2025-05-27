# 문제 설명
# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
# 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

def solution(n, k):
    # 꼬치 가격 12000원
    kkochi = n * 12000
    
    # 무료음료는 10개당 1개
    free_drink = n // 10
    
    # 실제 음료 가격
    drinkpay = k - free_drink
    if(drinkpay < 0): #시킨 음료보다 이벤트 음료가 더많으면 가격 x
        drinkpay = 0
    
    #음료 가격
    drink_cost = drinkpay * 2000
    
    #총 가격
    allpaid = kkochi + drink_cost
    
    return allpaid

print(solution(10, 3))  # 양꼬치 10인분, 음료수 3개 → 124,000원
print(solution(64, 6))  # 양꼬치 64인분, 음료수 6개 → 768,000원
