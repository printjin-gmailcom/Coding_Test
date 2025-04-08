from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        patternDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patternDict[pattern].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, length = queue.popleft()
            
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for word in patternDict[pattern]:
                    if word == endWord:
                        return length + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, length + 1))
        
        return 0
