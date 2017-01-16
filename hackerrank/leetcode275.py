# [1,2,3,4,4,4,4] => 4
# [1,2,4,4,4] => 3 


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0

        n = len(citations)
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) / 2

            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                r = mid -1
            else:
                l = mid + 1
        return n - l 