def solution(n, m):
    answer = []
    a = max(n, m)
    b = min(n, m)
    r = 0

    # 유클리드 호제법 이용
    # 최대공약수
    # math.gcd()도 가능!
    while b != 0:
        r = a % b
        a = b
        b = r

    answer.append(a)

    # 최소공배수 = 두 수의 곱 / 최대공약수
    answer.append(n * m / a)

    return answer
