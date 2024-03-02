import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main1021 {
    // 양방향 순환 큐
    public static void main(String[] args) throws IOException {
        int cnt = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 배열 초기화
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i=1; i<N+1; i++){
            deque.addLast(i);
        }

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++){
            // 움직인 횟수 tempcnt
            int tempcnt = 0;
            int target = Integer.parseInt(st2.nextToken());
            while(true) {
                int cur = deque.pollFirst();
                if (target != cur) {
                    deque.addLast(cur);
                    tempcnt += 1;
                } else {
                    cnt += Math.min(tempcnt, N-tempcnt);
                    N -= 1;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}
