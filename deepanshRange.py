from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict
from math import ceil, log2

input = stdin.readline
read = lambda: map(int, input().strip().split())


# Function To return left node index
def left(idx):
    return 2 * idx


# Function To return right node index
def right(idx):
    return 2 * idx + 1


class SegmentTree:
    # Build Tree to store the sum of array in some range at each index of the tree
    def __init__(self, arr):
        self.size = len(arr)
        self.tree_size = 2 ** ceil(log2(self.size))
        self.tree = [0] * 2 * self.tree_size
        self.lazy = self.tree.copy()
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = self.tree[left(idx)] + self.tree[right(idx)]
        self.idx, self.left_node, self.right_node = [1, 0, self.size - 1]

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def range_sum(self, range_left, range_right):
        sum = 0
        range_left += self.tree_size
        range_right += self.tree_size
        self.lazy_update(range_left, range_right)
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

    # Function to update the changes in parent node and pass the information to child node
    def node_update(self, index):
        for node in [left(index), right(index)]:
            if self.lazy[node]:
                self.tree[node] = self.lazy[node]
                self.lazy[node] = 0
                if node < self.tree_size:
                    self.lazy[left(node)] = self.lazy[right(node)] = self.tree[node] // 2

    # Lazily updates the stored information to calculate the new information correctly
    def lazy_update(self, left_index, right_index):
        left_update = []
        right_update = []
        left_index //= 2
        right_index //= 2
        while left_index:
            left_update.append(left_index)
            right_update.append(right_index)
            left_index //= 2
            right_index //= 2
        for lst_update in [left_update, right_update]:
            for index in reversed(lst_update):
                if self.lazy[index]:
                    self.tree[index] = self.lazy[index]
                    self.lazy[index] = 0
                    self.lazy[left(index)] = self.lazy[right(index)] = self.tree[index] // 2

    # Range Update to assign a new_value to every element in range [range_left, range_right] both inclusive
    def range_update(self, range_left, range_right, new_val):
        range_left += self.tree_size
        range_right += self.tree_size
        start_left, start_right = range_left, range_right
        # Lazily update the nodes encountered in path (range_left--> index 1) and (range_right --> index 1)
        self.lazy_update(range_left, range_right)
        while range_left <= range_right:
            if range_left & 1:
                self.tree[range_left] = new_val
                self.lazy[range_left] = 0
                if range_left < self.tree_size:
                    self.lazy[left(range_left)] = self.tree[range_left] // 2
                    self.lazy[right(range_left)] = self.tree[range_left] // 2
                range_left += 1

            if not range_right & 1:
                self.tree[range_right] = new_val
                self.lazy[range_right] = 0
                if range_right < self.tree_size:
                    self.lazy[left(range_right)] = self.tree[range_right] // 2
                    self.lazy[right(range_right)] = self.tree[range_right] // 2
                range_right -= 1
            new_val *= 2
            range_left //= 2
            range_right //= 2
        self.sum_update(start_left, start_right)

    # Update Sum information to the parents of newly updated nodes
    def sum_update(self, start_left, start_right):
        start_left = start_left // 2
        start_right = start_right // 2
        while start_left:
            self.node_update(start_left)
            self.node_update(start_right)
            self.tree[start_left] = self.tree[left(start_left)] + self.tree[right(start_left)]
            self.tree[start_right] = self.tree[left(start_right)] + self.tree[right(start_right)]
            start_left //= 2
            start_right //= 2


n, queries = read()
lst = list(read())
st = SegmentTree(lst)
for q in range(queries):
    temp = list(read())
    if temp[0] == 1:
        c, i, x = temp
        st.range_update(i - 1, i - 1, x)
    else:
        st.range_update(0, n - 1, temp[1])
    print(st.range_sum(0, n - 1))
