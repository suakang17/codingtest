n, k = map(int, input().split())
l = list(map(int, input().split()))

for j in range(1, len(l)):  # 삽입 역정렬 사용하는 경우
    while (j > 0) & (l[j] > l[j - 1]):
        l[j], l[j - 1] = l[j - 1], l[j]
        j -= 1

print(l[k - 1])

# 내장함수 sort 사용하는 경우
l.sort(reverse=True)
print(l[k-1])