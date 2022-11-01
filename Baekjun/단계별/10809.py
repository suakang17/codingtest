s = input()
for i in range(97, 123):
    if chr(i) in s:
        print(s.index(chr(i)), end=' ')  # list.index(): 두 번 이상 원소가 중복되어 존재하는 경우에는 맨 처음 등장한 순간의 인덱스를 출력
    else:
        print(-1, end=' ')

# 타 소스 - 문자열 find 메서드
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')  # string.find(): 찾는 문자가 존재 한다면 해당 위치의 index를 반환해주고, 찾는 문자가 존재 하지 않는다면 -1 을 반환
    
# 타 소스 2 - 코드효율
print(*map(input().find, map(chr, range(97, 123))))