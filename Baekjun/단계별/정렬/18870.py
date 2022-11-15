# 시간초과 - 파이썬3, pypy3
import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().strip().split()))
l_sorted = sorted(set(l))
for i in l:
    print(l_sorted.index(i), end=' ')  # .index() : O(N) -> 시간 초과

# 모범 소스
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))  # 중복제거, 오름차순 정렬

dic = {arr2[i] : i for i in range(len(arr2))}  # {dict[요소]: 요소의 인덱스}
for i in arr:
    print(dic[i], end = ' ')

