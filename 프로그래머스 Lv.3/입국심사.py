# my solution1(X)
# 테스트케이스 3번부터 런타임 에러가 발생한 이유 : 문제의 제한사항에서 입국심사를 기다리는 사람의 최댓값은 10억이고 각 심사관이 한 명을 심사하는데 걸리는 시간은 최대 10억분이므로 만약 최악의 경우에 아래의 소스코드를 실행하게 된다면 "max(times) * n + 1"은 10억**2의 값을 나타내게 되어서 당연히 런타임 에러가 발생할 수 밖에 없을 것이다..!! -->> 따라서, start = 0, end = max(times) * n + 1와 같이 초깃값만 부여하고 리스트를 생성하지 않은 채 이분 탐색을 실행해야 할 것이다..!!
# (ex) print(list(range(0, 1_000_000_000**2)))
# 실행결과 : MemoryError
# -->> 실제로, VSC로 예제 코드를 실행해보니 "MemoryError"가 발생하는 것을 확인할 수 있었습니다..!!

"""
def solution(n, times):
    answer = 0
    arr = list(range(0, max(times) * n + 1)) # <<-- 결괏값으로 반환될 수 있는 시간의 모든 경우의 수들..!!
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        passed = 0
        for t in times:
            passed += arr[mid] // t
        if passed >= n:
            answer = mid
            end = mid - 1
        elif passed < n:
            start = mid + 1
    
    return answer
"""

# my solution2

# my thoughts : 위의 풀이처럼 arr리스트를 생성하지 않고 start, end 2개의 변수만 값 할당을 한 후 정렬된 배열에서 이분탐색을 실행하는 것처럼 문제에 다시 접근해보았습니다..!! -->> "Memory Error"를 피하기 위해서..!!

def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        passed = 0
        for t in times:
            passed += mid // t
        if passed > n:
            answer = mid # <<-- 다음 번의 while문을 수행 시 혹시 모를 상황에 대비해 그때그때마다 answer에 값을 저장해줘야 함..!!
            end = mid - 1 # <<-- 우리가 찾고자 하는 값은 모든 사람이 심사를 받는데 걸리는 시간의 "최솟값"이기 때문에 혹시 모를 상황을 대비해 while문을 한 번 더 돌아줘야 합니다..!!
        elif passed == n:
            answer = mid
            # <<-- 다음 번의 while문을 수행 시 혹시 모를 상황에 대비해 그때그때마다 answer에 값을 저장해줘야 함..!!
            end = mid - 1 # <<-- 우리가 찾고자 하는 값은 모든 사람이 심사를 받는데 걸리는 시간의 "최솟값"이기 때문에 혹시 모를 상황을 대비해 while문을 한 번 더 돌아줘야 합니다..!!
        elif passed < n:
            start = mid + 1
    
    return answer
