class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        def search(current, n):
            if n == 0: 
                result.append(current)
                return

            for i in nums:
                
                if current == []:
                    search(current+[i], n-1)
                else:
                    current_max = max(current)
                    
                    if i > current_max:
                        search(current+[i], n-1)

        for i in range(0, len(nums)+1):
            search([], i)

        return result

c = Solution()
print c.subsets([0])

