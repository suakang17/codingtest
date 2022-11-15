A, B = map(int, input().split())
C = int(input())
if (B+C)>=60:
    if (A+int((B+C)/60))>23:
        print((A+int((B+C)/60))-24,(B+C-(60*int((B+C)/60))))
    else:
        print((A+int((B+C)/60)),(B+C-(60*int((B+C)/60))))
else:
    print(A, (B+C))