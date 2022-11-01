# import sys
# n = int(sys.stdin.readline().strip())
# wordlist = []
# chrlist = []
# for i in range(n):
#     chrlist = []
#     word = sys.stdin.readline().strip()
#     for c in word:
#         if c not in chrlist:
#             chrlist.append(c)
#         else:
#             if word[int(word.index(c) + 1)] == c or word[int(word.index(c) - 1)] == c: # 이부분 작동안함
#                 print(word[word.index(c)+1])
#                 chrlist.append(c)
#     if ''.join(chrlist) == word:
#         wordlist.append(word)
# print(len(wordlist))

# 정답 소스 1
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:
        group_word += 1  # error가 0이면 그룹단어
print(group_word)

# 정답 소스 2
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# 정답 소스 3
word=[]
num=int(input(""))

for i in range(num):
    word=input("")
    for j in range(1,len(word)):
        if word.find(word[j-1])>word.find(word[j]):
           num-=1
           break
print(num)

# 정답 소스 4
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
