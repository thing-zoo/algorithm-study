import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        int answer = 0;
        int end = 0;
        int total = a[0];
        for (int start = 0; start < n; start++) {
            while (end < n && total < m) {
                end++;
                if (end != n) total += a[end];
            }
            if (end == n) break;
            if (total == m) answer += 1;
            total -= a[start];
        }
        System.out.println(answer);
        sc.close();
    }
    
}
