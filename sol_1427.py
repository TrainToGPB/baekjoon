"""
[문제]
배열을 정렬하는 것은 쉽다. 
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
--
[입력]
첫째 줄에 정렬하려고 하는 수 N이 주어진다. 
N은 1,000,000,000보다 작거나 같은 자연수이다.
--
[출력]
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""
n_list = list(map(int, list(input())))

sorted_idx = 0
n_list_copy = n_list[:]
n_list_sorted = []
while sorted_idx < len(n_list):
    max_n = 0
    max_idx = 0
    for idx, nls in enumerate(n_list_copy):
        if nls > max_n:
            max_n = nls
            max_idx = idx
    
    n_list_sorted.append(n_list_copy[max_idx])
    n_list_copy = n_list_copy[:max_idx] + n_list_copy[max_idx + 1:]
    sorted_idx += 1

print(''.join(map(str, n_list_sorted)))
