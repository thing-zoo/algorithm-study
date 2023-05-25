import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> minheap = new PriorityQueue<>();
        while (n-- > 0) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (minheap.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(minheap.poll());
                }
            } else {
                minheap.add(x);
            }
        }
    }
}
