answer_list = set()
n = int(input())

for i in range(0, n):
    str = input()
    answer_list.add(str)

answer_list = list(answer_list)
answer_list.sort(key = lambda x : (len(x), x), reverse = False)

for i in range(len(answer_list)):
    print(answer_list[i])
