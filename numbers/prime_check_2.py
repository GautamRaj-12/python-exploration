# Approach: Start checking divisibility from 2 up to the number itself (excluding the number).
# If any number divides the input number, it's not prime. If no number divides it by the end,
# then it's a prime number. Additionally, handle the case where the input number is 1 or less.

# Taking input from the user
num = int(input("Enter a number for prime checking: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
        # Exit the loop and end the program early since we've found a divisor
        break
else:
    if num > 1:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
