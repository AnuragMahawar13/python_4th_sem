#to create a list by concatenating a given list with a range from 1 to n
list_1=['p','q']
num=int(input("Enter a number"))
output_list=[]

for i in list_1:
    for j in range(1,num+1):
        output_list.append(i+str(j))

print(output_list)

