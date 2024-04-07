# 세그먼트트리 연습

class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = [0] * (4 * self.length)
        self.build(arr, 0, 0, self.length - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_range(self, l, r):
        return self.query(0, 0, self.length -1, l, r)

    def update_value(self, idx, val):
        self.update(0, 0, self.length - 1, idx, val)
    
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
seg = SegmentTree(nums)
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    print(seg.query_range(min(x, y), max(x, y)))
    seg.update_value(a-1, b)
    