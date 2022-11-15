# 내장함수 사용 ver.
nstring = list(input())
nstring.sort(reverse=True)
print(''.join(nstring))

# 내장함수 안쓰기 - 삽입 정렬 ver.
import sys
nstring = list(map(int, sys.stdin.readline().strip()))
for i in range(1, len(nstring)):
    while (i > 0) & (nstring[i] > nstring[i-1]):
        nstring[i], nstring[i-1] = nstring[i-1], nstring[i]
        i -= 1
for j in nstring:
    print(j, end='')