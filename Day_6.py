# # Day 6 ------>>>

# # ---------------Match Case-----------------------

 day = int(input("Enter the day: "))

 match day:
     case 1:
         print("Monday")
     case 2:
         print("Tuesday")
     case 3:
         print("Wednesday")
     case 4:
         print("Thursday")
     case 5:
         print("Friday")
     case 6:
         print("Saturday")
     case 7:
         print("Sunday")
     case _:
         print("Invailid Day")


# -----------------For Loop --------------------------

# string 

name = "Shivam"

for i in name:
    print(i)

# list

fruits = ["Mango", "Strawberry", "Guava", "Grapes", "Litchi"]

for x in fruits:
    print(x)
    for k in x:
        print(k)

# range() function 

for y in range(10):
    print(y)

# range using sss rule (start, stop, step)

for z in range(1,10,2):
    print(z)

# useing break and continue 

for p in range(1,10):
    if p == 6:
        break
    print(p)

for q in range(1,10):
    if q == 6:
        break
    print(q)

for r in range(1,10):
    if r == 6:
        continue

    print(r)
