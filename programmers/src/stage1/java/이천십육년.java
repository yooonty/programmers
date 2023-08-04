package stage1;

public class 이천십육년 {
	public String solution(int a, int b) {
		String[] day = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };
		int[] month = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

		int date = 0;
		for (int i = 0; i < a - 1; i++) {
			date += month[i];
		}

		date += b - 1;

		return day[date % 7];
	}

}
