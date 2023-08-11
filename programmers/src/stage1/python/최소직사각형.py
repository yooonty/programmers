def solution(sizes):
    # size 정렬
    for s in sizes:
        s.sort()

    # 가장 큰 가로 * 가장 큰 세로
    return max([x[0] for x in sizes]) * max(x[1] for x in sizes)
