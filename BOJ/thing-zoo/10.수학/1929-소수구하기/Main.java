import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static boolean[] prime = new boolean[1000001];
    public static void main(String[] args) {
        Arrays.fill(prime, true);
        findPrime();

        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        for (int i = m; i <= n; i++) {
            if(!prime[i]) continue;
            System.out.println(i);
        }
        sc.close();
    }

    public static void findPrime() {
        prime[0] = prime[1] = false;
        for (int i = 2; i <= Math.sqrt(prime.length); i++) {
            if (!prime[i]) continue;
            for (int j = i*i; j < prime.length; j += i) {
                prime[j] = false;
            }
        }
    }
}
