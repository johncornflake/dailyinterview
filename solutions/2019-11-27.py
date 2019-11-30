# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#
# Here's a starting point:
#
# class Solution:
#   def reverseWords(self, str):
#     # Fill this in.
#
# print Solution().reverseWords("The cat in the hat")
# # ehT tac ni eht tah

class Solution:
    def reverseWords(self, str):
        ranges = []
        for i, e in enumerate(list(str)):
            if e == ' ': ranges.append(i)
        ranges += [len(str)]
        start = 0
        reversed_words = ''
        for i in ranges:
            reversed_words += str[start:i][::-1] + ' '
            start = i+1

        return reversed_words

s = "The cat in the hat"
s2 = "Here's another test"
print(Solution().reverseWords(s2))
