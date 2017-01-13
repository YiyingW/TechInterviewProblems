import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                result += cmap[k] * (cmap[k] - 1)
        return result

c = Solution()
print c.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])

