package stage1;

public class 이상한문자만들기 {
	public String solution(String s) {
		char[] ch = s.toCharArray();
		int idx = 0; //인덱스 판별
		for (int i = 0; i < ch.length; i++) {
			if (ch[i] == ' ') { // 공백일 경우 인덱스 0으로 초기화
				idx = 0;
				continue;
			}
			if (idx % 2 == 0) {
				ch[i] = Character.toUpperCase(ch[i]);
			} else {
				ch[i] = Character.toLowerCase(ch[i]);
			}
			idx++;
		}
		return String.valueOf(ch);
    }
}
