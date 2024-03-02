import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main1991 {
    static StringBuilder sbPre = new StringBuilder();
//    static StringBuilder sbMid = new StringBuilder();
//    static StringBuilder sbPost = new StringBuilder();
    static int inputToInt (String str){
        if (str.equals(".")) return -1;
        int result = str.charAt(0) - 'A';
        return result;
    }
    static char intToChar (int node){
        char result = (char) ('A' + node);
        return result;
    }
    static void preOrder(int[] leftC, int[] rightC, int root) {
        if (root == -1) return;
        sbPre.append(intToChar(root));
        preOrder(leftC, rightC, leftC[root]);
        preOrder(leftC, rightC, rightC[root]);
    }
    static void midOrder(int[] leftC, int[] rightC, int root) {
        if (root == -1) return;
        midOrder(leftC, rightC, leftC[root]);
//        sbMid.append(intToChar(root));
        sbPre.append(intToChar(root));
        midOrder(leftC, rightC, rightC[root]);
    }
    static void postOrder(int[] leftC, int[] rightC, int root) {
        if (root == -1) return;
        postOrder(leftC, rightC, leftC[root]);
        postOrder(leftC, rightC, rightC[root]);
//        sbPost.append(intToChar(root));
        sbPre.append(intToChar(root));
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
//        int[] parents = new int[N];
//        for (int i = 0; i < N; i++) {
//            parents[i] = i;
//        }
        int[] leftchildren = new int[N];
        Arrays.fill(leftchildren, -1);
        int[] rightchildren = new int[N];
        Arrays.fill(rightchildren, -1);

        for (int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String node = st.nextToken();
            String left = st.nextToken();
            String right = st.nextToken();
            leftchildren[inputToInt(node)] = inputToInt(left);
            rightchildren[inputToInt(node)] = inputToInt(right);
        }
        preOrder(leftchildren, rightchildren, 0);
        sbPre.append("\n");
        midOrder(leftchildren, rightchildren, 0);
        sbPre.append("\n");
        postOrder(leftchildren, rightchildren, 0);
        System.out.println(sbPre);
//        System.out.println(sbMid);
//        System.out.println(sbPost);

    }
}
