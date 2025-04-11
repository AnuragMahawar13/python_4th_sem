#Q49.Python program to compute squares of first n Fibonacci numbers using map() function and generate a list of numbers:

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def square(x):
    return x * x

n = int(input("Enter how many Fibonacci numbers you want: "))
fib_numbers = fibonacci(n)
squares = list(map(square, fib_numbers))

print("Fibonacci numbers:", fib_numbers)
print("Squares:", squares)