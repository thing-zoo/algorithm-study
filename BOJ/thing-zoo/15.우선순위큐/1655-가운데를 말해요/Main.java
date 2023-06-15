import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> leftHeap = new PriorityQueue<>(Collections.reverseOrder());   // 최대힙, 중앙값미만
        PriorityQueue<Integer> rightHeap = new PriorityQueue<>();  // 최소힙, 중앙값이상, 루트 = 중앙값
        int n = Integer.parseInt(br.readLine());
        for (int i = 1; i <= n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (i == 1 || rightHeap.peek() < x) {
                rightHeap.add(x);
            } else {
                leftHeap.add(x);
            }

            int leftSize;
            if (i%2 != 0) leftSize = i/2;
            else leftSize = i/2-1;
            
            if (leftSize < leftHeap.size()) {
                rightHeap.add(leftHeap.poll());
            } else if (leftSize > leftHeap.size()) {
                leftHeap.add(rightHeap.poll());
            }
            sb.append(rightHeap.peek()+"\n");
        }    
        System.out.println(sb);
    }
}
