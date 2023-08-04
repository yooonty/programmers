package stage1;

import java.util.*;

public class 나누어떨어지는숫자배열 {
	public int[] solution(int[] arr, int divisor) {
		int[] answer = Arrays.stream(arr).filter(x -> x % divisor == 0).toArray();
		if (answer.length == 0) {
			answer = new int[1];
			answer[0] = -1;
		}
		Arrays.sort(answer);
		return answer;
	}
}
