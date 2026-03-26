#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if not (isinstance(x, int) or x <= 0 or isinstance(my_list, list)):
            raise ValueError
        result = ''
        for idx, value in enumerate(my_list):
            if idx < x:
                result += str(value)
            else:
                break
        result = int(result)
        return result
    except:
        return 0
