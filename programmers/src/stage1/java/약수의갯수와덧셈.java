package stage1;

public class 약수의갯수와덧셈 {
	public int solution(int left, int right) {
		int answer = 0;
		for (int i = left; i <= right; i++) {
			// 약수의 개수 담을 변수
			int cnt = 0;
			// 약수 구하기
			for (int j = 1; j * j <= i; j++) {
				if (j * j == i)
					cnt++;
				else if (i % j == 0)
					cnt += 2;
			}
			// 약수 개수가 짝수? 홀수?
			if (cnt % 2 == 0)
				answer += i;
			else
				answer -= i;
		}
		return answer;
	}
}
