#Q23. To transpose a matrix
matrix=([1,2,3],[4,5,6],[7,8,9])
row=len(matrix)
col=len(matrix[0])
for i in range(0,col):
    for j in range(i+1,col):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print(matrix)