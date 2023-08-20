import itertools


def solution(numbers):
    # 두 개의 수를 뽑아 더해서 만든 리스트
    answer = list(map(lambda x: sum(x), itertools.combinations(numbers, 2)))
    # 중복 제거
    answer = list(set(answer))
    # 오름차순 정렬
    answer.sort()
    return answer
