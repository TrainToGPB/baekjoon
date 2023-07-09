"""
[문제]
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 
이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
--
[입력]
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
--
[출력]
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
--
[제한]
1 ≤ N ≤ 1,000,000
-10^9 ≤ Xi ≤ 10^9
"""
n = int(input())
n_list = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

sorted_n_list = quick_sort(n_list)
comp_coor_dict = {}
previous_append = sorted_n_list[0]
coor = 0
comp_coor_dict[previous_append] = coor
for snl in sorted_n_list[1:]:
    if comp_coor_dict:
        if previous_append < snl:
            coor += 1
    previous_append = snl
    comp_coor_dict[snl] = coor

comp_coor = []
for nl in n_list:
    comp_coor.append(comp_coor_dict[nl])

print(*comp_coor)
