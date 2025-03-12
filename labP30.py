#Q.30 To check whether a list is sorted or not.
def is_sort(list_1):
    return all(list_1[i-1]<list_1[i] for i in range(1,len(list_1)-1))
list_1=[1,2,3,4,5,6,7,8,9]
print(is_sort(list_1))