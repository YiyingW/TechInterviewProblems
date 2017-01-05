class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def oneCase(currentList, k, n):
            print currentList
            if k==0 and sum(currentList) == n:
                if set(currentList) not in result:
                    result.append(set(currentList))
            else:
                # if 1 not in currentList and sum(currentList)+1 <= n:
                #     oneCase(currentList+[1], k-1, n)
                # if 2 not in currentList and sum(currentList)+2 <= n:
                #     oneCase(currentList+[2], k-1, n)
                # if 3 not in currentList and sum(currentList)+3 <= n:
                #     oneCase(currentList+[3], k-1, n)
                # if 4 not in currentList and sum(currentList)+4 <= n:
                #     oneCase(currentList+[4], k-1, n)
                for i in range(1,10):
                    if i not in currentList and sum(currentList) < n:
                        oneCase(currentList+[i], k-1, n)

        oneCase([],k,n)
        result = [list(i) for i in result]
        return result


c = Solution()
print c.combinationSum3(3,9)
