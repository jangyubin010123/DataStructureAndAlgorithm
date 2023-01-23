# "파이썬 collections 모듈의 Counter 사용법"
# 참고1 > collections 모듈의 Counter 클래스는 사전 자료형과 매우 유사하며 비슷한 기능을 합니다..!!
# 참고2 > 파이썬 collections 모듈의 Counter 클래스는 사전 자료형과 달리 산술 연산자를 활용할 수 있는 특징이 있습니다..!!

# 이번 포스팅에서는 데이터의 개수를 셀 때 매우 유용한 파이썬의 collections 모듈의 Counter 클래스에 대해서 알아보겠습니다.

# "Counter 기본 사용법"
# collections 모듈의 Counter 클래스는 별도 패키지 설치 없이 파이썬만 설치되어 있다면 다음과 같이 임포트해서 바로 사용할 수 있습니다.
"""
from collections import Counter
"""
# Counter 생성자는 여러 형태의 데이터를 인자로 받는데요. -->> "먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 됩니다."

c = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
print(c)
# 출력결과 : Counter({'hi': 3, 'hey': 2, 'hello': 1})

# Counter 생성자에 문자열을 인자로 넘기면 각 문자가 문자열에서 몇 번씩 나타나는지를 알려주는 객체가 반환됩니다.

c = Counter("hello world")
print(c)
# 출력결과 : Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# "Counter를 사전처럼 사용하기"
# -->> "collections 모듈의 Counter 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 사용할 수 가 있습니다."
# 예를 들어, 대괄호를 이용하여 키로 값을 읽을 수 있고요..!!

counter = Counter("hello world")
print(counter["o"], counter["l"])
# 출력결과 : 2 3

# 특정 키에 해당하는 값을 갱신할 수도 있고요..!!

counter["l"] += 1
counter["h"] -= 1
print(counter)
# 출력결과 : Counter({'l': 4, 'o': 2, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, 'h': 0})

# if문에서 "in" 키워드를 이용하여 특정 키가 카운터에 존재하는지를 확인할 수 있습니다..!!
"""
if "o" in counter:
    print("o in counter")

del counter["o"]

if "o" not in counter:
    print("o not in counter")
"""

# "사전으로 Counter 흉내하기"
# Counter를 사용하는 것은 쉽지만 -->> Counter를 만드는 것은 그만큼 간단하지는 않습니다.
# 일반 사전을 이용하여 어떤 단어가 주어졌을 때 단어에 포함된 각 알파벳의 글자 수를 세어주는 함수를 작성해보겠습니다..!!

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

print(countLetters("hello world"))
# 출력결과 : {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# "가장 흔한 데이터 찾기" -->> 즉, "most_common()" 함수를 활용하여 데이터가 많이 나온 순으로 정렬된 배열을 리턴해줄 수 있습니다..!! + 추가로, 인자에 숫자 K를 넣으면 그 수 만큼 데이터를 잘라서 배열 형태로 리턴해줍니다..!! -->> 즉, 많이 나온 데이터 순대로 K개 잘라줌..!!
# 아마도 실전에서 Counter가 자주 쓰이는 경우는 가장 많이 나온 데이터나 가장 적게 나온 데이터를 찾을 때일 것일 텐데요.
# Counter 클래스는 이와 같은 작업을 좀 더 쉽게 할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common() 메서드를 제공하고 있습니다.

from collections import Counter
print(Counter("hello world").most_common())
# 출력결과 : [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

# 이 메서드의 인자로 숫자 K를 넘기면 그 숫자 만큼만 리턴하기 때문에, 가장 개수가 많은 K개의 데이터를 얻을 수도 있습니다.

from collections import Counter
print(Counter("hello world").most_common(1))
# 출력결과 : [('l', 3)]

# -->> "즉, Counter의 'most_common()' 함수가 없었다면 가장 많이 나온 데이터를 구하려면 함수를 직접 작성해야 하는 불상사가 생겼을 것이다..!!"

# "산술 연산자 활용"
# Counter가 재밌는 부분은 바로 마치 숫자처럼 산술 연산자를 사용할 수 있다는 것인데요..!!
# 예를 들어, 아래와 같이 2개의 카운터 객체가 있을 때,

counter1 = Counter(["A", "A", "A"])
counter2 = Counter(["A", "B", "B"])

# 이 두 객체를 더할 수도 있고요..!! -->> 신기한 듯..!!

print(counter1 + counter2)
# 출력결과 : Counter({'A': 4, 'B': 2})

# 물론 두 객체를 뺄 수도 있습니다..!!
# 뺄셈의 결과로 0이나 음수가 나온 경우에는 최종 카운터 객체에서 제외가 되니 이 부분은 주의해서 사용하시길 바랍니다..!!

counter1 = Counter(["A"])
counter2 = Counter(["A", "B", "B"])
print(counter1 - counter2)
# 출력결과 : Counter()
