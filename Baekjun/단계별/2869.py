A, B, V = map(int, input().split())
day = (V - B)/(A - B)  # A*day - B*(day-1) = V 를 정리
print(int(day) if day == int(day) else int(day)+1)

# 타 소스
print((V-B-1) // (A-B) + 1)
# 달팽이는 하루에 A-B미터씩 총 V미터 올라가야됨
# 목표 지점에 도달한 날에는 미끄러진거 고려하면 안되므로 총 V-B 미터를 올라가는 것
# 만약 V-B 가 A-B로 나눠떨어지지 않는다면 +1 한것이 정답 -> 근데 int형이라 나눠떨어지는지 구분해서 if문 쓰기 싫으니 미리 1 빼놓고 몫에 무조건 1 더하는것으로 처리