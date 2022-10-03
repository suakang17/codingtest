# ============================== 내 풀이
n = int(input())
result = 0
for hour in range(n+1):  # 0시 ~ n시
    if hour == 3 or hour == 13 or hour == 23:  # 시각에 3이 있는 경우
        result += (60*60)
    else:  # 시각에 3이 없는 경우
        result += (15*60)*2 - (15*15)  # 분에만 3 등장하는 경우, 초에만 3 등장하는 경우 - 교집합(분, 초 모두 3 등장하는 경우)
print(result)
# 시간 복잡도 최대 O(23)
# ============================== 모범 답안
n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
# 시간 복잡도 최대 O(23*60*60) == O(86400) 이므로 3중으로 접근해도 문제x