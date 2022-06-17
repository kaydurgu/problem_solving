class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        
        lower =  string.ascii_lowercase
        
        q = deque([[beginWord , 1]])
        
        while q:
            x ,step = q.popleft()
            if x == endWord:
                return step
            for i in range(len(x)):
                for z in lower:
                    new_word = x[:i] + z + x[i + 1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        q.append([new_word, step + 1])
        return 0