import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            Stack<Character> stack = new Stack<>();
            String str = sc.next();
            String answer = "YES";
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '(') {
                    stack.push('(');
                } else {
                    if (stack.isEmpty()) {
                        answer = "NO";
                        break;
                    } else {
                        if (stack.pop() == '(') {
                            continue;
                        } else {
                            answer = "NO";
                            break;
                        }
                    }
                }
            }
            if (!stack.isEmpty()) {
                answer = "NO";
            }
            System.out.println(answer);
        }
        sc.close();
    }
}
