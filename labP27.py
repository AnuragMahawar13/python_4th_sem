#Q27. To find all the member of a list that are divisible by a particular element 
list_1=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter a number:-"))
for i in list_1:
    if(i%num==0):
        print(i)
