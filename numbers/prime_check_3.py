# Approach: First, check if the number is less than or equal to 1, as such numbers are not prime.
# Then, check divisibility starting from 2 up to num-1. If a divisor is found, it's not prime.
# If no divisors are found, the number is prime.

# Taking input from the user
num = int(input("Enter a number for prime checking: "))

if num <= 1:
    print(f"{num} is not a prime number")
    #break - can't do break outside a loop
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            # Exit early since a divisor was found
            break
    else:
        print(f"{num} is a prime number")
