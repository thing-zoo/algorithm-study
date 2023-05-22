import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);

        int answer = (int) 2e9;
        int end = 0;
        for(int start = 0; start < n; start++) {
            while(end < n && a[end] - a[start] < m) end++;
            if(end == n) break;
            answer = Math.min(answer, a[end] - a[start]);
        }
        System.out.println(answer);
        sc.close();
    }

}
