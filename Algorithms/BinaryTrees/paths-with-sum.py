# You are given a binary tree in which each node contains an integer value
# (which might be positive or negative)
# Design an algorithm to count the number of paths that sum to a given value.
# Path doesn't need to start at the root or a leaf, but must go downwards
# Algorithm for a single path: for each path, at each node, the sum of values to that node so far
# - the sum of values to a node with sum that is the difference between the node
# and target sum: runningSum2 = runningSum1 - targetSum.
# Hash the sums to numPaths (number of times this sum occured)
# do one table for each path to save space
# Adapt this to a tree with DFS

def count_paths_with_sum_main(root, target_sum):
    path_count_table = dict()
    return count_paths_with_sum(root, target_sum, 0, path_count_table)

def count_paths_with_sum(root, target_sum, running_sum, path_count_table):
    if root is None:
        return 0
    running_sum += root.val
    prev_sum = running_sum - target_sum
    total_paths = path_count_table.get(prev_sum)

    # add additional path that starts at the root
    if running_sum == target_sum:
        total_paths += 1
    # increment the pathcount by 1 at that sum, add the sum to table it it's not already there
    increment_hash_table(path_count_table, running_sum, 1)
    # recurse left and right, counting the number of paths with sum target_sum
    total_paths += count_paths_with_sum(root.left, target_sum, running_sum, path_count_table)
    total_paths += count_paths_with_sum(root.right, target_sum, running_sum, path_count_table)
    # after recursing, decrement the value for that sum, this is to undo the changes so that other nodes don't use it
    increment_hash_table(path_count_table, running_sum, -1)

    return total_paths

def increment_hash_table(path_count_table, running_sum, delta):
    new_count = path_count_table.get(running_sum) + delta
    if new_count == 0:
        del path_count_table[running_sum]
    else:
        path_count_table.update(running_sum = new_count)




