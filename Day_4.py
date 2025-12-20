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

#String Methods

s1 = "abcdefghi"
print(s1.upper()) #uppercase methods

s2 = "ABCDEFGHI"
print(s2.lower()) #lowercase methods

s3 = " Heloo World "
print(s3.strip())  #strip method

s4 = "heloo world sss"
print(s4.rstrip("s")) #rstrip method

s5 = "silver spoon"
print(s5.replace("sp","m"))  #replace method 

s6 = "silver spoon"
print(s6.split())  #split methods

s7 = "silver spoon"
print(s7.capitalize())  #capitlize methods

print(s7.center(15))  #center methods

print(s7.count("s"))  #count methods

print(s7.endswith("spoon"))  #endswith methods

print(s7.find("oo"))  #find methods

print(s7.index("spoon"))  #index methods

s8 = "helloworld"
print(s8.isalnum())  #isalnum methods

print(s8.isalpha())  #isalpha methods

s9 = "HELOO WORLD"
print(s9.isupper())  #isupper methods

s10 = "heloo world"
print(s10.islower()) #islower methods

print(s9.isprintable()) #isprintable methods

print(s10.isspace())  #isspace methods

print(s3.istitle())  #istitle methods

print(s10.startswith("heloo"))  #startwith methods

print(s10.swapcase())  #swapcase methods

print(s10.title())  #title methods

