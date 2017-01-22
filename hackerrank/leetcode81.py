class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if len(A) == 0: return False
        l, r = 0, len(A) - 1
        while (l <= r): 
            m = l + (r-l)/2
            if A[m] == target: 
                return True
            elif A[m] < A[r]: # case1: l < m < r
                if A[m] < target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif A[m] > A[r]:
                if A[l] <= target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                r -= 1
        return False


c = Solution()
print c.search([1,3,1,1,1,1], 3)