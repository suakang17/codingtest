import sys
global cnt


def recursion(s, l, r):  # 대상 문자열, 앞에서부터 문자인덱스, 뒤에서부터 문자인덱스
    global cnt
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):  # 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))s
# print('ABC:', isPalindrome('ABC'))


T = int(sys.stdin.readline())
for i in range(T):
    s = sys.stdin.readline().strip()  # 알파벳 대문자로 구성
    global cnt
    cnt = 0
    res1, res2 = isPalindrome(s)
    print(res1, res2)
