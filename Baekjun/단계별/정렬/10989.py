# 메모리 초과 소스
# import sys
#
# n = int(sys.stdin.readline())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(sys.stdin.readline()))
#
# sorted_list = sorted(num_list)
#
# for i in sorted_list:
#     print(i)

# 정답 소스 - 계수정렬(카운터정렬) pypy 메모리초과/ python 성공 pypy3의 경우 메모리 초과가 다시 발생한다. (코딩 테스트를 준비하는 경우 pypy3로도 실행해봐야 함...)
# pypy: 여기서 메모리를 추가적으로 사용하는 print문을 sys.stdin.write로 변경할 경우 정답으로 인정된다.
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001  # for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어지므로 
                        # 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트 생성해두기
for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1  # 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.

for i in range(10001):
    if num_list[i] != 0:  # 입력을 다 받고나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력
        for j in range(num_list[i]):
            print(i)