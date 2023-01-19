# 제한 사항 : number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.
# 문제 설명 : "XYZ 마트에서 15일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인 경우에 대해 알아봅시다." -->> "즉, 셋째날까지 회원가입을 할 수 없게 되는 상황이라면 남은 회원가입 가능 일수는 넷째 날과 다섯 째날과 여섯 째날만 남은 것입니다..!!" -->> "왜냐하면 일곱 째날부터는 10일이 안되기 때문입니다..!!" -->> ....
def solution(want, number, discount):
    answer = 0
    d = {}
    for i in range(len(want)):
        d[want[i]] = i
    # -->> 즉, 바나나 : 0, 사과 : 1, 쌀 : 2, 포크 : 3, 포트 : 4 와 같이 번호를 부여합니다..!!
    
    for i in range(len(discount)):
        check = discount[i:i+10:1] # <<-- 해당 날짜부터 10일간 비교해야 되기 때문입니다..!!
        # 즉, 할인 기간은 한 싸이클처럼 계속 반복해서 도는 것이 아닌 문제의 예시처럼 할인 기간이 15일이라고 하면 딱 15일 동안만 할인을 하는 것이기 때문에 여섯 째 날까지만의 상황들만 고려하면 됩니다..!!
        if len(check) < 10: # <<-- 만약 해당 날짜부터 10일이 안되면 원하는 수량을 못 맞추기 때문에 비교할 필요가 없으므로 바로 for문을 탈출해줍시다..!!
            break
        copy_number = [0] * len(number)
        for j in range(0, 10): # 참고 > len(check) == 10
            if check[j] in d:
                copy_number[d[check[j]]] += 1
        if copy_number == number:
            answer += 1            
    return answer
