class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string += i  
        new_string = new_string.lower()
        return new_string[::-1] == new_string
        