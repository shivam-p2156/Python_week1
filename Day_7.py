# Day 7 ---------->>>>

# ----------------- While loop -------------

i = 1

while i <= 3:
    print(i)
    i = i+1

else:              # else with while loop 
    print("Loop finished")

# break in while loop 

i=1
while i<=10:
    if i == 5:
        break
    print(i)
    i = i+1

# continue in while loop 

i=0
while i<=10:
    i = i+1
    if i == 5:
        break
    print(i)
    

# do - while loop in python .

while True:
    num = input("Enter the Pin: ")
    if num == "1234" :
        print("Pin is correct")
        break
    else:
        print("Wrong pin, Try again")

