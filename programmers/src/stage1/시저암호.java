package stage1;

public class 시저암호 {
	public String solution(String s, int n) {
		String answer = "";
		char[] ch = s.toCharArray();
		for (char c : ch) {
			if (c != 32) {
				if (c == 90 || c == 122)
					c -= 26;
				c += n;
				answer += c;
			} else
				answer += " ";
		}
		return answer;
	}
}
