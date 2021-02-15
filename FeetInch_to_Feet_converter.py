
import re


def convert(to_convert):
    """
    Used to convert measurements made in feet" inches' to float number usable in software.

    arg : to_convert : A string with a format [feet]" inches'.
    Supports special characters like dashes (i.e. 27'-4 5/16")

    Example 1 :
    foo = "27'-4 5/16\""
    bar = convert(foo)
    print(bar)
    >>> 27.359375

    Example 2:
    foo = "1'-4\""
    bar = convert(foo)
    print(bar)
    >>> 1.3333333333333333
    """

    # We first separate the feet part and the inches part in 2 variables (it's str format)
    feet, raw_inches = to_convert.split(sep="'")

    # We use regex to get rid of any character that is not alphanumeric or "/" ([\w/] part) in the
    # inches part. Example : 4 5/16" is now ['4', '5/16'], still in str format
    raw_inches = re.findall(r"[\w/]+", raw_inches)

    # Here I'm going to use eval() to turn numbers and operations in string format into number format.
    # For example it turns the string '1/2' into 0.5
    # I then store the values in a list to use them in later operations
    inches = []
    for elt in raw_inches:
        inches.append(eval(elt))

    # We sum the round part and the float part it it exists
    inches = sum(inches)

    # I convert the feet value which was still a string into a number using eval again
    # and convert it to inches by dividing it by 12.
    feet = eval(feet) + inches / 12

    return feet


# Example code
# to_convert = "2'-8\""
# print(convert(to_convert))
