#write a function to check palindrome or not

# def palindrome(n):
#     rev=0
#     while(n>0):
#         rev=(rev*10)+(n%10)
#         n=n//10
#     if(rev==num):
#         print("number is palindrome")
#     else:
#         print("number is not palindrome") 
# num=int(input("Enter a number:-"))
# palindrome(num)

#-----------------------------------------------
#function to find sum of first n natural numbers

def natural(n):
    print((n*(n+1)//2))

num=int(input("Enter a number:-"))
natural(num)

