# my solution

# 참고 > 한국법에서는, "윤년"이란 그레고리력에서 여분의 하루인 2월 29일을 추가하여 1년 동안 날짜의 수가 366일이 되는 해를 말한다(천문법 제2조 제5호). 윤년에는 2월과 8월이 같은 요일로 시작된다.

def solution(a, b):
    answer = ''
    days = 0
    cld = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}
    days += b - 1
    for i in range(a - 1):
        days += cld[i]
    q, r = divmod(days, 7)
    answer = week[r]
    return answer
