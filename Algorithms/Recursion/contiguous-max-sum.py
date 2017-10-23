# Given an array of both positive and negative integers, find the contiguous subsequence
# with the largest sum
# e.g. [2, 5, -8, 3, -2, 4, -10]
# Algorithm: observe that we always want to add positive numbers
# we may want to include negative numbers when it's absolute value is smaller than the positive sum

def contiguous_max_sum(nums):
    max_sum = 0
    shortened = shorten(nums)
    temp_sum = 0
    for i in range(len(shortened)):
        if shortened[i] > 0:
             max_sum = max(max_sum, shortened[i] + temp_sum)
        else:
            if abs(shortened[i]) < max_sum:
                temp_sum += (shortened[i] + max_sum)
    return max_sum

# shortens the nums array to alternating positive and negative numbers
def shorten(nums):
    shortend = []
    positives = 0
    negatives = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            positives += nums[i]
            if negatives < 0:
                shortend.append(negatives)
                negatives = 0
        elif nums[i] <= 0:
            negatives += nums[i]
            if positives > 0:
                shortend.append(positives)
                positives = 0
    if positives > 0:
        shortend.append(positives)
    return shortend

if __name__ == "__main__":
    print (contiguous_max_sum([3, 2, -5, 8, 9]))
