"""
[문제]
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
--
[입력]
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
--
[출력]
첫째 줄에 경우의 수를 출력한다.
"""
width = int(input())
if width < 2:
    print(0)
else:
    dp = [0 for _ in range(width + 1)]
    dp[2] = 3

    for i in range(3, len(dp)):
        if i % 2 == 0:
            dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

    print(dp[-1])
