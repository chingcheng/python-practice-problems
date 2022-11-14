# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    members_count = 0
    for mem in members_list:
        members_count += 1
    attendees_count = 0
    for attend in attendees_list:
        attendees_count += 1
    members_fifty = members_count/2
    if attendees_count >= members_fifty:
        return True
    else:
        return False
