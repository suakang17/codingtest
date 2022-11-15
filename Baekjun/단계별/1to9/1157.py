import sys
word = list(sys.stdin.readline().strip().upper())
unique_word = list(set(word))

lettercnt = []
for i in unique_word:
    lettercnt.append(word.count(i))

if lettercnt.count(max(lettercnt)) > 1:
    print('?')
else:
    print(unique_word[lettercnt.index(max(lettercnt))])

# 타 소스
i = input().upper();
n = 0
for p in map(chr, range(65, 91)):
  q = i.count(p)
  if n < q:
      n, c = q, p
  elif n == q:
      c = "?"
print(c)