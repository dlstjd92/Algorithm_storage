def heapify_up(heap, index):
    # 부모 노드 인덱스 계산
    parent = (index - 1) // 2
    # 부모보다 현재 노드가 작으면 교환
    if index > 0 and heap[index] < heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        heapify_up(heap, parent)


def heapify_down(heap, index):
    # 자식 노드 인덱스 계산
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    smallest = index

    # 왼쪽 자식이 더 작으면 갱신
    if left_child < len(heap) and heap[left_child] < heap[smallest]:
        smallest = left_child

    # 오른쪽 자식이 더 작으면 갱신
    if right_child < len(heap) and heap[right_child] < heap[smallest]:
        smallest = right_child

    # 가장 작은 값과 교환 후 재귀적으로 힙 정렬
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        heapify_down(heap, smallest)


def push(heap, value):
    # 값을 힙에 추가 후 위로 정렬
    heap.append(value)
    heapify_up(heap, len(heap) - 1)


def pop(heap):
    if not heap:
        raise IndexError("Heap is empty")

    # 루트값 반환 후 마지막 값을 루트로 이동
    root = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    if heap:
        heapify_down(heap, 0)
    return root


# 입력 처리
times = int(input())
card = []
for _ in range(times):
    card.append(int(input()))

# 최소 힙 초기화
heap = []
for value in card:
    push(heap, value)

# 계산
ans = 0
while len(heap) > 1:
    num1 = pop(heap)
    num2 = pop(heap)
    sumNum = num1 + num2
    ans += sumNum
    push(heap, sumNum)

print(ans)
