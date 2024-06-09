# paramaters and arguments

def add(x, y):
    print(x+y)
add(3, 4)



#Return statement and recursion in python 

def hello():
    return("hello samir sir")
print(hello())


def sum(a, b):
    return ("The addition of two number is", a+b)

print(sum(23,32))

 #recurision

def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))
    
print (fact(5))




#lamda function 

a = lambda b: b*5
print(a(4))


x = lambda a, b, c: (a+b)*c
print(x(3, 4, 5))