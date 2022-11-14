# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if values == []:
        return None
    sum = 0
    for nums in values:
        sum += nums
    return sum
