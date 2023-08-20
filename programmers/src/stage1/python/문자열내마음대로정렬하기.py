def solution(strings, n):
    # 인덱스 n의 문자가 같은 경우를 대비하여
    # 오름차순 정렬 1번 실행
    strings.sort()
    # sort()의 key 매개변수를 이용
    # 정렬을 목적으로 하는 함수
    strings.sort(key=lambda x: x[n])
    return strings
