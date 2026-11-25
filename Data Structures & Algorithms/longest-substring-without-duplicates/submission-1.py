class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_word = ""
        count = 0
        loc_count = 0
        for i in s:
            if i not in new_word:
                new_word += i
                loc_count +=1
                count = max(loc_count, count)
                print(count)
            else:
                new_word = new_word[new_word.index(i)+1:]
                new_word += i
                loc_count = len(new_word)
        return max(loc_count, count)
                




        