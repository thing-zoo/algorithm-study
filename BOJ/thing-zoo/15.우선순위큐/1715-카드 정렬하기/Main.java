import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        while (n-- > 0) {
            heap.add(Integer.parseInt(br.readLine()));
        }
        int result = 0;
        while (heap.size() > 1) {
            int x = heap.poll();
            int y = heap.poll();
            result += x + y;
            heap.add(x + y);
        }
        System.out.println(result);
    }
}
