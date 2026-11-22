def Multi(a,b,c,d):
    if type(a) != int or type(b) != int or type(c) != int or type(d) != int:
        raise(TypeError)
    else:
        return a * b * c * d

try:
    print(Multi(1,2,'4',3))
except TypeError:
    print('에러발생')

