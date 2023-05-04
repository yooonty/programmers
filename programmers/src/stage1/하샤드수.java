package stage1;

public class 하샤드수 {
	public boolean solution(int x) {
		int sum = 0;
		String[] s = String.valueOf(x).split("");
		for (String str : s) {
			sum += Integer.parseInt(str);
		}
		return x % sum == 0 ? true : false;
	}
}
