import collections
'''
For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v.
If we can, then it must be the duplicate edge.

In [37]: import collections
In [38]: dic=collections.defaultdict(set)
In [39]: dic[1].add(2)
In [40]: dic[1].add(3)
In [41]: dic
Out[41]: defaultdict(set, {1: {2, 3}})
In [42]: dic[1]
Out[42]: {2, 3}
In [43]: 1 in dic
Out[43]: True
'''
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def deep_search_first(source, target):
            if source == target:
                return True
            else:
                try:
                    # 已经递归过的就不需要再重复此操作了（应为有（1,2），（2,1），没有此条件会循环递归）
                    if source not in seen:
                        seen.add(source)
                        # return any(deep_search_first(start, target) for start in graphs[source])
                        for start in graphs[source]:
                            if deep_search_first(start, target):
                                return True
                except Exception as e:
                    print(e)
            return False

        graphs = collections.defaultdict(set)

        for s, t in edges:
            # 已经递归的节点
            seen = set()
            if s in graphs and t in graphs and deep_search_first(s, t):
                return s, t
            else:
                graphs[s].add(t)
                graphs[t].add(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))