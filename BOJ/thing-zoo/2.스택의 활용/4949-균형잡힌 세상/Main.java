import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String data;
        while(true) {
            data = sc.nextLine();
            if (data.equals(".")) break;
            String answer = "yes";
            Stack<Character> stack = new Stack<>();
            for (int i = 0; i < data.length(); i++) {
                if (data.charAt(i) == '(' || data.charAt(i) == '[') {
                    stack.push(data.charAt(i));
                } else if (data.charAt(i) == ')') {
                    if (stack.isEmpty() || (!stack.isEmpty() && stack.pop() != '(')) {
                        answer = "no";
                        break;
                    }
                } else if (data.charAt(i) == ']') {
                    if (stack.isEmpty() || (!stack.isEmpty() && stack.pop() != '[')) {
                        answer = "no";
                        break;
                    }
                }
            }
            if (!stack.isEmpty()) {
                answer = "no";
            }
            System.out.println(answer);
        }
        sc.close();
    }
}
