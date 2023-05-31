import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static int n, m, k;
    public static char[][] board;
    public static int[][] dir = {{1,0}, {0,1}, {-1,0}, {0,-1}, {1,1}, {1,-1}, {-1,-1}, {-1,1}};
    public static Map<String, Integer> map = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dfs(i, j, "" + board[i][j]);
            }
        }
        for (int i = 0; i < k; i++) {
            System.out.println(map.getOrDefault(br.readLine(), 0));
        }
    }

    public static void dfs(int x, int y, String sub) { // dfs로 (x, y)에서부터 모든방향에서의 5칸 내 부분문자열 찾기
        if (sub.length() <= 5) // 5칸 이내면
            map.compute(sub, (k, v) -> (v == null) ? 1 : v + 1); // 부분문자열 카운트
        if (sub.length() == 5) // 5칸이 되면
            return; // 종료
        for (int i = 0; i < 8; i++) { // 8방향
            int nx = (x + dir[i][0] + n)%n; // 환형 이동
            int ny = (y + dir[i][1] + m)%m;
            dfs(nx, ny, sub + board[nx][ny]); // 다음문자열 추가
        }
    }
}
