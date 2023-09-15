"""
[문제]
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 
말이 지나는 칸은 좌측 상단의 칸도 포함된다.
--
[입력]
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 
둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.
--
[출력]
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
"""
import sys
input = sys.stdin.readline

height, width = map(int, input().split())
board = [input() for _ in range(height)]


def letter_to_num(letter):
    return ord(letter) - 65


def dfs(x, y, board, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_path = sum(visited)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue
        new_letter = board[ny][nx]
        if visited[letter_to_num(new_letter)] == 1:
            continue
        visited[letter_to_num(new_letter)] = 1
        max_path = max(max_path, dfs(nx, ny, board, visited))
        visited[letter_to_num(new_letter)] = 0

    return max_path


visited = [0 for _ in range(26)]
visited[letter_to_num(board[0][0])] = 1
x, y = 0, 0

max_path = dfs(x, y, board, visited)
print(max_path)