class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        words.reverse()
        print(words)
        s = ''
        for word in words:
            if word != '':
                s = s + word.strip() + ' '
        s = s.rstrip()
        return s