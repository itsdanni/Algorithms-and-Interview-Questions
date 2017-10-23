# Print all combinations of n pairs of parentheses:
# Algorithm:
# Using recursion, build string from scratch as long as it's valid
# We select either a left or right parens
# can select left as long as there are still left left
# can select right as long as it's syntax correct, meaning the number of
# closed <= number of open brackets
# So we keep track of num_left and num_right

def add_parens_starter(n):
    result = []
    # have to initiate result here since add_parens doesn't return anything
    add_parens(result, n, n, '')
    return result

def add_parens(result, left_rem, right_rem, curr):
    # base case: invalid state
    if left_rem > right_rem or left_rem < 0:
        return
    # we used all the parens
    if left_rem == 0 and right_rem == 0:
        result.append(curr)
    else:
        add_parens(result, left_rem - 1, right_rem, curr + '(')
        add_parens(result, left_rem, right_rem - 1, curr + ')')

if __name__ == "__main__":
    print (add_parens_starter(3))

