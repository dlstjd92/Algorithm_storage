from collections import deque

def solution(nodes, edges):
    n = len(nodes)
    # 1) 노드 값을 0..n-1로 매핑
    id_map = {v: i for i, v in enumerate(nodes)}
    
    # 2) degree 계산 및 인접 리스트 구성
    deg = [0] * n
    adj = [[] for _ in range(n)]
    for a, b in edges:
        u, v = id_map[a], id_map[b]
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    visited = [False] * n
    odd_even_cnt = 0
    inv_odd_even_cnt = 0

    # 3) 컴포넌트별 BFS
    for i in range(n):
        if visited[i]:
            continue
        queue = deque([i])
        visited[i] = True

        cnt1 = 0  # 홀짝 트리 조건: deg%2 == node%2 인 정점의 수
        cnt2 = 0  # 역홀짝 트리 조건: deg%2 != node%2 인 정점의 수

        while queue:
            u = queue.popleft()
            g = deg[u] & 1          # deg(u) mod 2
            v_parity = nodes[u] & 1 # u mod 2

            if g == v_parity:
                cnt1 += 1
            else:
                cnt2 += 1

            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    queue.append(w)

        # 4) 컴포넌트 단위 결과 집계
        if cnt1 == 1:
            odd_even_cnt += 1
        if cnt2 == 1:
            inv_odd_even_cnt += 1

    return [odd_even_cnt, inv_odd_even_cnt]