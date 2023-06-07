"""
[문제]
N개의 수 A1, A2, ..., AN과 L이 주어진다.
Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오.
이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.
--
[입력]
첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
둘째 줄에는 N개의 수 Ai가 주어진다. (-10^9 ≤ Ai ≤ 10^9)
--
[출력]
첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.
"""
# import sys
# input = sys.stdin.readline

# n, l = map(int, input().split())
# n_list = list(map(int, input().split()))

# d = [n_list[0]]
# for i in range(1, n):
#     new_min = min(n_list[max(0, i-l+1):i])
#     if n_list[i] < new_min:
#         n_min = n_list[i]
#     else:
#         n_min = new_min
#     d.append(n_min)

# print(*d)

from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
n_list = list(map(int, input().split()))

d = []
q = deque()

for i in range(n):
    while q and q[0] < i - l + 1:
        q.popleft()
    
    while q and n_list[q[-1]] > n_list[i]:
        q.pop()

    q.append(i)
    d.append(n_list[q[0]])

print(*d)