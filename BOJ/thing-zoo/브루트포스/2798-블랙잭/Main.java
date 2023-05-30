import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = sc.nextInt();
        }
        sc.close();

        int answer = 0;
        Loop:
        for (int i = 0; i < n-2; i++) {
            for (int j = i + 1; j < n-1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int total = cards[i] + cards[j] + cards[k];
                    if (total <= m) {
                        answer = Math.max(answer, total);
                        if (total == m) {
                            break Loop;
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}