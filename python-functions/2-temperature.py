def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    if celsius < -100:
        return '{:.2f}'.format(celsius)
    else:
        return celsius