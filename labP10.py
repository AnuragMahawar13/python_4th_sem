#to find reverse of number
num=int(input("Enter a number:-"))
res=0
while(num>0):
    res=(res*10)+(num % 10)
    num=num//10
print("reverse number is:-",res)
