def odd(num):
    if not num/2 == num//2:
        return True
    return False

def even(num):
    if num/2 == num//2:
        return True
    return False

def next(num):
    if odd(num):
        return (num*3)+1
    return num/2

def calculate(num):
    while not finished:
        num = next(num)
        if num == 1:
            