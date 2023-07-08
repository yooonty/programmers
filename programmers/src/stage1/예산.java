package stage1;

import java.util.Arrays;

public class 예산 {
	public int solution(int[] d, int budget) {
		Arrays.sort(d); // 오름차순 정렬
		int answer = 0;
		for (int i = 0; i < d.length; i++) {
			if (budget >= d[i]) {
				answer++;
				budget -= d[i];
			} else
				break;
		}
		return answer;
	}
}
