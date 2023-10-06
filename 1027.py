"""
[문제]
세준시에는 고층 빌딩이 많다. 
세준시의 서민 김지민은 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다. 
빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. 
i번째 빌딩 (1부터 시작)은 (x,0)부터 (x,높이)의 선분으로 나타낼 수 있다. 
고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 
두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 
가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.
--
[입력]
첫째 줄에 빌딩의 수 N이 주어진다. 
N은 50보다 작거나 같은 자연수이다. 
둘째 줄에 1번 빌딩부터 그 높이가 주어진다. 
높이는 1,000,000,000보다 작거나 같은 자연수이다.
--
[출력]
첫째 줄에 문제의 정답을 출력한다.
"""
n = int(input())
buildings = list(map(int, input().split()))


def get_gradient(x, nx, buildings):
    return abs((buildings[x] - buildings[nx]) / (x - nx))


def check_can_see(x, direction):
    range_direction = range(x - 1, -1, -1) if direction == 'left' else range(x + 1, n)
    gradients = []
    for nx in range_direction:
        new_gradient = get_gradient(x, nx, buildings)
        if len(gradients) == 0:
            gradients.append(new_gradient)
        else:
            if new_gradient < gradients[-1]:
                gradients.append(new_gradient)
            elif new_gradient == gradients[-1]:
                gradients = [new_gradient]
            else:
                if len(gradients) > 1:
                    break
                else:
                    gradients = [new_gradient]
                    break
            
    return gradients


max_can_see = 0
for x in range(n):
    can_see = 0
    left_gradients = check_can_see(x, 'left')
    right_gradients = check_can_see(x, 'right')

    can_see += len(left_gradients)
    can_see += len(right_gradients)
    if can_see > max_can_see:
        max_can_see = can_see

print(max_can_see)
