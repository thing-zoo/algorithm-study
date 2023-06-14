import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            PriorityQueue<Long> heap = new PriorityQueue<>();
            while (n-- > 0) {
                heap.add(Long.parseLong(st.nextToken()));
            }
            long result = 0;
            while (heap.size() > 1) {
                long x = heap.poll();
                long y = heap.poll();
                result += x + y;
                heap.add(x + y);
            }
            System.out.println(result);
        }
    }
}
