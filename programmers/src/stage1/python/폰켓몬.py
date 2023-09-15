def solution(nums):
    # combinations 이용 시 시간초과
    # 중복제거 한 nums 의 수
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2
