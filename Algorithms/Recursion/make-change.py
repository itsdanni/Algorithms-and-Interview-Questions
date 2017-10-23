# Given an infinite number of 25, 10, 5, 1, calculate number of ways to represent n cents
# Algorithm:
# suppose we want to make change for 100:
# make_change(100) = make_change(100 using 0 quarters)
#                  + make_change(75 using 0 quarters)
#                  + make_change(50 using 0 quarters)
#                  + make_change(25 using 0 quarters)
#                  + 1
# each of these expand to something like
# make_change(25 using 0 quarters, 0 dimes)
#                                  1 dime)
#                                  2 dimes)
# base case: a fully reduced problem: make 50 using 0 quarters, 5 dimes (5*10 = 50)

def make_change_no_memoi(amount, denoms, index):
    if index > len(denoms) - 1:
        return 1
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_rem = amount - i * denom_amount
        ways += make_change_no_memoi(amount_rem, denoms, index + 1)
        i += 1
    return ways

# to optimize, we will have a mapping for (amount, index)
def make_change(amount, denoms, index, memo):
    if memo[amount][index] > 0:
        return memo[amount][index]

    if index >= len(denoms) - 1:
        return 1

    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_rem = amount - i * denom_amount
        ways += make_change_no_memoi(amount_rem, denoms, index + 1)
        i += 1
    memo[amount][index] = ways
    return ways
