class Solution:
      def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def popcount(x):
            c = 0
            while x:
                c += x & 1
                x >>= 1
            return c

        result = []
        for h in range(12):
            for m in range(60):
                if popcount(h) + popcount(m) == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result