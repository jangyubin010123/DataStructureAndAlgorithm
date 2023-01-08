from math import gcd 
def solution(arr):
    answer = 0
    for i in range(0, len(arr) - 1):
        temp1 = gcd(arr[i], arr[i+1])
        temp2 = temp1 * (arr[i] // temp1) * (arr[i+1] // temp1)
        arr[i+1] = temp2
    
    answer = arr[len(arr) - 1]
        
    return answer
