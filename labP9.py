#Q.9 To find sum of digits of a number
num=int(input("Enter a number:-"))
res=0
while(num>0):
    res=res+(num % 10)
    num=num//10
print("Sum of digits of that number is:-",res)