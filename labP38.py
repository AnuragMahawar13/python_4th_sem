#Q.38 program to convert a tuple of string into tuple of int
l_of_tuple=(['111','11'],['222','22'])
new_tuple=([0,0],[0,0])
for i in range(len(l_of_tuple)):
    for j in range(len(l_of_tuple[0])):
        new_tuple[i][j]=int(l_of_tuple[i][j])
print(new_tuple)
        