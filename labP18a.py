#program to print a decimal number into binary number using recursion

def dec_to_bi(decimal_number):
    if(decimal_number==0):
        return '0'
    elif(decimal_number==1):
        return '1'
    
    return dec_to_bi(decimal_number//2)+str(decimal_number%2)

num=int(input("Enter a number:-"))
print(dec_to_bi(num))