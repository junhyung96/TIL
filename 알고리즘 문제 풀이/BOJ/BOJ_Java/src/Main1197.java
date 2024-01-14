import java.io.IOException;
import java.util.Arrays;

public class Main1197 {

    static Edge[] edges;

    public static void main(String[] args) throws IOException {
        int V = readInt();
        DisjointSet disjointSet = new DisjointSet(V+1);
        int numEdges = readInt();
        edges = new Edge[numEdges];
        for (int i = 0; i < numEdges; ++i) {
            int u = readInt();
            int v = readInt();
            int w = readInt();
            edges[i] = new Edge(u, v, w);
        }
        Arrays.sort(edges, 0, numEdges);

        int sumWeight = 0;
        int cnt = 0;
        for (Edge e : edges) {
            if (disjointSet.isInSameGroup(e.u, e.v)) continue;
            disjointSet.union(e.u, e.v);
            sumWeight += e.w;
            cnt++;
            if (cnt == V-1) break;
        }

        System.out.println(sumWeight);
    }

    static int readInt() throws IOException {
        int val = 0;
        boolean negative = false;
        do {
            int c = System.in.read();
            if (c == '-') {
                negative = true;
                continue;
            }
            if (c == ' ' || c == '\n') break;
            val = 10*val + c-48;
        } while (true);
        return negative ? -val : val;
    }
}

class Edge implements Comparable<Edge> {
    int u, v, w;
    Edge(int u, int v, int w) { this.u = u; this.v = v; this.w = w; }

    @Override
    public int compareTo(Edge e) { return this.w - e.w; }
}

class DisjointSet {
    private int[] roots;

    DisjointSet(int N) {
        roots = new int[N];
    }

    public boolean isInSameGroup(int u, int v) {
        return findRoot(u) == findRoot(v);
    }

    public void union(int u, int v) {
        int ru = findRoot(u);
        int rv = findRoot(v);

        if (ru == rv) return;

        if (roots[ru] < roots[rv]) {
            roots[rv] = ru;
        } else {
            int rankU = roots[ru];
            roots[ru] = rv;
            if (rankU == roots[rv]) roots[rv]--;
        }
    }

    public int findRoot(int u) {
        if (roots[u] <= 0) return u;

        return roots[u] = findRoot(roots[u]);
    }

}
