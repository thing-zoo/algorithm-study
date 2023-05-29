import java.util.*;

public class Main {
    public static void main(String[] args) { // 슬라이딩 윈도우 사용
        Scanner sc = new Scanner(System.in);
        int n, d, k, c;
        n = sc.nextInt();
        d = sc.nextInt();
        k = sc.nextInt();
        c = sc.nextInt();

        int[] sushi = new int[n];
        for (int i = 0; i < n; i++)
            sushi[i] = sc.nextInt();
        sc.close();
        
        Map<Integer, Integer> count = new HashMap<>(); // 스시 종류 카운트
        count.put(c, 1); // 미리 쿠폰 적용
        for (int i = 0; i < k; i++) { // 초기 윈도우 카운트
            count.compute(sushi[i], (key, value) -> (value == null) ? 1 : value + 1);
        }

        int answer = 0;
        int end = k - 1;
        for (int start = 0; start < n; start++) {
            answer = Math.max(answer, count.size()); // 정답 갱신
            // 윈도우 슬라이드해주기
            count.put(sushi[start], count.get(sushi[start]) - 1); // start 카운트 감소
            if (count.get(sushi[start]) == 0) // start 카운트가 0이면
                count.remove(sushi[start]); // 삭제
            end = (end + 1)%n; // end 한칸 이동
            count.compute(sushi[end], (key, value) -> (value == null) ? 1 : value + 1); // 새 end 카운트
        }
        System.out.println(answer);
    }
}