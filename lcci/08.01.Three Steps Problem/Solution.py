class Solution:
    def waysToStep(self, n: int) -> int:
        mod = 10**9 + 7

        def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            m, n = len(a), len(b[0])
            c = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(len(a[0])):
                        c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod
            return c

        def pow(a: List[List[int]], n: int) -> List[List[int]]:
            res = [[4, 2, 1]]
            while n:
                if n & 1:
                    res = mul(res, a)
                n >>= 1
                a = mul(a, a)
            return res

        if n < 4:
            return 2 ** (n - 1)
        a = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
        return sum(pow(a, n - 4)[0]) % mod
