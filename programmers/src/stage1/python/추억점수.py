def solution(name, yearning, photo):
    dic = {}
    answer = []

    for i in range(len(name)):
        dic[name[i]]=yearning[i]

    for i in photo:
        score = 0
        for j in i:
            if j in dic:
                score+=dic.get(j)
        answer.append(score)

    return answer
