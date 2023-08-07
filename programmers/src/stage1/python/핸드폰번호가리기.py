def solution(phone_number):
    # (len(phone_number)-4)*'*' + s[:4] 도 가능
    l = list(phone_number)
    for i in range(len(l)-4):
        l[i] = '*'
    return "".join(l)
