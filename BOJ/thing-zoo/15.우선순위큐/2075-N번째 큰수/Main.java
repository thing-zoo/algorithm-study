import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i = 0; i < n*n; i++) {
            heap.add(sc.nextInt());
            if (heap.size() > n) {
                heap.poll();
            }
        }
        sc.close();
        System.out.println(heap.peek());
    }
}
