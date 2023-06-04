"""
[문제]
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
수의 위치가 다르면 값이 같아도 다른 수이다.
--
[입력]
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)
--
[출력]
좋은 수의 개수를 첫 번째 줄에 출력한다.
"""
import sys
input = sys.stdin.readline
n = int(input())
num_list = sorted(list(map(int, input().split())))

good_num_count = 0
for target_idx in range(n):
    target = num_list[target_idx]
    idx1 = 0
    idx2 = n - 1
    while idx1 < idx2:
        num_sum = num_list[idx1] + num_list[idx2]
        if num_sum < target:
            idx1 += 1
        elif num_sum > target:
            idx2 -= 1
        else:
            if idx1 != target_idx and idx2 != target_idx:
                good_num_count += 1
                break
            elif idx1 == target_idx:
                idx1 += 1
            elif idx2 == target_idx:
                idx2 -= 1

print(good_num_count)
