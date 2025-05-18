from collections import defaultdict
def solution(n, wires):
    answer = 999
    # 그래프를 순회하면서 노드를 끊기
    # 아 리턴값은 나눈 두 노드갯수의 차이
    
    # 가장 편한 방법은? 루트와 리프찾기.
    # 사실 모두 연결이 보장되어있기 때문에 루트는 아무거나 써도 됨->1번노드가 루트다
    # 이제 자기 자식노드의 갯수를 새면 됨
    
    
    
    graph = defaultdict(list)
    
    for start, to in wires:
        graph[start].append(to)
        graph[to].append(start)
        
    print(graph)
    node_num = [0]*n
    def dfs(node, visited):
        node_count=1
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                node_count+=dfs(i,visited.copy())
                
        node_num[node-1] = node_count
        return node_count
    
    print(dfs(1,set([1])), node_num)
    
    # 이제 순회돌면서 각 노드값과 차이 구하면서 제일 작은거 쓰면 됨
    # 최적의 로직이 아닌, 편한 로직을 구성해라
    # 솔직히 노드별로 전부 순회 돌아도 괜찮잖아
    for i in range(n):
        for j in graph[i+1]:
            if node_num[i]>node_num[j-1]:
                
                # 나는?
                parent = n-node_num[j-1]
                
                if node_num[j-1] > parent:
                    answer = min(node_num[j-1] - parent, answer)
                else:
                    answer = min(parent - node_num[j-1] ,answer)
                    
                print(answer)
    
    return answer