# Day 4 ----->>

#Input function

name = input("enter your name at least 6 latters ")
print(name) #it always take input as a string

#if we want to take input as a integer use typecasting
#Example:

b = int(input("Enter the the integer"))
print(b)


# String

#Multiline string
c = """hello
My mame is
shivam"""

print(c)

print("string slicing started")
#Accsesing character of string

#name = "shivam"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


#lenght of string

print(len(name))

#String slicing

print(name[0:5])
print(name[:5]) #slicing from start
print(name[0:]) #slicing till end
print(name[-4:5]) #slicing using negative index



