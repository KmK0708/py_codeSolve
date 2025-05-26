#정수 배열 arr와 query가 주어진다.

# query를 순회하면서 다음 작업을 반복한다.

# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버린다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버린다.

# 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성하라.
#       arr	            query      result
#[0, 1, 2, 3, 4, 5]	  [4, 1, 2]	  [1, 2, 3]

def solution(arr, query):
    for i in range(len(query)): # 쿼리를 for문으로 순회한다.
        if(i % 2 == 0): # 쿼리가 짝수면 
            arr = arr[:query[i]+1]  # 쿼리 인덱스 뒤로 자르기 (자신 제외)
            print(arr)
        else: #홀수면 
            arr = arr[query[i]:] # 쿼리 인덱스 앞부분 자르기
            print(arr)
        
    return arr

tst = [0, 1, 2, 3, 4, 5,6,7]
qry = [5,1,3]
print(solution(tst,qry))