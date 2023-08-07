def solution(arr):
    # arr에서 가장 작은 수를 제거
    arr.pop(arr.index(min(arr)))
    # 빈 배열이면 [-1]을, 빈 배열이 아니면 arr을 리턴
    return [-1] if len(arr) == 0 else arr
