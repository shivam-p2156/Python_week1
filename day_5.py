# if - else statement 

a= int(input("Enter your age: "))

if (a>=18):
    print("you are adult")

else:
    print("you are minor")

#if - elif - else statement

if (a<0):
    print("number is negative")
elif (a==0):
    print("number is zero")
else:
    print("number is positive")



# nested if statment

if (a<0):
    print("number is negative")
elif (a>0):
    if (a<=10):
        print("number is less than 10")
    elif (a>=10 and a<=20):
        print("number is between 10 to 20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
    
