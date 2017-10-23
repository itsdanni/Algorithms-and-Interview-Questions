# compute all permutations of a string of unique characters
# Algorithm: base case: len(str) == '', return
# question: accumulating results in permutations, recursion returns

def permutation_unique_starter(str):
    return permutation_unique(str, 0, [])

def permutation_unique(str, index, permutations):
    # base case:
    if index > len(str) - 1 or str == '':
        return
    elif index == 0:
        permutations.append(str[index])
        permutation_unique(str, index + 1, permutations)
    else:

        new_permutations = []
        for perm in permutations:
            for pos in range(len(perm) + 1):
                new_str = perm[0:pos] + str[index] + perm[pos:]
                new_permutations.append(new_str)
        print(new_permutations)
        return permutation_unique(str, index + 1, new_permutations)

if __name__ == "__main__":
    permutation_unique_starter('abcd')
