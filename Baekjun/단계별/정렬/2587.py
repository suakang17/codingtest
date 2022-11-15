import sys
l = []; sum = 0
for i in range(5):
    num = int(sys.stdin.readline().strip())
    sum += num
    l.append(num)

print(int(sum/5))
for j in range(1, len(l)):
    while (j > 0) & (l[j] < l[j-1]):
        l[j], l[j-1] = l[j-1], l[j]
        j -= 1
print(l[2])
