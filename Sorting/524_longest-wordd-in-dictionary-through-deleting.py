"""
Given a string s and a string array dictionary, 
return the longest string in the dictionary that can be formed by deleting some of the given string characters. 
If there is more than one possible result, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.
 

Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""

from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        # sorted_list = sorted(dictionary, key=lambda x :-len(x))
        dictionary.sort()

        result = ""
        for word in dictionary:
            if len(word) > len(result):
                i = 0
                cur_word = ""
                for ch in word:
                    while i < len(s):
                        if s[i] == ch:
                            cur_word += s[i]
                            i += 1                        
                            break
                        i += 1
                if cur_word == word:
                    result = cur_word if len(cur_word) > len(result) else result

        return result



                    


        