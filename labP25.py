#Q25. To multiply to matrix
matrix_2=([1,1,1],[1,1,1])
matrix_1=([2,2],[2,2],[2,2])
col_1=len(matrix_1[0])
row_1=len(matrix_1)
row_2=len(matrix_2)
col_2=len(matrix_2[0])
result=([0,0,0],[0,0,0],[0,0,0])

if(col_1==row_2):
    for i in range(0,row_1):
        for j in range(0,col_2):
            sum=0
            for k in range(0,row_2):
                sum=sum+(matrix_1[i][k]*matrix_2[k][j])
            result[i][j]=sum
    for row in result:
        print(row)
else:
    print("Mutiply can not be done")
