# write a program to check if a number is postive
num = int(input("enter a number here: "))
if num > 0:
    print("it is postive")

#write a program to check whether a number is odd or even 

number = int(input("enter a number here: "))
if number % 2 == 0:
    print("it is an even number")
else:
    print("it is an odd number")


# write to create area calculator
print("********AREA CALCULATOR ************")
print("""press 1 to get the area of squre 
press 2 to get the area of retangle)
press 3 to get the area of circle)
press 4 to get the area of triangle """)

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    side = float(input("enter the length of one side: "))
    area = side**2
    print("the area of square is: ", area)


elif choice == 2:
    length = float(input("enter the length of the rectangle: "))
    width = float(input("enter the width of the rectangle: "))
    area = length * width
    print("ther area of rectangle is ", area)


elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = ((22/7) * (radius**2))
    print("ther area of circle is ", area)


elif choice == 4:
    base = float(input("enter the base of the triangle: "))
    height = float(input("enter the height of the triangle: "))
    area = 0.5 * base *height
    print("ther area of triangle is ", area)

else: 
    print("invalide number ")

print("Process finished with exit code 0")


#write a program check whether the passed letter is a vowel or not 

letter = input("enter a letter here: ")
if letter in "aeiou":
    print("it is a vowel")
else: 
    print("it is not a vowel")