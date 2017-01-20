class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l, r = 0, x

        while l < r:
            mid = l + (r - l + 1)/2

            if array[mid]**2 > x:
                r = mid - 1
            else:
                l = mid 
        return r