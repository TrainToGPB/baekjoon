"""
[문제]
다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다.
다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.
현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
다솜이는 기호 1번이다. 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.
예를 들어서, 마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 다솜이는 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면, 국회의원에 당선이 된다.
돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.
다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.
--
[입력]
첫째 줄에 후보의 수 N이 주어진다. 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다. N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.
--
[출력]
첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.
"""
from collections import deque

N = int(input())
N_list = deque()
for _ in range(N):
    N_list.append(int(input()))

idiots_num = sum(N_list)
dasom = N_list.popleft()
good_idiots_num = 0
if N_list:
    others = N_list
    while dasom <= max(others):
        others[others.index(max(others))] -= 1
        dasom += 1
        good_idiots_num += 1

print(good_idiots_num)