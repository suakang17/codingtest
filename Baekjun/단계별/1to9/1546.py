n = int(input())
grade = list(map(int, input().split()))
new = []
for i in grade:
    m = max(grade)
    new.append(i/m*100)
print(sum(new)/n)

# 타 소스 - 반복문 X
n = int(input())
list = list(map(int, input().split(' ')))
m = max(list)
print((sum(list)/m*100)/n)