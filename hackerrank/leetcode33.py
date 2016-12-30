class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if len(A) == 0: return -1
        l, r = 0, len(A) - 1
        if l == r: 
            if A[l] == target: 
                return l
            else:
                return -1
        while (l <= r): 
            m = (l+r)/2 
            print m
            if A[m] == target: return m
            elif A[l] <= A[m] <= A[r]: # case1: l < m < r
                if A[m] > target:
                    r = m - 1
                else:
                    l = m  + 1
            elif A[m] < A[l]:
                if target > A[m] and target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif A[m] >= A[l]:
                if target >= A[l] and target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                return -1
        return -1



c = Solution()
print c.search([1,3], 3)