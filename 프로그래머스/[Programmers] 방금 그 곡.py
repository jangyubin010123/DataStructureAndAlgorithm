# my solution

# my thoughts : "#"이 포함된 상태에서 (입력으로 받은) m이 악보 정보에 있는지 판별하기 어려우므로 "A#" -->> "a" 즉, "#"이 포함된 음은 소문자로 바꿔서 비교하면 편리하게 문제를 풀 수 있을 것입니다..!!

def solution(m, musicinfos):
    answer = ''
    m = m.replace("A#","a")
    m = m.replace("C#","c")
    m = m.replace("D#","d")
    m = m.replace("F#","f")
    m = m.replace("G#","g")
    
    for i in range(len(musicinfos)):
        # 참고 > 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
        # 만약 제목에 #이 있을 수도 있으니 혹시 몰라서 변경 범위를 음으로 제한하였습니다..!!
        musicinfos[i] = musicinfos[i].split(",")
        musicinfos[i][3] = musicinfos[i][3].replace("A#","a")
        musicinfos[i][3] = musicinfos[i][3].replace("C#","c")
        musicinfos[i][3] = musicinfos[i][3].replace("D#","d")
        musicinfos[i][3] = musicinfos[i][3].replace("F#","f")
        musicinfos[i][3] = musicinfos[i][3].replace("G#","g")
        musicinfos[i] = ",".join(musicinfos[i])
    
    # print(m)
    # print(musicinfos) <<-- 여기까지 ok..!!
    
    answer_list = []
    
    for i, music in enumerate(musicinfos):
        music = music.split(",")
        before = music[0]
        after = music[1]
        name = music[2] 
        eums = music[3]
        before = before.split(":")
        after = after.split(":")
        # print(after) # 출력결과 ex : ['12', '14']
        # print(before) # 출력결과 ex : ['12', '00']
        # -->> 이제 각각마다 음악이 재생된 시간을 구하면 됩니다..!!
        a_t = int(after[0]) * 60 + int(after[1])
        b_t = int(before[0]) * 60 + int(before[1])
        t = a_t - b_t # -->> 여기까지 ok..!!
        q = t // len(eums) # q : quotient
        r = t % len(eums) # r : remainder
        # print(q)
        # print(r)
        eums = eums[::1] * q + eums[0:r:1]
        # print(eums) -->> 여기까지 ok..!!
        if m in eums:
            # 참고 > 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
            answer_list.append((name, -t, i))
    # print(answer_list)
    
    # 참고 > 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
    if len(answer_list) == 0:
        return "(None)"
    
    answer_list.sort(key = lambda x : (x[1], x[2]), reverse = False)
    answer = answer_list[0][0]
    return answer
