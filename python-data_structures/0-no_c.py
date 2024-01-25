

#function that removes all characters c and C from a string.
def no_c(my_string):
    arr = []

    for char in my_string:
        if char != "c" and char != "C":
            arr.append(char)
    string = ''.join(str(x) for x in arr)
    return string