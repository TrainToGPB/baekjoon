"""
[문제]
로마 시대 때는 현재 사용하는 아라비아 숫자가 아닌 다른 방법으로 수를 표현하였다.
로마 숫자는 다음과 같은 7개의 기호로 이루어진다.

기호 I V X L C D M
값 1 5 10 50 100 500 1000
수를 만드는 규칙은 다음과 같다.

보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다. 
그리고 그 값은 모든 숫자의 값을 더한 값이 된다. 
예를 들어 LX = 50 + 10 = 60 이 되고, MLI = 1000 + 50 + 1 = 1051 이 된다.
V, L, D는 한 번만 사용할 수 있고 I, X, C, M은 연속해서 세 번까지만 사용할 수 있다. 
예를 들어 VV나 LXIIII 와 같은 수는 없다. 
그리고 같은 숫자가 반복되면 그 값은 모든 숫자의 값을 더한 값이 된다.
예를 들어 XXX = 10 + 10 + 10 = 30 이 되고, CCLIII = 100 + 100 + 50 + 1 + 1 + 1 = 253 이 된다.
작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 다음과 같다. 
IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900 을 나타낸다. 
이들 각각은 한 번씩만 사용할 수 있다. 
그런데 IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다. 
이들 외에는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 없다. 
예를 들어 XCXC 나 CMCD, VX 나 IIX 와 같은 수는 없다. 
참고로 LIX = 50 + 9 = 59, CXC = 100 + 90 = 190 이 된다.
모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현해야 한다. 
예를 들어 60 은 LX 이지 XLXX 가 아니고, 5 는 V 이지 IVI 가 아니다.
아래의 예를 참고 하시오.

DLIII = 500 + 50 + 3 = 553
MCMXL = 1000 + 900 + 40 = 1940
235 = CCXXXV
2493 = MMCDXCIII
로마 숫자로 이루어진 두 수를 입력받아 그 둘을 더한 값을 아라비아 숫자와 로마 숫자로 출력하는 프로그램을 작성하시오.
--
[입력]
첫째 줄과 둘째 줄에 하나씩 로마 숫자로 표현된 수가 주어진다. 입력된 각 수는 2000 보다 작거나 같고, 두 수의 합은 4000보다 작다.
--
[출력]
입력으로 주어진 두 수를 더한 값을 첫째 줄에 아라비아숫자로 출력하고 둘째 줄에는 로마 숫자로 출력한다.
"""
from collections import deque


def rome_to_arabian(num_rome):
    num_arab = 0
    while num_rome:
        num_rome_temp = '' + num_rome.popleft()
        if num_rome_temp == 'I':
            if num_rome and num_rome[0] in 'VX':
                num_rome_temp += num_rome.popleft()
        elif num_rome_temp == 'X':
            if num_rome and num_rome[0] in 'LC':
                num_rome_temp += num_rome.popleft()
        elif num_rome_temp == 'C':
            if num_rome and num_rome[0] in 'DM':
                num_rome_temp += num_rome.popleft()

        num_arab += rom2ara[num_rome_temp]
    
    return num_arab


def arabian_to_rome(num_arab):
    num_rome = ''
    for ara in aras[::-1]:
        while num_arab >= ara:
            num_arab -= ara
            num_rome += ara2rom[ara]
    return num_rome


if __name__ == "__main__":
    num_rome1 = deque(input())
    num_rome2 = deque(input())

    roms = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    aras = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom2ara = {rom: ara for rom, ara in zip(roms, aras)}
    ara2rom = {ara: rom for rom, ara in zip(roms, aras)}

    sum_arab = rome_to_arabian(num_rome1) + rome_to_arabian(num_rome2)
    sum_rome = arabian_to_rome(sum_arab)

    print(sum_arab)
    print(sum_rome)
