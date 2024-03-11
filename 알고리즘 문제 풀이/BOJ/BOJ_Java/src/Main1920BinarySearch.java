import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 특정 값 조회
// 이진 탐색
public class Main1920BinarySearch {
    static int[] nums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for (int i=0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++){
            if (binarySearch(Integer.parseInt(st.nextToken()))) sb.append("1\n");
            else sb.append("0\n");
        }
        System.out.println(sb);
    }

    static boolean binarySearch(int x) {
        int start = 0;
        int end = nums.length - 1;
        int mid = (start + end) / 2;

        while (start <= end) {
            if (x < nums[mid]) end = mid-1;
            else if (x > nums[mid]) start = mid+1;
            else return true; // x 를 찾으면 true 반환
            mid = (start + end) / 2;
        }
        // 못 찾으면 false 반환
        return false;
    }
}
