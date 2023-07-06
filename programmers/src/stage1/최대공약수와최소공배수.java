package stage1;

public class 최대공약수와최소공배수 {
	public int[] solution(int n, int m) {
		// 유클리드 호제법 이용!
		int[] answer = { 0, 0 };
		int a = Math.max(n, m);
		int b = Math.min(n, m);
		int r = 0;

		// 최대공약수
		while (b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		answer[0] = a;

		// 최소공배수
		answer[1] = n * m / a;
		return answer;
	}
}
