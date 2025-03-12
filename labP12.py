#Q.12 to print fibonaaci series
num=int(input("Enter term:-"))
prev1=1
prev2=0
i=1
while(i<=num):
    if(i>2):
        curr=prev1+prev2
        prev2=prev1
        prev1=curr
        print(curr,"  ",end=" ")
    elif(i==1):
        print(prev2,"  ",end=" ")
    elif(i==2):
        print(prev1,"  ",end=" ")  
    i=i+1
