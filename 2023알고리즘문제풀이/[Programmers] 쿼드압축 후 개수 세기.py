# my solution (X)

# another solution : "재귀 함수"를 이용한 풀이입니다..!!

def solution(arr):
    global answer
    # -->> 즉, "global answer" 선언을 해줌으로써 answer라는 변수는 전역변수가 되었습니다..!!
    # 즉, 아래 참고 문헌 내용의 2번에 해당합니다..!!
    answer = [0, 0]
    # answer[0] : 0의 갯수
    # answer[1] : 1의 갯수
    quad(arr, answer, len(arr))
    return answer

def quad(arr, s, n):
    x, y, tg = s[0], s[1], arr[s[0]][s[1]]
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != tg:
                quad(arr, [x, y], n//2)
                quad(arr, [x, y+n//2], n//2)
                quad(arr, [x+n//2, y], n//2)
                quad(arr, [x+n//2, y+n//2], n//2)
                return # <-- 여기서, "return"문을 통해 종료해줘야만 25행을 수행하지 않기 때문입니다..!!
    answer[tg] += 1 # <<-- 이 경우는 내부에 있는 모든 수가 같은 값을 가지는 경우입니다..!!

# "global" 키워드 관련 참고 문헌 : https://codingpractices.tistory.com/entry/Python-%EC%A0%84%EC%97%AD-%EB%B3%80%EC%88%98-%EC%A7%80%EC%97%AD-%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%B4%9D-%EC%A0%95%EB%A6%AC-global-nonlocal
# 참고 > [Python] 전역변수, 지역변수 사용법 총 정리 / global, nonlocal
# 1. 전역변수를 특정함수에 가져오기
#   함수 안에서 전역 변수의 값을 변경하려면 "global" 키워드를 사용해 선언을 해주면 된다..!!
# 2. 전역변수가 없는데 global 선언으로 전역 변수를 만드는 경우..!!
#   함수 안에 "global + 변수" 선언을 하면 해당 변수는 전역 변수가 됩니다..!!
