class Solution:
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        prefixGcd = []
        mx = 0
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(gcd(x, mx))
        prefixGcd.sort()

        total = 0
        i, j = 0, n - 1
        while i < j:
            total += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        return total