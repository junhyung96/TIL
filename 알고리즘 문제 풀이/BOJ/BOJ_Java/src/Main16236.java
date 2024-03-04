import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main16236 {
    // 아기 상어위치에서 bfs로 제일 가까운 먹이를 찾아 이동
    // 자신의 크기와 같은 수의 물고기를 먹으면 레벨업
    static int N;
    static int babyShark = 2;
    static int exp = 0;
    static int sx, sy;
    static int time = 0;
    static int[][] map;
    static int[][] deltaSearch = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    static int[] bfs(int x, int y) {
        Queue<LinkedList<Integer>> queue = new LinkedList<>();
        LinkedList<Integer> list = new LinkedList<>();
        list.add(x);
        list.add(y);
        list.add(0);
        queue.offer(list);
        boolean[][] visited = new boolean[N][N];
        visited[x][y] = true;
        ArrayList<int[]> fishes = new ArrayList<>();
        while(!queue.isEmpty()){
            LinkedList<Integer> list1 = queue.poll();
//            System.out.println(list1);
            int cx = list1.poll();
            int cy = list1.poll();
            int dist = list1.poll();

            for (int[] delta : deltaSearch) {
                int nx = cx + delta[0];
                int ny = cy + delta[1];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                if (visited[nx][ny]) continue;
                if (map[nx][ny] > babyShark) continue;

                visited[nx][ny] = true;
                LinkedList<Integer> list2 = new LinkedList<>();
                list2.add(nx);
                list2.add(ny);
                list2.add(dist + 1);
                queue.offer(list2);

                if (map[nx][ny] == 0) continue;
                if (map[nx][ny] == babyShark) continue;

                int[] result = {nx, ny, dist+1};
                fishes.add(result);
//                return result;
            }
        }

        if (fishes.isEmpty()){
            int[] result = {0, 0, 0};
            return result;
        } else {

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        for (int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++){
                int temp = Integer.parseInt(st.nextToken());

                if (temp == 9){
                    sx = i;
                    sy = j;
                    map[i][j] = 0;
                }else {
                    map[i][j] = temp;
                }

            }
        }
        while(true) {
            int[] res = bfs(sx, sy);
//            System.out.println(Arrays.toString(res) + "결과");
            sx = res[0];
            sy = res[1];
            if (res[2] == 0) break;
            exp += 1;
            if (exp == babyShark){
                babyShark += 1;
                exp = 0;
            }
            map[res[0]][res[1]] = 0;
            time += res[2];
        }

        System.out.println(time);
    }
}
