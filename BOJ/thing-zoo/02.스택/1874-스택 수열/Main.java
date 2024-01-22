import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int n = sc.nextInt();
        int now = 1;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int data = sc.nextInt();
            while (now <= data) { // 입력받은 수까지
                stack.push(now++); // 오름차순 삽입, 현재 수 증가
                sb.append("+\n");
            }
            if (stack.pop() == data) { // top이 입력받은수면
                sb.append("-\n"); // 출력
            } else { // 불가능한 경우
                System.out.println("NO");
                sb.setLength(0); // 문자열 비우고
                break; // 종료
            }
        }
        System.out.print(sb);
        sc.close();
    }
}
