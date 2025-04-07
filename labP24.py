#Q24. To add two matrix
matrix_1=([1,1,1],[1,1,1],[1,1,1])
matrix_2=([2,2,2],[2,2,2],[2,2,2])
result=([0,0,0],[0,0,0],[0,0,0])
row_1=len(matrix_1)
row_2=len(matrix_2)
col_1=len(matrix_1[0])
col_2=len(matrix_2[0])
if(row_1 != row_2 or col_1!=col_2):
    print("these matrices can not be added")
else:
    for i in range(0,row_1):
        for j in range(0,col_1):
            result[i][j]=matrix_1[i][j]+matrix_2[i][j]
    print(result)

