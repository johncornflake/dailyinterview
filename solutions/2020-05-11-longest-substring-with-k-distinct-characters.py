'''
Hi, here's your problem today. (You've reached the end of the problems for now - in the meanwhile, here is a random question. And visit
CoderPro
 for more practice!) This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s
that contains at most k
distinct characters.For instance, given the string:aabcdefff
and k = 3, then the longest substring with 3 distinct characters would be  defff.
The answer should be 5.
Here's a starting point:
def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
print(longest_substring_with_k_distinct_characters('aabcdefff', 3)

# 5 (because 'defff' has length 5 with 3 characters)
'''

def longest_substring_with_k_distinct_char(s, k):
    substrings = []
    for i in range(0, len(s) - 1):
        substr = ''
        for char in s[i:]:
            # if there are less than 3 unique chars or the char is in the substr, add to it.
            if len(set(substr)) < k or char in substr: substr += char

        substrings.append(substr)

    # I'm not sure the purpose of this question, but in the event there are more than
    # one substrings of k length, it should return them all in a list.
    max_str_len = len(max(substrings, key=len))
    res = [ss for ss in substrings if len(ss) == max_str_len]

    # should it return an empty list if there are not at least k characters?
    return res


t = 'aabcdefff'
t2 = 'aabbccddeeff'
t3 = 'aaaaaaa'

print(longest_substring_with_k_distinct_char(t, 3))
print(longest_substring_with_k_distinct_char(t2, 3))
print(longest_substring_with_k_distinct_char(t3, 2))
