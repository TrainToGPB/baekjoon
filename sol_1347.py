"""
[문제]
홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다. 
미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나, 벽을 포함하고 있다. 
모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 
홍준이는 미로에서 모든 행과 열의 이동할 수 있는 칸을 걸어다녔다. 
그러면서 자신의 움직임을 모두 노트에 쓰기로 했다. 
홍준이는 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.
입력으로 홍준이가 적은 내용을 나타내는 문자열이 주어진다. 
각 문자 하나는 한 번의 움직임을 말한다. 
‘F’는 앞으로 한 칸 움직인 것이고, ‘L'과 ’R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다. 
즉, 90도를 회전하면서, 위치는 그대로인 것이다.
--
[입력]
첫째 줄에 홍준이가 적은 내용의 길이가 주어진다. 
길이는 0보다 크고, 50보다 작다. 
둘째 줄에 홍준이가 적은 내용이 내용이 주어진다.
--
[출력]
첫째 줄에 미로 지도를 출력한다. 
‘.’은 이동할 수 있는 칸이고, ‘#’는 벽이다.
"""
from collections import deque

note_len = int(input())
notes = input()

coor = [0, 0]
directions = deque([[1, 0], [0, -1], [-1, 0], [0, 1]])
footprints = [coor[:]]
for note in notes:
    direction = directions[0]
    if note == 'F':
        coor[0] += direction[0]
        coor[1] += direction[1]
        footprints.append(coor[:])
    elif note == 'R':
        directions.rotate(-1)
    elif note == 'L':
        directions.rotate(1)

min_foot_x, max_foot_x = min([x[0] for x in footprints]), max([x[0] for x in footprints])
min_foot_y, max_foot_y = min([x[1] for x in footprints]), max([x[1] for x in footprints])

for col in range(min_foot_x, max_foot_x + 1):
    for row in range(min_foot_y, max_foot_y + 1):
        if [col, row] in footprints:
            print('.', end='')
        else:
            print('#', end='')
    print()