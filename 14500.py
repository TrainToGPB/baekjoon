"""
[문제]
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
--
[입력]
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.
--
[출력]
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
"""
height, width = map(int, input().split())
numbers = []
for _ in range(height):
    nums = list(map(int, input().split()))
    numbers.append(nums)


tetrominos = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [1, 1]]
]


def rotate_coor(rotation, coor):
    if rotation % 4 == 0:
        rotated_coor = coor
    elif rotation % 4 == 1:
        rotated_coor = [-coor[1], coor[0]]
    elif rotation % 4 == 2:
        rotated_coor = [-coor[0], -coor[1]]
    elif rotation % 4 == 3:
        rotated_coor = [coor[1], -coor[0]]
    return rotated_coor


def max_tetromino_sum(numbers):
    max_sum = 0
    for h in range(height):
        for w in range(width):
            start_coor = [w, h]
            for tetromino in tetrominos:
                for rotation in range(4):
                    rotated_tetromino = [[rotate_coor(rotation, coor)[0], rotate_coor(rotation, coor)[1]] for coor in tetromino]
                    temp_sum = 0
                    is_out = False
                    for tetro_coor in rotated_tetromino:
                        new_coor = [start_coor[0]+tetro_coor[0], start_coor[1]+tetro_coor[1]]
                        if new_coor[0] < width and new_coor[1] < height:
                            temp_sum += numbers[new_coor[1]][new_coor[0]]
                        else:
                            break
                    if is_out:
                        continue
                    else:
                        max_sum = temp_sum if temp_sum > max_sum else max_sum
    return max_sum


print(max_tetromino_sum(numbers))
