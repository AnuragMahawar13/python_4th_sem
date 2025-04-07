#Q.35 program to reverse a list at specific position
list_1=["1","2","3","4","5","6","7","8","9","10"]
start=2
end=7
list_1[start:end+1]=list_1[start:end+1][::-1]
print(list_1)