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
    static int[][] deltaSearch = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
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
        Collections.sort(fishes, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                    if (o1[2] != o2[2])
                return Integer.compare(o1[2], o2[2]);
                    else if (o1[0] != o2[0])
                        return Integer.compare(o1[0], o2[0]);
                    else
                        return Integer.compare(o1[1], o2[1]);
            }

        });
//        for (int[] fish : fishes) {
//            System.out.println(Arrays.toString(fish));
//        }
//        System.out.println("0000000000000000000000000");

        if (fishes.isEmpty()){
            int[] result = {0, 0, 0};
            return result;
        } else {
            return fishes.get(0);
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
//            System.out.println(sx + " " + sy);
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

//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.util.LinkedList;
//import java.util.Queue;
//import java.util.StringTokenizer;
//
//public class Main {
//
//    private static int M, N, date;
//    private static int[][] box;
//    private static Queue<Point> tomato;
//    private static boolean[][] isVisited;
//    private static int[][] delta = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
//
//    static class Point {
//        int x, y;
//
//        public Point(int x, int y) {
//            this.x = x;
//            this.y = y;
//        }
//
//        @Override
//        public String toString() {
//            return "Point [x=" + x + ", y=" + y + "]";
//        }
//
//    }

//    private static void bfs() {
//
//        while (!tomato.isEmpty()) {
//            int size = tomato.size();
//            for (int t = 0; t < size; t++) {
//                Point p = tomato.poll();
//                for (int i = 0; i < 4; i++) {
//                    int nx = p.x + delta[i][0];
//                    int ny = p.y + delta[i][1];
//
//                    if (nx < 0 || ny < 0 || nx >= N || ny >= M)
//                        continue;
//                    if (isVisited[nx][ny])
//                        continue;
//                    if (box[nx][ny] == 1 || box[nx][ny] == -1)
//                        continue;
//
//                    isVisited[nx][ny] = true;
//                    tomato.add(new Point(nx, ny));
//                    box[nx][ny] = 1;
//                }
//
//            }
//            date++;
//        }
//    }

//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        M = Integer.parseInt(st.nextToken());
//        N = Integer.parseInt(st.nextToken());
//        isVisited = new boolean[N][M];
//        box = new int[N][M];
//        tomato = new LinkedList<>();
//        date = 0;
//
//        for (int i = 0; i < N; i++) {
//            st = new StringTokenizer(br.readLine());
//            for (int j = 0; j < M; j++) {
//                box[i][j] = Integer.parseInt(st.nextToken());
//                if (box[i][j] == 1) {
//                    tomato.add(new Point(i, j));
//                    isVisited[i][j] = true;
//                }
//            }
//        }
//
//        bfs();
//
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < M; j++) {
//                if (box[i][j] == 0) {
//                    date = -1;
//                    break;
//                }
//            }
//        }
//
//        if (date == -1) {
//            System.out.println(date);
//        } else {
//            System.out.println(date - 1);
//        }
//    }
//}
