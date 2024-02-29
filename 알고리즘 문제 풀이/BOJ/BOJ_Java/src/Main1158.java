import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main1158 {
    // 요세푸스 문제
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        Queue<Integer> queue = new LinkedList<>();

        for (int i=1; i<N+1; i++){
            queue.offer(i);
        }
//        System.out.print("<");
        sb.append("<");
        while (true) {
            if (queue.size() == 1) {
//                System.out.print(queue.poll());
                sb.append(queue.poll());
                break;
            }
            for (int i=0; i<K-1; i++) {
                queue.offer(queue.poll());
            }
//            System.out.print(queue.poll() + ", ");
            sb.append(queue.poll()).append(", ");
        }
//        System.out.print(">");
        sb.append(">");
        System.out.println(sb);
    }
}

