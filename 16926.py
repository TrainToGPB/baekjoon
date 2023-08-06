"""
[문제]
크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.
A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.
1 2 3 4       2 3 4 8       3 4 8 6
5 6 7 8       1 7 7 6       2 7 8 2
9 8 7 6   →   5 6 8 2   →   1 7 6 3
5 4 3 2       9 5 4 3       5 9 5 4
 <시작>         <회전1>        <회전2>
배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.
--
[입력]
첫째 줄에 배열의 크기 main_width, M과 수행해야 하는 회전의 수 R이 주어진다.
둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.
--
[출력]
입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def get_inner_matrix(matrix, level):
    inner_matrix = []
    inner_height, inner_width = len(matrix) - (2 * level), len(matrix[0]) - (2 * level)
    for ih in range(inner_height):
        inner_matrix.append(matrix[ih+level][level:inner_width+level])
    return inner_matrix


def flatten(matrix):
    flatten_matrix = []
    height = len(matrix)
    for h in range(height):
        if h == 0:
            flatten_matrix.extend(matrix[0])
        elif h == height - 1:
            flatten_matrix.extend(matrix[-1][::-1])
        else:
            flatten_matrix.append(matrix[h][-1])
    for rh in range(height-2, 0, -1):
        flatten_matrix.append(matrix[rh][0])

    flatten_matrix = deque(flatten_matrix)
    
    return flatten_matrix


def matrixize(flatten_matrix, height):
    matrix = []
    width = (len(flatten_matrix) + 4 - (2 * height)) // 2
    for h in range(height):
        if h == 0:
            matrix.append(list(flatten_matrix)[:width])
            for _ in range(width):
                flatten_matrix.popleft()
        elif h == height - 1:
            matrix.append(list(flatten_matrix)[:width][::-1])
            for _ in range(width):
                flatten_matrix.popleft()
        else:
            matrix.append([0] * (width-1) + [flatten_matrix.popleft()])
    for rh in range(height-2, 0 , -1):
        matrix[rh][0] = flatten_matrix.popleft()
    
    return matrix


def insert_matrix(main_matrix, sub_matrix):
    sub_height, sub_width = len(sub_matrix), len(sub_matrix[0])
    for i in range(sub_height):
        for j in range(sub_width):
            main_matrix[i + 1][j + 1] = sub_matrix[i][j]

    return main_matrix


def transpose(matrix):
    height, width = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            transposed[j][i] = matrix[i][j]
    
    return transposed


def main():
    height, width, rotation = map(int, input().split())
    matrix = []
    for _ in range(height):
        matrix.append(list(map(int, input().split())))

    istransposed = False
    if height < width:
        matrix = transpose(matrix)
        height, width = width, height
        istransposed = True

    rotated_matrix = []
    for level in range(width // 2):
        inner_matrix = get_inner_matrix(matrix, level)
        flatten_inner_matrix = flatten(inner_matrix)
        if istransposed:
            flatten_inner_matrix.rotate(rotation)
        else:
            flatten_inner_matrix.rotate(-rotation)
        inner_height = height - (2 * level)
        rotated_inner_matrix = matrixize(flatten_inner_matrix, inner_height)
        if rotated_matrix:
            rotated_matrix = insert_matrix(rotated_matrix, rotated_inner_matrix)
        else:
            rotated_matrix = rotated_inner_matrix

    if istransposed:
        rotated_matrix = transpose(rotated_matrix)
        height, width = width, height

    for h in range(height):
        print(*rotated_matrix[h])


if __name__ == "__main__":
    main()
