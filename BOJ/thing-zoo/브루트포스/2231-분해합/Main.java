import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int total = i, m = i;
            while (m > 0) {
                total += m%10;
                m /= 10;
            }
            if (total == n) {
                answer = Math.min(answer, i);
            }
        }

        if (answer == Integer.MAX_VALUE) {
            answer = 0;
        }
        System.out.println(answer);
    }
}