import sys
c = int(input())
for i in range(c):
    l = sys.stdin.readline().split()
    ll = []
    for k in l:
        ll.append(int(k))  # l은 str으로 저장되므로 int list인 ll로 전환
    heads = ll[0]
    del ll[0]
    avg = sum(ll)/len(ll)
    cnt = 0  # 평균 넘는 학생 수
    for j in ll:
        if j > avg:
            cnt += 1
    ratio = cnt/heads*100
    print(str(format(ratio, ".3f"))+'%')

# 타 소스
import sys
for _ in range(int(sys.stdin.readline())):  # readline으로 str으로 받은거 int로 먼저 바꾸고
    a = list(map(int,sys.stdin.readline().strip().split()))  # 그 다음 strip, split
    mean = sum(a[1:len(a)])/a[0]
    print('%.3f'%round(sum(map(lambda x:x>mean, a[1:len(a)]))/a[0]*100,4)+"%")