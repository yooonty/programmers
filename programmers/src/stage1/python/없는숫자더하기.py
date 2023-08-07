def solution(numbers):
    # 1~9 숫자 중 없는 숫자로 list
    no = [i for i in range(1, 10) if i not in numbers]
    return sum(no)
