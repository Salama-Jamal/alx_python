


#Write a function that returns a set of common elements in two sets.
def common_elements(set_1, set_2):
    arr = []
    for i in set_1:
        for j in set_2:
            if i == j:
                arr.append(i)
    return arr