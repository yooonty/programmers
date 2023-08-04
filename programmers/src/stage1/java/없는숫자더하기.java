package stage1;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class 없는숫자더하기 {
	public int solution(int[] numbers) {
		int answer = 0;
		// int -> List
		List<Integer> intList = Arrays.stream(numbers).boxed().collect(Collectors.toList());
		for (int i = 0; i < 10; i++) {
			if (!intList.contains(i))
				answer += i;
		}
		return answer;
	}
}
