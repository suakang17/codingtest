n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # board = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]


# dfs로 특정 노드 방문한 뒤에 연결된 모든 노드들 방문하는 함수 작성하기
def dfs(x, y):
    # 범위 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 해당 노드 상하좌우의 연결 노드도 재귀로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True  # 재귀함수에 의해 리턴된 값을 호출한 Caller에서 쓰지 않았으므로, 해당 값은 버려짐
    return False


# 모든 노드에 대해 음료수 채우기
ice = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:  # line21의 True를 받아 쓰는 것
            ice += 1

print(ice)
