# Approach: First, check if the number is less than or equal to 1, as such numbers are not prime.
# Then, use a boolean variable to track if the number is prime.
# Iterate from 2 up to num-1 to check for any divisors. If a divisor is found, set the boolean to False and break the loop.
# Finally, check the boolean to determine if the number is prime.

# Taking input from the user
num = int(input("Enter a number for prime checking: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
