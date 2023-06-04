import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        int count = 0;
        for (int i = 666; i < Integer.MAX_VALUE; i++) {
            if (Integer.toString(i).contains("666")) {
                if (++count == n) {
                    System.out.println(i);
                    break;
                }
            }
        }
    }
}
