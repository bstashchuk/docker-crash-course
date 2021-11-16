n = int(input("Please enter any positive number: "))

if n < 0:
    print("Error: Number must be positive")
else:
    sum = 0
    i = n
    while i > 0:
        sum += i
        i -= 1
    print("Sum of all positive numbers till", n, "is", sum)
