# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input number
num = int(input("Enter a number: "))

# Calculate factorial and print the result
print(f"The factorial of {num} is {factorial(num)}")
