from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def build_graph(words: List[str]) -> Dict[str, Set[str]]:
            graph = defaultdict(set)
            
            for i in range(len(words) - 1):
                w1, w2 = words[i], words[i + 1]
                min_len = min(len(w1), len(w2))
                found_diff = False
                
                for j in range(min_len):
                    if w1[j] != w2[j]:
                        graph[w1[j]].add(w2[j])
                        found_diff = True
                        break
                
                if not found_diff and len(w1) > len(w2):
                    return {}
            
            return graph
        
        def dfs(node: str, graph: Dict[str, Set[str]], visited: Set[str], stack: List[str]) -> bool:
            if node in visited:
                return visited[node] == 1
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor, graph, visited, stack):
                    return False
            stack.append(node)
            return True
        
        graph = build_graph(words)
        if not graph:
            return ''
        
        visited = {}
        stack = []
        
        for node in graph:
            if node not in visited:
                if not dfs(node, graph, visited, stack):
                    return ''
        
        return ''.join(reversed(stack))
