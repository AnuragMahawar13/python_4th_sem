#to find largest and smallest number in a list
list=[35,36,26,9,48]
largest=list[0]
smallest=list[0]
for i in list:
    largest=max(largest,i)
    smallest=min(smallest,i)
print("largest number is:-",largest)
print("smallest number is :-",smallest)