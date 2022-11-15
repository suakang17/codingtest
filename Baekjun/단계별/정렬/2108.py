# # 내 소스 - 포기
# # 계수정렬로 효율적으로 처리하기 -> 절댓값MAX 4000 -> 8001 size list needed
# import sys
# N = int(sys.stdin.readline())
# num_index_list = [0]*8001
# numsum = 0
# maxcount = 0
# maxcountnumlist = []
# maxnum = -4001
# minnum = 4001
# for i in range(N):
#     inputnum = int(sys.stdin.readline())
#     num_index_list[inputnum + 4000] += 1  # 음수일 가능성 존재하므로 인덱싱 4000씩 밀어서 처리
#     numsum += inputnum  # 산술평균 대비
#
#     if num_index_list[inputnum + 4000] > maxcount:
#         maxcount = num_index_list[inputnum + 4000]  # MAX 등장횟수
#
#     if inputnum > maxnum:  # 최댓값
#         maxnum = inputnum
#     if inputnum < minnum:  # 최솟값
#         minnum = inputnum
#
# # 산술평균
# print("산술평균", format(numsum/N, ".0f"))
#
# # 중앙값
# num_list_4000 = []  # 정렬된 순서의 4000더해진 숫자 담을 리스트
# num_list = []  # True number list
# midindex = N//2  # 중앙값 인덱스 -> 인덱싱이 -4000~4000인거 고려하기 -> 등장한 값들만 추려야
# # for j in num_index_list:
# #     if j > 0:
# #         #num_list.append(num_index_list.index(j)-4000)  # 한가지값만 담기는데 이 경우는 값이 중복되어 가장 처음으로 해당 j값이 등장하는 위치 반환하기 때문
# num_list_4000 = list((filter(lambda x: num_index_list[x] != 0, range(len(num_index_list)))))
# # print(num_list_4000)  # for debugging
# for j in num_list_4000:
#     num_list.append(j-4000)
# # print(num_list)  # for debugging
# print("중앙값", num_list[midindex])  # 중복값 처리안됨 ㅁㅊ!!!!!!
#
# # 최빈값
# maxcntnumlist = []
# for k in range(len(num_index_list)):
#     if num_index_list[k] == maxcount:  # k == 등장횟수
#         maxcntnumlist.append(k - 4000)
# if len(maxcntnumlist) == 1:
#     print("최빈값", maxcntnumlist[0])
# else:
#     print("최빈값", maxcntnumlist[1])
#
# # 범위
# print("범위", maxnum - minnum)

# 타 소스
# 음수를 포함해서 정렬시키는 방법을 써야합니다.
# 전에 써먹은 카운팅 정렬을 개량해서 사용합시다.
# 최빈값이 문제입니다. 최빈값 끼리도 모아서 정렬을 시켜야합니다.

import sys

# 입력의 수
n = int(sys.stdin.readline())
# 수의 범위는 -4000~+4000입니다. 배열의 크기는 8001이면 충분합니다.
arr = [0]*8001
avg = 0
many = 0
# for문을 돌려서 수를 입력받읍시다.
for _ in range(n) :
    num = int(sys.stdin.readline())
    # 입력받은 수가 음수일 수도 있으니 +4000을 해서 배열에 넣어줍니다.
    arr[num+4000] += 1
    # 겸사겸사 최빈값의 출연횟수를 구해줍니다.
    if arr[num+4000] > many :
        many = arr[num+4000]
    # 겸사겸사 평균산술을 구해줍시다.
    avg+=num

# 평균산술을 규정합니다.
avg = round(avg/n)
# 중앙값의 인덱스를 구해줍니다.
middle_idx = n//2+1
middle = 0
# 최빈수의 리스트를 선언
many_arr = []

min = -10000
max = 0
cnt = 0
for (index, value) in enumerate(arr) :
    if arr[index] != 0 :
        # 최솟값 구하기
        if min == -10000 :
            min = index
        # 최댓값 구하기
        max = index
        # 최빈값 리스트에 넣기
        if value == many :
            many_arr.append(index)
        for _ in range(value) :
            cnt += 1
            # 중앙값 구하기
            if cnt == middle_idx :
                middle = index
# 산술 평균 출력
print(avg)
# 중앙값 출력
print(middle-4000)
# 최빈값 리스트 출력
if len(many_arr) > 1 :
    print(many_arr[1]-4000)
else :
    print(many_arr[0]-4000)
# 범위 출력
print(max-min)