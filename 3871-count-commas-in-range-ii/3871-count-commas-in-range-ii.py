class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        p = 1000
        commas = 1

        while p <= n:
            ans += n - p + 1
            p *= 1000
            commas += 1

            if p <= n:
                ans += n - p + 1
                p *= 1000

        return ans
        