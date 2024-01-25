

#Write a function that returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if len(sentence) > 0 else None
    return length, first