import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        // - 뒤의 값들을 최대로 하면 됨 -> 전부 더해주자
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine(), "-"); // -를 기준으로 토큰 분리
        ArrayList<Integer> sum = new ArrayList<>();
        while (st.hasMoreTokens()) {
            String e = st.nextToken();
            StringTokenizer st2 = new StringTokenizer(e, "+"); // +를 기준으로 토큰 분리
            // + 사이값들의 합 구하기
            int total = 0;
            while (st2.hasMoreTokens()) {
                total += Integer.parseInt(st2.nextToken());
            }
            sum.add(total); // 저장해줌
        }
        // - 사이의 합들 빼주기
        int answer = sum.get(0);
        for (int i = 1; i < sum.size(); i++) {
            answer -= sum.get(i);
        }
        System.out.println(answer);
        sc.close();
    }
}