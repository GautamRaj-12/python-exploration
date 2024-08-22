# Approach: Initialize a boolean variable to track if the number is prime.
# Iterate from 2 up to num-1 to check for any divisors. If a divisor is found, set the boolean to false and break the loop.
# Finally, check the boolean and the number to determine if it's prime.

# Taking input from the user
num = int(input("Enter a number for prime checking: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
