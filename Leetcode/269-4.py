from typing import List, Dict, Set
from collections import deque, defaultdict

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
        
        def topological_sort(graph: Dict[str, Set[str]], in_degree: Dict[str, int]) -> str:
            queue = deque([char for char in in_degree if in_degree[char] == 0])
            order = []
            
            while queue:
                char = queue.popleft()
                order.append(char)
                for neighbor in graph[char]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(order) == len(in_degree):
                return ''.join(order)
            else:
                return ''
        
        graph, in_degree = build_graph(words)
        if graph is None:
            return ''
        
        return topological_sort(graph, in_degree)
