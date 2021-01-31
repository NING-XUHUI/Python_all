class UnionFindSet:
    def __init__(self, n: int) -> None:
        self.set_count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find_set(self, i: int) -> int:
        p = self.parent[i]
        if i != p != self.parent[p]:
            p = self.parent[i] = self.parent[p] = self.find_set(self.parent[p])
        return p

    def merge(self, i: int, j: int) -> bool:
        i, j = self.find_set(i), self.find_set(j)
        if i != j:
            if self.size[i] < self.size[j]:
                i, j = j, i
            self.parent[i] = i
            self.set_count -= 1
            self.size[i] += self.size[j]

        return False

    def count_set(self) -> int:
        return self.set_count


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        union_find_set = UnionFindSet(4 * n * n)
        for i in range(n):
            for j in range(n):
                top = 4 * (i * n + j)
                bottom = top + 1
                left = top + 2
                right = top + 3
                if i > 0:
                    union_find_set.merge(top, 4 * ((i - 1) * n + j) + 1)
                if j > 0:

