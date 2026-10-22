class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        count = 1
        length = len(beginWord)
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(length):
                    temp = word
                    for c in range(97, 123):
                        temp = temp[:i] + chr(c) + temp[i+1:]
                        if temp in word_set:
                            q.append(temp)
                            word_set.remove(temp)
            count += 1

        return 0