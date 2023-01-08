from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True) # 내림차순 정렬 시행
    dq = deque(people)
    while dq:
        if len(dq) == 1:
            dq.pop() # <==> dq.popleft()
            answer += 1
            continue
        sum_weight = dq[0] + dq[-1]
        if sum_weight > limit:
            dq.popleft()
            answer += 1
        elif sum_weight == limit:
            dq.popleft()
            dq.pop()
            answer += 1
        else:
            dq.popleft()
            dq.pop()
            answer += 1
    return answer
  
  # 참고 >
  """
  이번 문제는 투포인터를 생각하며 문제를 풀었다.

예시 2개를 보며 문제를 파악해보자

예시 1) people = [40, 40, 40, 50, 50, 60, 70, 80], limit = 100

이 예시는 보트에 (40, 60), (40, 50), (40, 50), (70), (80) 이렇게 총 5개의 보트가 필요하다.

예시는 애초에 정렬이 되어 있으나 문제의 테스트 케이스는 정렬이 되어 있지 않을 수 있으므로 우선 people을 정렬해주어야 한다.

우선 가장 첫 번째 원소와 가장 마지막 원소의 합을 limit와 비교한다.

40과 80을 비교해 100보다 같거나 작지 않다면 마지막 원소를 pop해주면서 answer += 1을 해준다. 왜냐면 people은 정렬이 되어있기 때문에 가장 마지막 원소는 가장 첫번째 원소와 같이 타지 못한다면 혼자 탈 수 밖에 없기 때문에 pop을 시켜주면서 answer를 하나 늘려주는 것이다.

이제 가장 마지막 원소는 70이 되었다.

40과 70의 합 역시 limit인 100을 초과한다. -> 가장 마지막 원소 즉 70을 pop 시켜 주면서 answer += 1을 해준다.

이제 가장 마지막 원소는 60이 되었다.

비로소 첫 번째 원소와 마지막 원소의 합이 limit와 같거나 작아졌다. 이 경우는 가장 큰 원소와 가장 작은 원소가 함께 보트를 탈 수 있으니 가장 첫 번째 원소와 마지막 원소를 함께 pop해주고 보트의 수를 하나 올려준다. 즉 answer += 1를 해준다. (이때 가장 왼쪽을 pop해줄때 효율적인 deque를 사용하여 시간복잡도를 줄여준다.)
"""
