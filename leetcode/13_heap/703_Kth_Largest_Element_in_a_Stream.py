class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = [0]
        self.heapify(nums)
        while len(self.heap) > k + 1:
            self.pop()

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

        while len(self.heap) > self.k + 1:
            self.pop()
        return self.heap[1]

    def percolate_down(self, i=1):
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                # Swap right child
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # Move last value to root
        self.heap[1] = self.heap.pop()
        self.percolate_down()

        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        # 0-th position is moved to the end

        self.heap.extend(arr)
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            self.percolate_down(cur)
            cur -= 1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    test_kl = KthLargest(3, [4, 5, 8, 2])
    print(test_kl.heap)
    print(test_kl.add(3), "= 4")
    print(test_kl.heap)
    print(test_kl.add(5), "= 5")
    print(test_kl.heap)
    print(test_kl.add(10), "= 5")
    print(test_kl.heap)
    print(test_kl.add(9), "= 8")
    print(test_kl.heap)
    print(test_kl.add(4), "= 8")
    print(test_kl.heap)
