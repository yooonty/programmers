package stage1;

public class X만큼간격이있는N개의숫자 {
	public long[] solution(int x, int n) {
		long[] answer = new long[n];
		long add = x; // 조심!
		for (int i = 0; i < n; i++) {
			answer[i] = add;
			add += x;
		}
		return answer;
	}
}
