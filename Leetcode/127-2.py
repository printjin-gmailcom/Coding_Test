from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        def visitWordNode(visited, othersVisited, queue):
            current_word, length = queue.popleft()
            
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + char + current_word[i+1:]
                    if new_word in othersVisited:
                        return length + othersVisited[new_word]
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
            return None
        
        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        
        while queue_begin and queue_end:
            result = visitWordNode(visited_begin, visited_end, queue_begin)
            if result:
                return result
            
            result = visitWordNode(visited_end, visited_begin, queue_end)
            if result:
                return result
        
        return 0
