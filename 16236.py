"""
[문제]
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 
한 칸에는 물고기가 최대 1마리 존재한다.
아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
3-1. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
3-2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 
물고기를 먹으면, 그 칸은 빈 칸이 된다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 
예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
--
[입력]
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 
공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.
--
[출력]
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
"""
from collections import deque


def find_baby_position(ocean):
    for row_idx, row in enumerate(ocean):
        for col_idx, col in enumerate(row):
            if col == 9: return [row_idx, col_idx]


def find_targets(ocean, baby_position, baby_size):
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    queue = deque()
    queue.append((baby_position[0], baby_position[1]))
    visited[baby_position[1]][baby_position[0]] = 1
    targets = []

    while queue:
        x_now, y_now = queue.popleft()
        for direction in directions:
            x_new, y_new = x_now + direction[0], y_now + direction[1]
            if x_new < 0 or x_new >= n:
                continue
            if y_new < 0 or y_new >= n:
                continue
            if visited[y_new][x_new] != 0:
                continue

            if ocean[y_new][x_new] > baby_size:
                continue

            queue.append((x_new, y_new))
            visited[y_new][x_new] = 1
            distance[y_new][x_new] = distance[y_now][x_now] + 1

            if ocean[y_new][x_new] == baby_size:
                continue
            if ocean[y_new][x_new] == 0:
                continue

            targets.append((x_new, y_new, distance[y_new][x_new]))

    targets.sort(key=lambda x: (-x[2], -x[0], -x[1]))

    return targets


def move_and_eat(ocean, baby_position, baby_size):
    eat_count = 0
    time_spent = 0
    while True:
        targets = find_targets(ocean, baby_position, baby_size)
        if len(targets) == 0:
            break
        x_new, y_new, dist = targets.pop()

        time_spent += dist
        ocean[baby_position[1]][baby_position[0]], ocean[y_new][x_new] = 0, 0

        baby_position = [x_new, y_new]
        eat_count += 1
        if eat_count == baby_size:
            baby_size += 1
            eat_count = 0

    return time_spent


def main(n, ocean):
    baby_position = find_baby_position(ocean)
    baby_size = 2

    time_spent = move_and_eat(ocean, baby_position, baby_size)
    print(time_spent)


if __name__ == "__main__":
    n = int(input())
    ocean = [list(map(int, input().split())) for _ in range(n)]

    main(n, ocean)
