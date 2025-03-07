#to check number is armstrong or not
num=int(input("Enter a number:-"))
n=num
digit=0
while(n>0):
    digit=digit+1
    n=n//10
n=num
curr=0
while(n>0):
    curr=curr+((n%10)**digit)
if(num==curr):
    print("true")
else:
    print("false")
