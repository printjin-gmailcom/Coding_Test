from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def build_graph(words: List[str]) -> (Dict[str, Set[str]], Dict[str, int]):
            graph = defaultdict(set)
            in_degree = defaultdict(int)
            all_chars = set()
            
            for word in words:
                for char in word:
                    all_chars.add(char)
            
            for i in range(len(words) - 1):
                w1, w2 = words[i], words[i + 1]
                min_len = min(len(w1), len(w2))
                found_diff = False
                
                for j in range(min_len):
                    if w1[j] != w2[j]:
                        if w2[j] not in graph[w1[j]]:
                            graph[w1[j]].add(w2[j])
                            in_degree[w2[j]] += 1
                        found_diff = True
                        break
                
                if not found_diff and len(w1) > len(w2):
                    return None, None
            
            for char in all_chars:
                if char not in in_degree:
                    in_degree[char] = 0
            
            return graph, in_degree
        
        def dfs(node: str, graph: Dict[str, Set[str]], visited: Dict[str, int], stack: List[str]) -> bool:
            if node in visited:
                return visited[node] == 1
            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor, graph, visited, stack):
                    return False
            visited[node] = 1
            stack.append(node)
            return True
        
        graph, in_degree = build_graph(words)
        if graph is None:
            return ''
        
        visited = {}
        stack = []
        
        for char in in_degree:
            if char not in visited:
                if not dfs(char, graph, visited, stack):
                    return ''
        
        return ''.join(reversed(stack))
