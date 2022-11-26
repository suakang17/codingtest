import sys
input = sys.stdin.readline()
N = int(input); res = 1
while N > 0:
    res *= N
    N -= 1
print(res)