# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function

def biggest_gap(nums):
    max_gap = abs(nums[0] - nums[1])
    for i in range(1, len(nums)-1):
        current_num = nums[i]
        next_num = nums[i+1]
        gap = abs(current_num - next_num)
        if gap > max_gap:
            max_gap = gap
    return max_gap
