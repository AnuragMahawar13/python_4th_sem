#to print the following pattern
# *
# **
# ***
# ****
for i in range(1,5):
    print('*'*i)
print()
#for reverse of it
for j in range(4,0,-1):
    print('*'*j)
print()
#----------------------------------------------
#   *
#  ***
# *****
for i in range(1,6,2):
    print(' ','*'*i)
print()
#---------------------------------------------
# 1
# 22
# 333
# 4444
for i in range(1,5):
    n=str(i)
    print(n*i)
print()
#----------------------------------------------
#pascal's triangle
for row in range(1,9):
    ans=1
    if(i==1):
        print(1)
    else:
        print(1,end=" ")
    for col in range(1,row):
        
        ans=ans*(row-col)
        ans=ans//col
        print(ans,end=" ")
    print()
print()
#----------------------------------------------------
#floyd's triangle
i=1
for col in range(1,11):
    for row in range(0,col):
        print(i,end=' ')
        i=i+1
    print()

