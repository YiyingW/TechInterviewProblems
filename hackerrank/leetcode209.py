class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_array = [0]
        for i in nums:
            sum_array.append(sum_array[-1]+i)

        current_res = float('inf')

        for i in range(len(sum_array)):

            
            target = sum_array[i] + s

            
            l, r = i, len(sum_array)

            while l < r:
                mid = l + (r-l)/2
                if sum_array[mid] < target:
                    l = mid + 1
                elif sum_array[mid] >= target:
                    r = mid
            if l < len(sum_array):
                res = l - i
            else:
                res = float('inf')
            current_res = min(current_res, res)


        return current_res

c = Solution()
print c.minSubArrayLen(7, [2,3,1,2,4,3])