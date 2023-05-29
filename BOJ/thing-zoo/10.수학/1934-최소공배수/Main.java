import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(lcm(a, b));
        }
        sc.close();
    }

    public static int gcd(int a, int b) {
        if (a == 0) return b;
        return gcd(b%a, a);
    }

    public static int lcm(int a, int b) {
        return a*b/gcd(a, b);
    }
}
