import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        int answer = Integer.MAX_VALUE;
        int end = 0;
        int total = a[0];
        for (int start = 0; start < n; start++) {
            while (end < n && total < s) {
                end += 1;
                if (end != n) total += a[end];
            }
            if (end == n) break;
            answer = Math.min(answer, end - start + 1);
            total -= a[start];
        }
        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
        sc.close();
    }
    
}
