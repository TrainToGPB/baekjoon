"""
[문제]
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 
섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
--
[입력]
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.
--
[출력]
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs_find_islands(island_map, visit, width, height, x, y):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    visit[y][x] = True
    for dx, dy in zip(dx, dy):
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < width and ny >= 0 and ny < height:
            if not visit[ny][nx] and island_map[ny][nx] == 1:
                dfs_find_islands(island_map, visit, width, height, nx, ny)
    
island_maps, visits, widths, heights = [], [], [], []
while True:
    width, height = map(int, input().split())
    widths.append(width)
    heights.append(height)
    if width == 0 and height == 0:
        break

    island_map = []
    for _ in range(height):
        row = list(map(int, input().split()))
        island_map.append(row)
    island_maps.append(island_map)

    visit = [[False] * width for _ in range(height)]
    visits.append(visit)

for island_map, visit, width, height in zip(island_maps, visits, widths, heights):
    x, y = 0, 0
    island_count = 0
    for j in range(width):
        for i in range(height):
            if not visit[i][j] and island_map[i][j] == 1:
                island_count += 1
                dfs_find_islands(island_map, visit, width, height, j, i)

    print(island_count)
    