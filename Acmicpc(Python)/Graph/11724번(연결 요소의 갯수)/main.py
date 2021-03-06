from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 만들기
for _ in range(m):
    x, y = map(int, input().split())

    # graph[x] 에 append(y), graph[y] append(x) 하는 게무슨 의미인지..?
    # --> 간선정보를 입력해주는 것

    # --> x : 1, y : 5 라는 입력값이 있을 때
    # --> 1번 노드와 5번 노드를 연결시켜주는 것이다.
    graph[x].append(y)
    graph[y].append(x)

print(graph)

# bfs 는 큐에서 하나씩 pop을 해가면서, pop 을 했을 때 그 원소가 가리키고 있는 원소를 또 들어갈 것임

def bfs(start):
    # 큐에 시작하는 노드 넣기
    queue = deque([start])
    
    # 방문 시작노드 방문 처리
    visited[start] = True
    
    # 큐가 비어있을때 까지 반복
    while queue:
        # 탐색할 노드는 큐에서 하나씩 꺼내갈것임
        node = queue.popleft()
        # i = 해당 노드가 연결되어 있는 다른 노드를 가리킨다.
        for col in graph[node]:
            # 그 i 가 방문처리 되지 않았다면
            if not visited[col]:
                # 방문 처리 해주고,
                visited[col] = True
                # 큐에 삽입한다.
                queue.append(col)


# 노드 갯수만큼 반복 리스트 생성
visited = [False] * (1 + n)

# 연결 요소 갯수
count = 0

# 1 ~ N번 노드를 순회

for i in range(1, n + 1):
    # 만약 방문하지 않았다면
    if not visited[i]:
        # 만약 그래프가 비어있다면
        # 연결 요소 갯수  +1 --> 그래프가 비어있다는 것은, 그 노드가 다음으로 이어진 내용이 없다는 것
        # 방문 처리
        if not graph[i]:
            count += 1
            visited[i] = True
        # 만약 그래프가 비어있지 않다면 --> 다른 노드와 이어진 것이 있음
        else:
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결 요소 갯수 +1

print(count)