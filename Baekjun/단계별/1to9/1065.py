n = int(input())
hansu = set()  # 한자리수 두자리수는 모두 한수

for i in range(1, n+1):
    if i < 100:
        hansu.add(i)
    else:
        str_n = str(i)
        if (int(str_n[0]) - int(str_n[1])) == (int(str_n[1]) - int(str_n[2])):
            hansu.add(i)
print(len(hansu))

# 타 소스: 세 수 a,b,c가 등차수열을 이룰때 a+c=2*b
print(sum(i<100 or i//10%10*2 == i%10+i//100 for i in range(1,int(input())+1)))
