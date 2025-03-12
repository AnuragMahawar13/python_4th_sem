#Q.11 to find a number is palindrone or not
num=int(input("Enter a number:-"))
n=num
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
if(rev==num):
    print("true")
else:
    print("false")    