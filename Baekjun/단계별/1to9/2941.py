word = input()
kro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in kro:
    if i in word:
        word = word.replace(i, '1')
print(len(word))

# 타 소스
s=input()
print(len(s)-sum(map(s.count,['c=','c-','dz=','d-','lj','nj','s=','z='])))