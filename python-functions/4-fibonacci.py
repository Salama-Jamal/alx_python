def fibonacci_sequence(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        seq = [0,1]
        while(len(seq) < n):
            seq.append(seq[-1]+seq[-2])
        return seq