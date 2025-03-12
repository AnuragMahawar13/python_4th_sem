#Q.18(d)printing n terms of a fibonacci
def fibo(n):
    if(n<1):
        print("Enter a positive term")
        return
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

term=int(input("Enter a number:-"))
print("Fibonacci series is:-")
for i in range(1,term+1):
    print(fibo(i),end=" ")
   