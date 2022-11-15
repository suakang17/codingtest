a, b = input().split()
s_a = ''.join(reversed(list(a)))  # list(a).reverse 의 type == None -> 반환값 없음// reversed(str): 반환값 O
s_b = ''.join(reversed(list(b)))
if s_a > s_b:
    print(s_a)
else:
    print(s_b)

# 타 소스 - 인덱싱 이용
a, b = input().split()

a = a[::-1]
b = b[::-1]

print(max(a, b))

# 타 소스 2 - for
a, b = input().split()
s_a = ''; s_b = ''
for c in a:
    s_a = c + s_a
s_a = int(s_a)

for c in b:
    s_b = c + s_b
s_b = int(s_b)

print(max(s_a,s_b))