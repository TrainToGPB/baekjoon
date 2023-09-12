"""
[문제]
나3곱2 게임은 정수 하나를 이용한다. 
가장 먼저, 정수 x로 시작하고, 연산을 N-1번 적용한다. 
적용할 수 있는 연산은 두 가지 있고, 아래와 같다.
나3: x를 3으로 나눈다. x는 3으로 나누어 떨어져야 한다.
곱2: x에 2를 곱한다.
나3곱2 게임을 진행하면서, 만든 수를 모두 기록하면 수열 A를 만들 수 있다. 
예를 들어, x = 9, N = 6이고, 적용한 연산이 곱2, 곱2, 나3, 곱2, 나3인 경우에 A = [9, 18, 36, 12, 24, 8] 이다.
수열 A의 순서를 섞은 수열 B가 주어졌을 때, 수열 A를 구해보자.
--
[입력]
첫째 줄에 수열의 크기 N(2 ≤ N ≤ 100)이 주어진다. 
둘째 줄에는 수열 B가 주어진다. 
B에 포함된 원소는 1018 보다 작거나 같은 자연수이다.
--
[출력]
나3곱2 게임의 결과 수열 A를 출력한다. 
항상 정답이 존재하는 경우에만 입력으로 주어지며, 가능한 정답이 여러가지인 경우에는 아무거나 출력한다.
"""
def reset_answer_series(start_idx, series):
    answer_series = []
    series_copy = series[:]
    element = series_copy.pop(start_idx)
    answer_series.append(element)
    return answer_series, series_copy, element


def move_to_answer_series(answer_series, series_copy, element):
    series_copy.remove(element)
    answer_series.append(element)


def get_answer_series(series):
    start_idx = 0
    answer_series, series_copy, element = reset_answer_series(start_idx, series)

    while len(answer_series) < len(series):
        if element % 3 == 0:
            if element // 3 in series_copy:
                element //= 3
                move_to_answer_series(answer_series, series_copy, element)
            elif element * 2 in series_copy and element // 3 not in series_copy:
                element *= 2
                move_to_answer_series(answer_series, series_copy, element)
            else:
                start_idx += 1
                answer_series, series_copy, element = reset_answer_series(start_idx, series)
        else:
            if element * 2 in series_copy:
                element *= 2
                move_to_answer_series(answer_series, series_copy, element)
            else:
                start_idx += 1
                answer_series, series_copy, element = reset_answer_series(start_idx, series)

    return answer_series


if __name__ == "__main__":
    n = int(input())
    series = list(map(int, input().split()))
    answer_series = get_answer_series(series)
    print(*answer_series)
