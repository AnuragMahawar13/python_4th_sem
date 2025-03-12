#Q.21 To remove duplicates from a list
old_list=[1,1,2,2,3,3,4,4,5,5]
new_list=[]
for i in old_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)