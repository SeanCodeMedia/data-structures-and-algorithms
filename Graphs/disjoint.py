# class UnionFind:
#
#     def __init__(self, size):
#         self.root = [x for x in range(size)]
#
#         print(self.root)
#
#     def find(self, x):
#         return self.root[x]
#
#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)
#
#         if root_x != root_y:
#             for x in range(len(self.root)):
#                 if self.root[x] == root_y:
#                     self.root[x] = root_x
#
#     def is_connected(self, x, y):
#         return self.find(x) == self.find(y)
#
#
# uf = UnionFind(10)
# uf.union(0, 1)
# uf.union(1, 2)
# uf.union(2, 3)
# uf.union(3, 4)
# uf.union(4, 5)
# uf.union(5, 6)
# uf.union(6, 7)
#
# print(uf.is_connected(0, 3))  # true
# # print(uf.is_connected(5, 7))  # true
# # print(uf.is_connected(4, 9))  # false
# # # 1-2-5-6-7 3-8-9-4
# # uf.union(9, 4)
# # print(uf.is_connected(4, 9))  # true

'''


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 0  1  2  3  4  5  6  7  8  9

 [0, 0, 2, 3, 4, 5, 6, 7, 8, 9]
 0  1  2  3  4  5  6  7  8  9

'''


class UnionFind:

    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, x):
        return self.root[x]

    def get_disjoint(self):
        return self.root

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for x in range(len(self.root)):

                if self.root[x] == root_y:
                    self.root[x] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


un = UnionFind(10)
un.union(0, 1)
un.union(0, 2)
un.union(5, 6)
un.union(2, 8)

print(un.get_disjoint())
print(un.is_connected(8, 2))