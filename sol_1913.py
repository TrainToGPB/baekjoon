"""
[문제]
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

9	2	3
8	1	4
7	6	5

25	10	11	12	13
24	9	2	3	14
23	8	1	4	15
22	7	6	5	16
21	20	19	18	17

N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 
또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 
예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.
--
[입력]
첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 
둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.
--
[출력]
N개의 줄에 걸쳐 표를 출력한다. 
각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. 
N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.
"""
n = int(input())
target = int(input())


def move_and_write(number: int, board: list, coor_now: list, direction: list):
    coor_new = [coor_now[0] + direction[0], coor_now[1] + direction[1]]
    board[coor_new[1]][coor_new[0]] = number
    return coor_new, board


def make_snail_board(n, target):
    board = [[0] * n for _ in range(n)]
    coor_original = [n//2, n//2]
    coor = coor_original[:]
    number = 1
    board[coor[1]][coor[0]] = number
    
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 상, 우, 하, 좌
    snail_idx = 1
    if n == 1:
        return board, [1, 1]
    
    while True:
        for direction in directions:
            for _ in range((snail_idx + 1)//2):
                number += 1
                coor, board = move_and_write(number, board, coor, direction)
                if target == 1:
                    coor_target = coor_original[:]
                elif number == target:
                    coor_target = coor
                if number == n**2:
                    return board, [ct + 1 for ct in coor_target[::-1]]
            snail_idx += 1


board, coor_target = make_snail_board(n, target)

for board_row in board:
    print(*board_row)
    
print(*coor_target)
