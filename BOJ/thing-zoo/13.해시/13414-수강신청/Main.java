import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        Map<String, Integer> waiting_list = new HashMap<>();
        for (int i = 0; i < l; i++) {
            String number = br.readLine();
            if (waiting_list.containsKey(number)) { // 이미 신청한 사람이라면
                waiting_list.replace(number, i); // 대기순서를 뒤로 업데이트
            } else {
                waiting_list.put(number, i); // <학번, 대기순서> 추가
            }
        }

        List<Entry<String, Integer>> arr = new ArrayList<>(waiting_list.entrySet());
        arr.sort((e1, e2) -> e1.getValue().compareTo(e2.getValue())); // 값 기준 오름차순 정렬
        for (int i = 0; i < Math.min(k, arr.size()); i++) { // 신청 정원과 신청 인원중 최소값만큼 신청됨
            Entry<String, Integer> entry = arr.get(i);
            System.out.println(entry.getKey());
        }
    }
}
