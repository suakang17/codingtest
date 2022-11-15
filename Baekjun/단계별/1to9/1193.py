x = int(input())
up = 1  # 1 2 3 4 ...
down = 1  # ... 4 3 2 1
num = 1  # 몇 번째 분수
row = 1  # 대각선 줄 수
if x != 1:
    while num != x:
        row += 1
        for i in range(1, row+1):
            up = i
            down = (row+1-up)
            num += 1
            if num == x:
                break
if row == 1 or (row%2) == 0 :
    print(str(up)+'/'+str(down))
else:
    print(str(down)+'/'+str(up))

# 타 코드
X = int(input())

line = 1
while X > line:  # X가 몇 번째 줄에 몇 번째 숫자인지 구함
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')