from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        def formPath(path, node):
            for nextNode in graph[node]:
                if nextNode == n-1:
                    paths.append(path+[nextNode])
                else:
                    formPath(path+[nextNode], nextNode)
        formPath([0], 0)
        return paths
    
    
    
'''
https://leetcode.com/problems/all-paths-from-source-to-target/description/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).
'''