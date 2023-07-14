package stage1;

public class 시저암호 {
	public String solution(String s, int n) {
		char[] ch = s.toCharArray();
		for (int i = 0; i < ch.length; i++) {
			if (ch[i] == 32) // 공백인 경우
				continue;
			else if (65 <= ch[i] && ch[i] <= 90) { // 소문자인 경우
				ch[i] += n;
				if (ch[i] > 90) // 범위를 넘어갈때
					ch[i] -= 26;
			} else { // 대문자인 경우
				ch[i] += n;
				if (ch[i] > 122) // 범위를 넘어갈때
					ch[i] -= 26;
			}
		}
		return String.valueOf(ch);
	}
}
