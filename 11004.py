"""
[문제]
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 
앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
--
[입력]
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
--
[출력]
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
"""
def partition(arr, low, high):
    pivot = arr[high]  # 피벗은 리스트의 마지막 원소로 선택합니다.
    i = low - 1  # 작은 원소들의 구역의 끝 인덱스를 나타내는 변수입니다.

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # 작은 원소를 작은 구역으로 이동합니다.

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 피벗의 위치를 조정합니다.
    return i + 1

def quicksort(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)

        # 피벗이 k번째 원소인 경우
        if pivot_index == k - 1:
            return arr[pivot_index]

        # 피벗이 k번째 원소보다 작은 경우
        if pivot_index < k - 1:
            return quicksort(arr, pivot_index + 1, high, k)

        # 피벗이 k번째 원소보다 큰 경우
        if pivot_index > k - 1:
            return quicksort(arr, low, pivot_index - 1, k)

    # 리스트 크기가 1인 경우
    return arr[low]

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 퀵 정렬 수행 및 결과 출력
result = quicksort(A, 0, N - 1, K)
print(result)