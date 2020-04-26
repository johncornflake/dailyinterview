'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a list of strings, find the longest common prefix between all strings.

Here's some examples and some starter code.

def longest_common_prefix(strs):
  # Fill this in.

print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''
'''

def longest_common_prefix(strings):
    min_len = len(sorted(strings, key=len)[0])
    return min_len

a = ['helloworld', 'hellokitty', 'hell']
b = ['daily', 'interview', 'pro']

print(longest_common_prefix(a))
