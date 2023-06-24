package stage1;

import java.util.*;

public class 제일작은수제거하기 {
	public int[] solution(int[] arr) {
		if (arr.length == 1) {
			int[] answer = {-1};
			return answer;
		}

		int min = 0;
		int[] answer2 = new int[arr.length - 1];

		// 가장 작은 수 구하기
		int[] temp = Arrays.copyOf(arr, arr.length);
		Arrays.sort(temp);
		min = temp[0];

		// 가장 작은 수를 제거한 배열
		int index = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] != min)
				answer2[index++] = arr[i];
		}
		return answer2;
	}
}
