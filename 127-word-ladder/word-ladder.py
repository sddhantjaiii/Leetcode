from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        s.add(beginWord)
        s.remove(beginWord)
        q=deque()
        q.append([beginWord,1])
        while q:
            word=q[0][0]
            step=q[0][1]
            q.popleft()
            if word==endWord:
                return step

            for i in range(len(word)):
                orignal=word
                for ch in string.ascii_lowercase:
                    word=list(word)
                    word[i]=ch
                    word="".join(word)
                    if word in s:
                        q.append([word,step+1])
                        s.remove(word)
                word=orignal
        return 0
                
