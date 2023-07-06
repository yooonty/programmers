package stage1;

public class 문자열다루기기본 {
	public boolean solution(String s) {
		//숫자가 아닌것 제거
		String number = s.replaceAll("[^0-9]", "");
		return (s.length() == 4 || s.length() == 6) && s == number ? true : false;
	}
}
