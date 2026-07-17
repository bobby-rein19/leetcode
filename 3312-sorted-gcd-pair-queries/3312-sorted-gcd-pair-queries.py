class Solution:
     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxV = max(nums)
        cnt = [0] * (maxV + 1)
        for x in nums:
            cnt[x] += 1

        cntMultiple = [0] * (maxV + 1)
        for d in range(1, maxV + 1):
            total = 0
            for m in range(d, maxV + 1, d):
                total += cnt[m]
            cntMultiple[d] = total

        exact = [0] * (maxV + 1)
        for d in range(1, maxV + 1):
            c = cntMultiple[d]
            exact[d] = c * (c - 1) // 2

        for d in range(maxV, 0, -1):
            for m in range(2 * d, maxV + 1, d):
                exact[d] -= exact[m]

        prefix = [0] * (maxV + 1)
        for d in range(1, maxV + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        ans = []
        for q in queries:
            lo, hi = 1, maxV
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)
        return ans