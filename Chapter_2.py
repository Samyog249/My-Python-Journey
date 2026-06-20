#This is String Splite 
a = "Hello How are You"
print(a[6:9:1])
print(a[14:17:1])
print(a[0:6:1])

#Let's Talk about type conversion
# 1-Implicit Type Conversion
# Python automatically converts smaller data types (e.g., int) to larger ones (e.g., float) during operations to avoid data loss.
# 2-Explicit Type Conversion
#Use Python's built-in functions to manually convert data types: int(): Converts a value to an integer. float(): Converts a value to a floating-point number. str(): Converts a value to a string. bool(): Converts a value to a Boolean.



# #now let's Talk about Output in Python
name = "Samyog"
age = 19 
# # This is using formated string f is used for formating and write your variables in { }
print(f"Hi my name is {name} and My age is {age}") 

# #this is without formating String
print("Hi my name is",name,"And my age is",age)

# let's Talk about Input in Python 
age = input("What is your age:-") 
print("Your age is",age)
# When you give a input in any data type it will always give you string there is a problem
# but you can change data type use Explicite type conversion
# for eg:
age1 = int(input("What is your age:"))
print(f"Your age is {age1}")
# now it is int

# Arithmatic Operators
# Number- int,float,complex
# there are 7 Arithmatic Operators They are
# (+ , - , / , * , % , ** , //)

a = 20;
b = 10;
print(a+b)
print(a-b)
# there is a problem when we divide 2 number it all change into float 
print(a/b)
# so for takel this problem we use floer devision "//"
print(a*b)
print(a%b)
print(a//b)
print(a**b) # power 

# Comparision Operators
#(== , != , <=, >= ,< , >) for eg:
print(12==12)
print(12!=12)
print(12<=12)
print(12>=12)
print(12<12)
print(12>12)

# Logical Operators
# and, or ,not . for eg;
print(24 < 25 and 22 > 21) # if any 1 is false it will give answer false
print(12<11 or 12 > 14) # if any 1 is true it will give answer true 
print(not 12==13) # if there is a false but it will convert true if true than it will give false

# Assignment Operators
# ( = , += , -= , *= , //= , **=, %=) for eg:
#there is an number 10 we need to add it 4 times we do:
ao = 10;
ao = ao+10; # 10 + 10 = 20
ao = ao+10; # 20 + 10 = 30
ao = ao+10; # 30 + 10 = 40
ao = ao+10; # 40 + 10 = 50
print(ao)

# But if we use Assignment operator we don't need to write that ao = ao + 10 we use:
aa= 10;
aa +=10
aa +=10
aa +=10
aa +=10
print(aa)