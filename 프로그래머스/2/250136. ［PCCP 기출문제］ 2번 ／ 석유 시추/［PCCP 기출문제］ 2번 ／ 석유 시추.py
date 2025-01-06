def solution(land):
    n = len(land)
    m = len(land[0])
    parents = [i for i in range(n * m)]
    def is_parent(node):
        return node == parents[node]

    def get_parent(node):
        parent_candidate = parents[node]
        if is_parent(parent_candidate):
            return parent_candidate
        real_parent = get_parent(parent_candidate)
        parents[node] = real_parent
        return real_parent

    for child in range(n * m):
        i = child // m
        j = child % m
        if land[i][j] == 0:
            continue
        if j > 0 and land[i][j - 1] == 1:
            parent1 = get_parent(child)
            parent2 = get_parent(child - 1)
            if parent1 < parent2:
                parents[parent2] = parent1
                parents[child - 1] = parent1
            elif parent2 < parent1:
                parents[parent1] = parent2
                parents[child] = parent2
        if i > 0 and land[i - 1][j] == 1:
            parent1 = get_parent(child)
            parent2 = get_parent(child - m)
            if parent1 < parent2:
                parents[parent2] = parent1
                parents[child - m] = parent1
            elif parent2 < parent1:
                parents[parent1] = parent2
                parents[child] = parent2
    gas_amount_list = [0 for i in range(n * m)]
    col_gas_group_list = [set() for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                continue
            p = get_parent(i * m + j)
            gas_amount_list[p] += 1
            col_gas_group_list[j].add(p)

    max_cnt_sum = 0
    for j in range(m):
        gas_groups = col_gas_group_list[j]
        cnt_sum = 0
        for gas_group in gas_groups:
            cnt_sum += gas_amount_list[gas_group]
        if max_cnt_sum < cnt_sum:
            max_cnt_sum = cnt_sum

    return max_cnt_sum
