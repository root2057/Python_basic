for i in range (2, 32):
    print(i)

n = 7
for i in range (1, 11):
    print(n, "x", i, "=", n*i)


#while loop
a = 0
while a <= 5:
    print(a)
    a += 1


# while true 
while True:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))

    print(num1 + num2)


for x in range(1, 6):
    for y in range(1, x+1):
        print(y, end="")
    print()