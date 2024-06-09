# write a function to find maximum of three numbers in python 
def maximum_num(x, y, z):
    if x > y and x > z:
        print(x, "is the greatest number")
    elif y > x and y > z:
        print(y, "is the greatest number")
    else:
        print(z, "is the greatest number")

maximum_num(12,55,1111)

#write apython function to craete and print a list where the values are square of numbers between 1 and 30

def create_list():
    l = []
    for i in range(1, 31):
        l.append(i**2)


    return l
print(create_list())




#write a python function that takes a number as a parameter and check if the number is prime or out

def check_prime(numb):
    if numb == 1:
        print("it is not a prime number")
    if numb == 2:
        print("it is a prime number")
    if numb > 2: 

        for i in range(2, numb):
            if numb% i == 0:
                print("it is not a prime number")
                break

        else: 
            print("it is a prime number")
check_prime(456)





#write a python function to sum all the numbers in a list

def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return(total)

print(add([4,46,24,516,4564,164,4654]))