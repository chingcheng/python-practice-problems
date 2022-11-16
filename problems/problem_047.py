# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    upper_met = 0
    lower_met = 0
    digit_met = 0
    special_met = 0

    if len(password) >= 6 and len(password) <= 12:
        for values in password:
            if values.isalpha():
                if values.isupper():
                    upper_met += 1
                elif values.islower():
                    lower_met += 1
            elif values.isdigit():
                digit_met += 1
            elif values == "$" or values == "!" or values == "@":
                special_met += 1

        if upper_met > 0 and lower_met > 0 and digit_met > 0 and special_met > 0:
            return True
        else:
            return False
    else:
        return False
