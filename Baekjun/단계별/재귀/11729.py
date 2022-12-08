# 1단계: 1번에 있는 n-1개 1->2
# 2단계: 남은 1개 막대 1->3
# 3단계: 2번에 있는 n-1개 2->3

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

n = int(input())
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)

#  hanoi(n, a, b, c)의 의미는 n개의 블록이 a에 쌓여있는 걸 c로 옮길 것이며
#  남은 하나의 기둥이 b라는 뜻이고,
#  하노이 탑 공식에 의해 그 과정은 크게
#  1. "n-1개를 a에서 b로 옮기고"
#  2. "남은 1개를 a에서 c로 옮기고"
#  3. "n-1개를 b에서 c로 옮기는" 것으로 나눌 수 있고,
#  이것을 그대로 재귀호출 - 출력 - 재귀호출로 나타낸 것