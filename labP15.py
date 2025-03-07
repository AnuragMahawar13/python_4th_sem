#to print all palindromes for a range between 500-100
for i in range(500,1001):
    n=i
    rev=0
    while(i>0):
        rev=(rev*10)+(i%10)
        i=i//10
    if(rev==n):
        print(n)
        