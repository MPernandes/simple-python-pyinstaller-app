def add2(arg1, arg2):
    try:
        return float(arg1) + float(arg2)
    except ValueError:
        return str(arg1) + str(arg2)
