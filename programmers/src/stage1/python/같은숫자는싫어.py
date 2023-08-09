def solution(arr):
    answer = []
    # top 인덱스
    top = -1
    for i in arr:
        # answer가 빈 배열일 때
        if len(answer) == 0:
            answer.append(i)
            top += 1
        # answer가 빈 배열이 아닐 때
        else:
            # answer의 top이랑 다를 때
            if answer[top] != i:
                answer.append(i)
                top += 1
            # answer의 top이랑 같을 때
            else:
                continue
    return answer
