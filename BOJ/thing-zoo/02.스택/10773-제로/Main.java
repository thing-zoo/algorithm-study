import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        Stack<Integer> stack = new Stack<>();
        int total = 0;
        for (int i = 0; i < k; i++) {
            int x = sc.nextInt();
            total += x;
            if (x == 0) total -= stack.pop();
            else stack.push(x);
        }
        System.out.println(total);
        sc.close();
    }
}
