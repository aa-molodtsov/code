def K22(x,t):
    if x==t:
        return 1
    if x>t or x==12:
        return 0
    return K22(x+1,t)+K22(x+4,t)+K22(factorial(x+1),t)
from math import *
print('Ответ:',K22(2,24))
