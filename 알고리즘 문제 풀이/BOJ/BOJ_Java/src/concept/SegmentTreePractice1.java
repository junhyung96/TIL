package concept;

public class SegmentTreePractice1 {

    // 아래 코드는 구간 합 쿼리가 있을 때 마다 모든 값을 더함
    // point update = O(1)
    // range query = O(N)
    // dp 를 이용해서 O(N^2) 개의 구간 합을 미리 구해 놓는다면 쿼리를 O(1) 에 구할 수 있지만
    // 수열의 값 하나가 바뀐다면 모든 구간합도 바뀌어야 하므로 테이블 갱신이 O(N^2)만큼 소모된다

    // --> 세그먼트 트리를 이용하면 O(lonN) 개의 합으로 나타낼 수 있고, 어떤 값이 바뀌어도 같이 변해야 하는 구간은 O(logN) 개임.
    static int[] a;
    static void set(int i, int x){
        a[i] = x;
    }

    static int query(int l, int r){
        int result = 0;
        for (int i = l; i < r; i++){
            result += a[i];
        }
        return result;
    }
    public static void main(String[] args) {
        a = new int[]{5, -1, 3, 2, -8};

    }
}
