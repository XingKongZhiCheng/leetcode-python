class Solution:
    '''
    我使用了构筑连通图求解的
    '''
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graphs = []

        def find(edge):
            for i, graph in enumerate(graphs):
                if edge[0] in graph or edge[1] in graph:
                    return i
            return -1

        def combine_graphs():
            try:
                for i in range(len(graphs) - 1):
                    for j in range(i + 1, len(graphs)):
                        if set(graphs[i]) & set(graphs[j]):
                            graphs[i] += graphs[j]
                            del graphs[j]
            except Exception as e:
                print(e)

        # 构建连通图
        graphs = []
        for edge in edges:
            if len(graphs) > 1:
                combine_graphs()
            index = find(edge)
            if index == -1:
                graphs.append(edge)
            elif edge[0] not in graphs[index]:
                graphs[index].append(edge[0])
            elif edge[1] not in graphs[index]:
                graphs[index].append(edge[1])
            else:
                return edge


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection())


