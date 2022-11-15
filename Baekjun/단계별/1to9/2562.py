numbers = []
for i in range(9):
    numbers.append(int(input()))
max_num = max(numbers)
print(max_num)
print(numbers.index(max_num)+1)

# 모범 소스
l=[int(input())for i in range(9)]
print(max(l), l.index(max(l))+1)