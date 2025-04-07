#Q.43 Program to create a dictionary form a string to count no. of letter
string="i love python language"
dict_1={}
for i in string:
    if i in dict_1:
        dict_1[i]+=1
    else:
        dict_1[i]=1
print(dict_1)