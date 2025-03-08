#(c)printing factorial of a number using recursion
def fact(num):
    if(num==1):
        return 1
    
    return fact(num-1)*num

num=int(input("Enter a number:-"))
print(fact(num))