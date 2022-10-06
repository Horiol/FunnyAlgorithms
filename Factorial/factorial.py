def factorial(n):
    return 1 if n==0 else n * factorial(n-1)

number = int(input("Enter a number: "))
print(factorial(number))
