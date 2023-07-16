"""
[문제]
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 
이 회사는 N개의 컴퓨터로 이루어져 있다. 
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, 
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 
한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
--
[입력]
첫째 줄에, N과 M이 들어온다. 
N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.
--
[출력]
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
"""
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

num_computer, num_relation = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(num_relation)]

relation_dict = defaultdict(list)
for relation in relations:
    relation_dict[relation[1]].append(relation[0])


def hack_dfs(relation_dict, start_computer, visited, is_middle):
    visited.add(start_computer)
    for trust_computer in relation_dict[start_computer]:
        if trust_computer not in visited:
            hack_dfs(relation_dict, trust_computer, visited, is_middle)
    return visited


num_max_hacked = 0
max_hacks = []
is_middle = set()
for computer in range(1, num_computer+1):
    if computer in is_middle:
        continue
    visited = set()
    hacked_visited = hack_dfs(relation_dict, computer, visited, is_middle)

    num_hacked = len(hacked_visited)
    if num_hacked > num_max_hacked:
        num_max_hacked = num_hacked
        max_hacks = [computer]
    elif num_hacked == num_max_hacked:
        max_hacks.append(computer)

    is_middle = is_middle.union(hacked_visited)

print(*sorted(max_hacks))
