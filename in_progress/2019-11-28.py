# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.
#
# Here is a starting point:
#
# def findRanges(nums):
#   # Fill this in.
#
# print findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15])
# # ['0->2', '5->5', '7->11', '15->15']

# def findRanges(nums):
#     nums = list(set(nums))
#     res = []
#     cur_ind = 0
#     for index, element in enumerate(nums):
#         if index < cur_ind:
#             pass
#         else:
#             print('trying')
#             for i, e in enumerate(nums[index:]):
#                 cur_ind = i+index
#                 if e == element+i:
#                     end = e
#                 else:
#                     res.append(f'{element}->{end}')
#                     #cur_ind = i+index
#                     break
#
#     return res




l = [1, 3,4,5, 7,7,7, 10,11,12]
