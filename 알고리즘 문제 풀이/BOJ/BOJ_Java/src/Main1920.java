import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

// 특정 값 조회
// 해시맵 생각보다 느림
public class Main1920 {
    static boolean[] isNumber;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, Boolean> hashMap = new HashMap<>();

//        isNumber = new boolean[100_100];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++){
            int num = Integer.parseInt(st.nextToken());
            hashMap.put(num, true);
//            isNumber[num] = true;
        }
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++){
            int num = Integer.parseInt(st2.nextToken());
            if (hashMap.containsKey(num)) sb.append("1\n");
//            if (isNumber[num]) System.out.println(1);
            else sb.append("0\n");
        }
        System.out.println(sb);

    }
}
