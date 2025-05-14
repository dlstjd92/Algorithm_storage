from collections import defaultdict, deque

def solution(edges):
    # 1) graph, in/out degree, 노드 집합 구성
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()

    for u, v in edges:
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v]  += 1
        nodes.add(u); nodes.add(v)

    # 2) added_node 찾기 (in_deg==0)
    added_nodes = [n for n in nodes if in_deg[n] == 0]
    # 여러 개일 때는 out_deg>=2 인 노드를 우선
    if len(added_nodes) > 1:
        for n in added_nodes:
            if out_deg[n] >= 2:
                added_node = n
                break
        else:
            added_node = added_nodes[0]
    else:
        added_node = added_nodes[0]

    # 3) 분류기(classifier) 정의
    def classify(start):
        node = start
        visited = {node}
        while True:
            children = graph[node]
            # 막대: 자식이 없으면
            if not children:
                return 2
            # 8자(정션): 자식이 둘 이상이면
            if len(children) > 1:
                return 3
            # 유일한 자식
            nxt = children[0]
            # 도넛: 바로 시작점으로 돌아오면
            if nxt == start:
                return 1
            # 그 외 순환(사이클 내부)도 8자 처리
            if nxt in visited:
                return 3
            visited.add(nxt)
            node = nxt

    # 4) 각 서브그래프 분류
    answer = [added_node, 0, 0, 0]  # [루트, 도넛, 막대, 8자]
    for child in graph[added_node]:
        kind = classify(child)
        answer[kind] += 1

    return answer