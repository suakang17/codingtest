import sys
N = int(input())
l = []
for i in range(N):
    l.append(sys.stdin.readline().strip())
l = list(set(l))
l.sort()
l.sort(key=len)
for word in l:
    print(word)

# 타 소스 lambda 정렬
words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))  # list내 튜플로 처리 -> hashable?

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 -> 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])