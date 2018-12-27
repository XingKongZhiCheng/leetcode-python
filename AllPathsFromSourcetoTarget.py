import collections
class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # 从终点往回寻找，
        # 中间的一些点会产生分支
        # 但是肯定是在之前一个完整分支的基础上
        # 找到该分支（最后一个元素）在前一个完整路径的位置，补齐路径
        '''
        [[0, 1, 7], [0, 1, 4, 7], [0, 1, 2, 4], [0, 3, 4], [0, 1, 2, 3], [0, 1, 6, 7], [0, 1, 2, 6], [0, 3, 6], [0, 1, 2, 3], [0, 1, 4, 6], [0, 1, 2, 4], [0, 3, 4], [0, 1, 2, 3], [0, 1, 5, 6], [0, 1, 4, 5], [0, 1, 2, 4], [0, 3, 4], [0, 1, 2, 3], []]
        [[0, 1, 7], [0, 1, 4, 7], [0, 1, 2, 4, 7], [0, 3, 4, 7], [0, 1, 2, 3, 4, 7], [0, 1, 6, 7], [0, 1, 2, 6, 7], [0, 3, 6, 7], [0, 1, 2, 3, 6, 7], [0, 1, 4, 6, 7], [0, 1, 2, 4, 6, 7], [0, 3, 4, 6, 7], [0, 1, 2, 3, 4, 6, 7], [0, 1, 5, 6, 7], [0, 1, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7], [0, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]
        '''
        def search(target):
            for i, sub in enumerate(graph):
                for j in sub:
                    if j == target:

                        out[-1] = [j] + out[-1]
                        if i != 0:
                            # 有多条路径
                            # if j == out[-1][0]:
                            #     out.append(out[-1])
                            search(i)
                        else:
                            out[-1] = [i] + out[-1]
                            out.append([])
                            # out.insert(0, out.pop())

        out = []
        if not any(graph):
            return []
        else:
            length = len(graph)
            out.append([])
            search(length - 1)
        print(out)
        for i, e in enumerate(out):
            if 0 not in e:
                out = out[:i] + out[i + 1:]
                continue
            if length - 1 not in e:
                index = out[i-1].index(e[-1])
                out[i] += out[i-1][index+1:]

        return out


if __name__ == '__main__':
    sol = Solution()
    graph_input = [[3,1],[4,6,7,2,5],[4,6,3],[6,4],[7,6,5],[6],[7],[]]
    print(sol.allPathsSourceTarget(graph_input))