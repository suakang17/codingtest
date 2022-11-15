a = [int(input()) for i in range(10)]  # 한번에 나머지로 저장 불가? > 가능 : 문법 틀린듯 확인해보기
b = []
for i in a:
    b.append(i % 42)
c = set(b)
print(len(c))

# 타 소스
b = [int(input())%42 for i in range(10)]
print(len(set(b)))

# 타 소스 - sys.stdin input
import sys
a = set()
for i in sys.stdin:
    a.add(int(i)%42)
print(len(a))