# Very Fast with FastIO template
from math import log2, ceil
from sys import stdin
from bisect import bisect_left as bl
from collections import defaultdict

input = stdin.readline


# def lcm(x, y):
#     return (x * y) // gcd(x, y)

def left(idx):
    return 2 * idx


def right(idx):
    return 2 * idx + 1


class SegmentTree:
    # Build Tree to store the sum of array in some range at each index of the tree
    def __init__(self, arr):
        self.size = len(arr)
        self.tree_size = 2 ** ceil(log2(self.size))
        self.tree = [0] * 2 * self.tree_size
        self.lazy = [None] * 2 * self.tree_size
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = self.tree[left(idx)] + self.tree[right(idx)]
        self.idx, self.left_node, self.right_node = [1, 0, self.size - 1]

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = new_val
        start = start // 2
        while start:
            self.tree[start] = self.tree[left(start)] + self.tree[right(start)]
            start //= 2

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def range_sum(self, range_left, range_right):
        sum = 0
        range_left += self.tree_size
        range_right += self.tree_size
        self.lazy_update(range_left)
        self.lazy_update(range_right)
        while range_left <= range_right:
            if range_left & 1:
                self.node_update(range_left // 2)
                sum += self.tree[range_left]
                range_left += 1
            if not range_right & 1:
                self.node_update(range_right // 2)
                sum += self.tree[range_right]
                range_right -= 1
            range_right //= 2
            range_left //= 2
        return sum

    def node_update(self, index):
        for node in [left(index), right(index)]:
            if self.lazy[node] is not None:
                self.tree[node] = self.lazy[node]
                self.lazy[node] = None
                if node < self.tree_size:
                    self.lazy[left(node)] = self.lazy[right(node)] = self.tree[node] // 2

    def lazy_update(self, index):
        lst_update = []
        index //= 2
        while index:
            lst_update.append(index)
            index //= 2
        for index in reversed(lst_update):
            if self.lazy[index] is not None:
                self.tree[index] = self.lazy[index]
                self.lazy[index] = None
                self.lazy[left(index)] = self.lazy[right(index)] = self.tree[index] // 2

    # Range Update to assign a same value to every element in range [range_left, range_right] both inclusive
    def range_update(self, range_left, range_right, new_val):
        range_left += self.tree_size
        range_right += self.tree_size
        start_left, start_right = range_left, range_right
        tree_height = 0
        self.lazy_update(range_left)
        self.lazy_update(range_right)
        while range_left <= range_right:
            if range_left & 1:
                self.tree[range_left] = new_val * 2 ** tree_height
                self.lazy[range_left] = None
                if range_left < self.tree_size:
                    self.lazy[left(range_left)] = self.tree[range_left] // 2
                    self.lazy[right(range_left)] = self.tree[range_left] // 2
                range_left += 1

            if not range_right & 1:
                self.tree[range_right] = new_val * 2 ** tree_height
                self.lazy[range_right] = None
                if range_right < self.tree_size:
                    self.lazy[left(range_right)] = self.tree[range_right] // 2
                    self.lazy[right(range_right)] = self.tree[range_right] // 2
                range_right -= 1
            tree_height += 1
            range_left //= 2
            range_right //= 2
        self.sum_update(start_left)
        self.sum_update(start_right)

    def sum_update(self, index):
        index = index // 2
        while index:
            self.node_update(index)
            self.tree[index] = self.tree[left(index)] + self.tree[right(index)]
            index //= 2

#
# def build(arr):
#     for i in range(n):
#         tree[n + i] = arr[i]
#     for i in range(n - 1, 0, -1):
#         tree[i] = tree[i << 1] + tree[i << 1 | 1]
#
#
# def updateTreeNode(p, value):
#     tree[p + n] = value
#     p = p + n
#     i = p
#     while i > 1:
#         tree[i >> 1] = tree[i] + tree[i ^ 1]
#         i >>= 1
#
#
# def query(l, r):
#     res = 0
#     l += n
#     r += n
#     while l < r:
#         if (l & 1):
#             res += tree[l]
#             l += 1
#         if (r & 1):
#             r -= 1
#             res += tree[r]
#         l >>= 1
#         r >>= 1
#     return res


def two(l, r):
    return abs(st.range_sum(1, n-1) - 2 * st.range_sum(l, r))


# for test in range(int(input())):
n, q = map(int, input().split())
n += 1
lst = [0] + list(map(int, input().split()))
st = SegmentTree(lst)
# store = [0] * (n + 1)
# k = 0
# 5 4
# 6 7 3 9 8
# 2 3
# 1 4 4 12
# 2 5
# 1 1 3 7
#
# for ind, el in enumerate(lst):
#     k += el
#     store[ind] = k
# print(store)
for qu in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        c, l, r, x = s
        st.range_update(l, r, x)
        # for i in range(l, r + 1):
        #     updateTreeNode(i, x)
        """
        # for i in range(l, r + 1):
            # store[i] = store[i - 1] + x
            # lst[i] = x
        # for i in range(r + 1, n + 1):
            # store[i] = store[i - 1] + lst[i]
        """
    if s[0] == 2:
        l = r = s[1]
        d = two(l, r)
        while r + 1 < n and d > two(l, r + 1):
            r += 1
            d = two(l, r)
        print(r)
