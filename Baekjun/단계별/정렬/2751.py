# 내장함수 sort이용
# import sys
# N = int(sys.stdin.readline().strip())
# l = []
# for i in range(N):  # O(N)
#     l.append(int(sys.stdin.readline().strip()))  # O(1)
# l.sort()  # O(N log N)
# for j in l:  # O(N)
#     print(j)
#
# # 타소스 내장함수 sort
# from sys import stdin, stdout
# input()
# arr = sorted(list(map(int, stdin.read().split())))
# stdout.write('\n'.join(map(str,arr)))

# 병합정렬 이용 소스
import sys
# 병합정렬 함수    
def merge_sort(array):
    if len(array) <= 1:
        return array

    # 재귀호출 통해 원소 개수 1개씩이 될 때까지 분할
    mid = len(array)//2  # 원본배열길이의 절반
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0

    # 분할된 배열끼리의 비교
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # 먼저 끝났을 때 남은거 가져다 붙이기
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


N = int(input()); l = []
for i in range(N):
    l.append(int(sys.stdin.readline().strip()))

l = merge_sort(l)
for j in l:
    print(j)