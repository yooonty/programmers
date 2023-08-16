def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # or 연산 후 이진수
        tmp = format(i | j, "b")
        # n개 숫자로 채우기
        tmp = tmp.zfill(n)
        # 1/0 -> #/공백
        tmp = tmp.replace("1", "#")
        tmp = tmp.replace("0", " ")

        answer.append(tmp)
    return answer
