import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextInt();
        }
        sc.close();
        
        Arrays.sort(p);
        for (int i = 1; i < n; i++) {
            p[i] += p[i-1];
        }

        int total = 0;
        for (int i : p) {
            total += i;    
        }
        System.out.println(total);
    }
}
