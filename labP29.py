#Q.29 TO print table of 10 until user's choice using list comprehension and lambda function
num=int(input("Enter a number upto which you want to enter multiple of 10:-"))
new_list=[10*i for i in range(num+1)]
print(new_list)
