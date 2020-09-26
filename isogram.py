import re


def is_isogram(string):
    # cleaning the string
    string = string.lower()
    clean_string = re.sub(r"[^a-z]", "", string)

    # check if the set of char is equal length of the string
    return len(set(clean_string)) == len(clean_string)
