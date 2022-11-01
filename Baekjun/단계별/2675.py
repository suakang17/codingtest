import sys
for i in range(int(sys.stdin.readline())):
    times, word = sys.stdin.readline().strip().split()
    for j in word:
        print(j*int(times), end='')
    print()