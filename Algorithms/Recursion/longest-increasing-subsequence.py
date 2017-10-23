# Time:  O(nlogn)
# Space: O(n)
#
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
# Algorithm 1: O(n2)
# for each sequence starting from 0 to i, the LIS is the longest sequence from 0 to i-1
# whose tail is smaller than the number at i: the tail is the number at i

def longest_increasing_dp(nums):
    lengths = []
    for i in range(len(nums)):
        lengths.append(1)
        for j in range(i):
            if nums[j] < nums[i]:
                lengths[i] = max(lengths[i], lengths[j] + 1)
    return max(lengths if lengths else 0)
