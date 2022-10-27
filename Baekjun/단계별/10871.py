n, x = map(int, input().split())
list_a = list(map(int, input().split()))
for a in list_a:
    if a < x:
        print(a, end=' ')

# 다른 소스
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))