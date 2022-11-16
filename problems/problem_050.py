# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list):
    list1 = []
    list2 = []
    length = len(list)
    half_length = length//2 + (len(list)%2)

    for i in range(half_length):
        list1.append(list[i])
    for j in range(length//2):
        index = j + half_length
        list2.append(list[index])

    return list1, list2
