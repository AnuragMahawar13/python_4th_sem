#Q.39 Program to compute element wise sum of a given types
og_list=[[1,2,3,4],
         [3,2,5,1],
         [4,9,3,6]]

new_list=[0,0,0,0]
for i in range(len(og_list[0])):
    sum=0
    for j in range(len(og_list)):
        sum=sum+og_list[j][i]
    new_list[i]=sum
print(new_list)
