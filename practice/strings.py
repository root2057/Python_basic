a = "Harry Potter and the Goblet of Fire"

print(len(a))

print(a.count("o"))

print(a.upper())

print(a.lower())

print(a.index("o", 15, 34))

print(a.capitalize())

print(a.casefold())

print(a.find("o"))


name = "samir"
age = 24
b = "my name is {}. and my age is {}"
print(b.format(name, age))



print(name.center(20, "*"))




# STRING FUNCTION 

g = "1.234"
f = "Hello 123@"
e = " "
d = "HELLO"
c= "123456"
y = "Hello123"
x = "hello"
h = "hello admin what do you mean admin "

print(x, x.isalnum())
print(y, y.isalnum())
print(c, c.isalnum())
print(f, f.isalnum())


print(x, x.isalpha())


print(x, x.isdecimal())
print(g, g.isdecimal())
print(c, c.isdecimal())

print(g, g.isdigit())
print(c, c.isdigit())
print(y, y.isdigit())

print(y, y.isnumeric())
print(c, c.isnumeric())
print(e, e.isnumeric())


print(x, x.islower())
print(d, d.islower())

print(x, x.isupper())
print(y, y.isupper())



print(e, e.isspace())
print(f, f.isspace())


print(d, d.istitle())
print(f, f.istitle())
print(h, h.istitle())





# String method


m = "Harry Potter"

print(m.endswith("P"))
print(m.endswith("t", 6, 9))


print(m.startswith("h"))



print(m.swapcase())


print(m.strip())


n = "#JKLF#KJFD#KJFDA#FDKLAJ"
k = "hello. my name is samir. i am 23 years old"
print(n.split("#"))
print(k.split("."))