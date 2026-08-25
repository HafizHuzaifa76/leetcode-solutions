from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) > len(s) or len(s) == 0 or len(words) == 0:
            return []

        words_map = {}
        result = []
        words_len = len(words)
        size = len(words[0])
        combine_length = size * words_len
        for i in range(len(words)):
            if words[i] in words_map:
                words_map[words[i]] += 1
            else:
                words_map[words[i]] = 1
        
        for i in range(len(s)):
            total = i + combine_length
            if total <= len(s):
                sub_string = s[i: total]
                chunks = [sub_string[i:i+size] for i in range(0, len(sub_string), size)]
                chunks_map = {}
                for c in range(len(chunks)):
                    if chunks[c] in chunks_map:
                        chunks_map[chunks[c]] += 1
                    else:
                        chunks_map[chunks[c]] = 1
                if chunks_map == words_map:
                    result.append(i)

        return result


# // previous solution
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # if len(words) > len(s) or len(s) == 0 or len(words) == 0:
        #     return []

        # result = []
        # w = words[0]
        # same = True
        # for i in range(len(words)-1):
        #     w += words[i+1]
        #     if words[i] != words[i+1]:
        #         same = False
            
        # if same:
        #     indexes = set()
        #     if w in s:
        #         index = [i for i in range(len(s)) if s.startswith(w, i)]
        #         indexes.update(index)
        #     return list(indexes)


        # def backtrack(current, remaining):
        #     if not remaining:
        #         result.append(''.join(current))
        #         return

        #     for word in remaining:
        #         current.append(word)

        #         new_remaining = remaining.copy()
        #         new_remaining.remove(word)

        #         backtrack(current, new_remaining)

        #         current.pop()

        # backtrack([], words)

        # indexes = set()
        # for word in result:
        #     if word in s:
        #         index = [i for i in range(len(s)) if s.startswith(word, i)]
        #         indexes.update(index)

        # return list(indexes)