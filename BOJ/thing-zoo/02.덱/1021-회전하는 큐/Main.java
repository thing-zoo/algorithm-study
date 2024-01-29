import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Deque<Integer> deque = new ArrayDeque<>(n);
        for (int i = 1; i <= n; i++) { // 순서대로
            deque.add(i); // 큐에 삽입
        }
        int answer = 0;
        for (int i = 0; i < m; i++) {
            int data = sc.nextInt();
            // 앞뒤로 어디에 위치하는지 구하기
            int front = 0, back = 0;
            for (Integer e : deque) {
                if (e == data) break;
                front++;
            }
            back = deque.size() - front;
            if (front < back) { // 앞에서 가까우면
                for (int j = 0; j < front; j++) {
                    deque.addLast(deque.removeFirst()); // 2번연산: 왼쪽 이동
                }
                answer += front;
            } else { // 뒤에서 가까우면
                for (int j = 0; j < back; j++) {
                    deque.addFirst(deque.removeLast()); // 3번 연산: 오른쪽 이동
                }
                answer += back;
            }
            deque.removeFirst();
        }
        System.out.println(answer);
        sc.close();
    }
}
