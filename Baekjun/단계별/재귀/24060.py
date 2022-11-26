# 병합정렬 구현
global cnt  # 몇번째 저장되는지 확인 위함
cnt = 0
global knum
knum = 0
def merge_sort(arr):
    global cnt
    global knum
    if len(arr) <= 1:
        return arr

    mid = (len(arr)+1)//2  # !!주의!!: 문제에서는 홀수크기 배열인 경우 병합시 앞(low_arr)이 크도록 병합함
    low_arr = merge_sort(arr[:mid])  # 쪼갠 배열 사이즈 1 될 때까지 재귀호출
    high_arr = merge_sort(arr[mid:])  # 사이즈 1 된 다음에 mergint start

    merged_arr = []
    l = h = 0  # low_arr, high_arr 's index
    while (l < len(low_arr)) and (h < len(high_arr)):  # 두 배열 중 하나가 완전히 병합될 때까지
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            cnt += 1
            if cnt == K:
                knum = low_arr[l]
            l += 1
        else:
            merged_arr.append(high_arr[h])
            cnt += 1
            if cnt == K:
                knum = high_arr[h]
            h += 1
    # when one of low or high absolutely merged... append latter
    while l < len(low_arr):
        merged_arr.append(low_arr[l])  # 0부터 시작해서 +=1로 커지다가 멈춘 순간의 인덱스부터
        cnt += 1
        if cnt == K:
            knum = low_arr[l]
        l += 1
    while h < len(high_arr):
        merged_arr.append(high_arr[h])
        cnt += 1
        if cnt == K:
            knum = high_arr[h]
        h += 1
    return merged_arr


import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())  # (5 ≤ N ≤ 500,000), (1 ≤ K ≤ 10^8)
arrA = list(map(int, input().strip().split()))  # (1 ≤ Ai ≤ 10^9)
merged_arr = merge_sort(arrA)

if cnt < K:
    print(-1)
else:
    print(knum)