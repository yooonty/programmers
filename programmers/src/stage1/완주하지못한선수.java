package stage1;

import java.util.*;

public class 완주하지못한선수 {
	public String solution(String[] participant, String[] completion) {
		HashMap<String, Integer> map = new HashMap<>();
		for (String x : participant) {
			map.put(x, map.getOrDefault(x, 0) + 1);
		}
		for (String x : completion) {
			map.put(x, map.get(x) - 1);
		}
		String answer = "";
		for (String x : map.keySet()) {
			if (map.get(x) != 0) {
				answer = x;
				break;
			}
		}
		return answer;
	}
}
