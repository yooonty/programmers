import itertools


def solution(number):
    answer = 0
    # 조합을 이용하여 3개씩 => itertools.combination이용
    three = list(itertools.combinations(number, 3))
    for i in three:
        if sum(i) == 0:
            answer += 1
    return answer
