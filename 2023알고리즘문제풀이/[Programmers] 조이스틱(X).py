# [Programmers] 조이스틱.py

# my solution(X) -->> "다음에 다시 한번 더 풀어볼 것..!!"

# another solution : 즉, "그리디"하게 풀기 보다는 "완전탐색"을 이용한 풀이라고 볼 수 있을 것 같습니다..!!
# 또한 문제의 조건 중 name의 최대 길이가 20이므로 "완전탐색"을 통해 "A"가 아닌 곳을 가는 모든 경우의 수를 구한 뒤 조이스틱을 좌, 우로 움직이는 최단 거리를 구하는 방식으로 접근하신 것 같습니다..!!

# 다음의 티스토리 블로그 사이트를 참조하였습니다..!!
# -->> "https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Python"

# [풀이]
# 해당 문제는 프로그래머스의 그리디 유형으로 올라온 문제인데.. ....
# 그리디로 풀었던 방법은 현재 위치를 기준으로 "A"가 아닌 곳 중 가장 짧은 곳으로 가서 변경하고 이를 반복하는 작업을 했습니다.
# 그런데 이런식으로 풀면 반례가 생깁니다..!!

# 대표적으로 "BBBBAAAABA"가 있습니다.
# * 그리디 방식을 사용할 경우 아래와 같이 움직여야 합니다.
#   * >>><<<<< (8번)
# * 하지만, 실제 최소 좌우 움직임은 아래와 같습니다.
#   * <<>>>>> (7번)

# -->> 따라서 풀이 방식을 고민하다가 입력으로 주어지는 문자열의 최대 길이가 20이기 때문에 "완전 탐색"을 고려하게 되었습니다..!!
# 그리고 이를 통해 정답을 얻었습니다.
# 해당 문제를 풀때 편의를 위해 두 개의 추가 함수를 만들었습니다.
# * 알파벳이 주어졌을 때 상,하로 움직여야 하는 횟수를 구하는 함수 (countChange) 
# * 현재 위치에서 -->> 목표 위치로 갈 때 최소로 가려면 왼쪽으로 가야 하는지, 오른쪽으로 가야 하는지 확인하고 둘 중 최단 경로의 거리가 얼마인지 구하는 함수 (findShortestPath) 

# "완전 탐색"
# 완전 탐색 방식은 다음과 같습니다.
# * 가야할 곳은 "A"가 아닌 곳입니다.
# * 따라서 "A"가 아닌 곳의 인덱스를 전부 찾은 뒤(시작 위치 제외) 해당 인덱스들을 모두 방문하는 모든 경우의 수, 즉 순열을 구합니다..!!
# 각 순열에 따라 이동 거리를 구해보고 이를 가지고 정답을 갱신합니다.
# 모든 순열 중 최소 이동 거리가 나온 것이 문제에서 요구한 정답이 됩니다.

# 풀이 코드는 아래와 같습니다.

from itertools import permutations as p

INF = int(1e9)

# 알파벳이 주어졌을 때 상하로 움직이는 횟수 구하는 함수
def countChange(alp):
    return min(ord('Z') - ord(alp) + 1, ord(alp) - ord('A'))

# 왼쪽, 오른쪽 중 최단으로 가는 거리 구하는 함수
def findShortestPath(name, now, next):
    right, left = max(next, now), min(next, now)
    Case1 = right - left
    Case2 = left + len(name) - right
    return min(Case1, Case2)

def solution(name):
    answer = INF
    # "A" 가 아니라서 가야하는 위치(시작 위치 제외)
    toGoPlaces = [i for i in range(len(name)) if name[i] != "A" and i != 0]

    # 알파벳을 바꾸느라 생기는 이동
    changeCount = 0
    for c in name:
        changeCount += countChange(c)

    # 움직일 수 있는 모든 케이스
    cases = p(toGoPlaces, len(toGoPlaces))
    for case in cases:
        now = 0
        result = 0

        for next in case:
            dist = findShortestPath(name, now, next)
            result += dist
            now = next
            
        answer = min(answer, result + changeCount)
    return answer
