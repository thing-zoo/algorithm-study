import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        System.out.print("<");
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++)
            q.add(i);
        while (!q.isEmpty()) {
            for (int i = 1; i < k; i++)
                q.add(q.remove());
            if (q.size() == 1) System.out.printf("%d>", q.remove());
            else System.out.printf("%d, ", q.remove());
        }
        sc.close();
    }
}
