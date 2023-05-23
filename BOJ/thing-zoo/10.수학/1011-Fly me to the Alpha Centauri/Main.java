import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int dist = - Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
            int n = (int)Math.sqrt(dist);
            if (n*n == dist) {
                System.out.println(2*n-1);
            } else if(n*n+n < dist) {
                System.out.println(2*(n+1)-1);
            } else {
                System.out.println(2*n);
            }
        }
    }
}
