import sys
t = int(input())
score = 0
for i in range(t):
    l = sys.stdin.readline().strip().split('X')
    score_list = []
    for j in l:
        if 'O' in j:
            for k in range(1, len(j)+1):
                score += k
            score_list.append(score)
        score = 0
    print(sum(score_list))

# 타 소스 (반복문 2중)
import sys
n = int(sys.stdin.readline())
for i in range(n):
    ox = sys.stdin.readline()
    oc = 0
    oc_t = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            oc += 1
        else:
            oc = 0
        oc_t += oc
    print(oc_t)