import turtle


def square_fractal(simple_len=10, deep=3):
    '''
    Draws Square Koch curve
    '''
    for degree in [90, 270, 270, 90, 0]:
        if deep <= 1:
            turtle.forward(simple_len)
        else:
            square_fractal(simple_len, deep-1)
        turtle.left(degree)

def box_fractal(simple_len=10, deep=3):
    '''
    Draws Box fractal 
    '''
    for i in range(4):
        square_fractal(simple_len, deep)
        turtle.left(90)

def triangular_fractal(simple_len=3, deep=3):
    '''
    Draws Koch curve 
    '''
    for degree in [60, 240, 60, 0]:
        if deep <= 1:
            turtle.forward(simple_len)
        else:
            triangular_fractal(simple_len, deep-1)
        turtle.left(degree)

def koch_fractal(simple_len=10, deep=3):
    ''' 
    Draws Koch snowflake
    '''
    for i in range(3):
        triangular_fractal(simple_len, deep)
        turtle.right(120)
