#Q.38 program to remove a empty tuple from a list of a tuple
l_of_tuple=[(1,2,3),(),(4,5,6),(),(7,8,9)]
updated_tuple=[x for x in l_of_tuple if x]
print(updated_tuple)