N = input()
origin_num = N
cycle = 0
sum = 0
new_num = 0
while True:
    try:
        sum = int(N[0]) + int(N[1])
    except:
        sum = int(N[0])

    new_num = int(N[-1] + str(sum)[-1])
    N = new_num
    if origin_num == new_num:
        cycle += 1
        break
    else:
        cycle += 1
print(cycle)
