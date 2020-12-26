def factorial(n):

    print("Entering factorial with n", n)
    if (n == 1):
        return(1)

    return(n * factorial(n-1))



n_str = input("please enter a postive number: ")
n = int(n_str)
print("Factorial of", n, "is", factorial(n))
