class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                result.append(nums)
                return
            for x in range(start+1, 10):
                search(x, cnt+1, sums+x, nums+[x])
        search(0, 0, 0, [])
        return result



c = Solution()
print c.combinationSum3(3,9)
