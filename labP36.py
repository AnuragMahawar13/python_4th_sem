#Q.36 program to replace a value from a tuple in a list
list_of_tuple=[(10,20,30),(40,50,60),(70,80,90)]

for i in range(len(list_of_tuple)):
    temp_list=list(list_of_tuple[i])
    temp_list[-1]=100
    list_of_tuple[i]=tuple(temp_list)

print(list_of_tuple)
