#Q.18(b)printing octal number for decimal number
def dec_to_oct(decimal_number):
    if(decimal_number==0):
        return 
    
    return dec_to_oct(decimal_number//8)+str(decimal_number%8)

num=int(input("Enter a number:-"))
print(dec_to_oct(num))