

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse number is:", reverse)

# This program takes a number from the user, extracts digits one by
# one using modulus operator %, and builds the reverse number using
# loop and arithmetic operations.