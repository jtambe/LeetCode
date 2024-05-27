class Solution:
    def frequencySort(self, s: str) -> str:

        dict = {}
        for char in s:
            if char in dict:
                dict[char] = dict[char] + 1
            else:
                dict[char] = 1

        # sort dictionary using value from kv in reverse direction
        sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        print(sorted_list)

        result = ""
        for k in sorted_list:
            for i in range(k[1]):
                result = result + k[0]

        print(result)
        return result