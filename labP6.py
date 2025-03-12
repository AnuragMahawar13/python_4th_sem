#Q.6 To check prime or not
num=int(input("Enter any number to check prime or not:-"))
if(num<2):
    print("Invalid number")
i=2
while(i*i<=num):
    if(num%i==0):
        print("Not a prime number")
        break
    else:
        i=i+1
if(i*i>num):
    print("Prime Number")