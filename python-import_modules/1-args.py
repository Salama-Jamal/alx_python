


if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    argument = []

    for i in sys.argv:
        argument.append(i)
    argument.remove(argument[0])

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count ))
    elif count > 1:
        print("{} arguments:".format(count ))

    for j in range(len(argument)):
        print("{}: {}".format(j+1, argument[j]))

       