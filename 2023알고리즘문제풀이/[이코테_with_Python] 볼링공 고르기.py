# <Q05> 볼링공 고르기

# my solution

n, k = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] != arr[j]:
            answer += 1
        elif arr[i] == arr[j]:
            continue

print(answer)
