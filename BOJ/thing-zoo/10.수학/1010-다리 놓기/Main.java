import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            long answer = 1;
            for (int j = n+1; j <= m; j++) {
            	answer *= j;
                answer /= (j-n);
            }
            System.out.println(answer);
        }
        sc.close();
    }
}
