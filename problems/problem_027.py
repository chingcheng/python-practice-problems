# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if values == []:
        return None
    max_value = values[0]
    for num in values:
        if num > max_value:
            max_value = num
    return max_value
