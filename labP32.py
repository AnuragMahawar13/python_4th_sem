#Q.32 program that takes a list of words and return the longest word with its length
list_1=["apple","banana","pineapple","watermelon","guava"]
max_letter=0
j=0
for i in range(1,len(list_1)):
    if(len(list_1[i])>len(list_1[i-1])):
        j=i
    
print(list_1[j],len(list_1[j]))