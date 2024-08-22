# Approach: A prime number has two factors, so find the factors, count them,
# if the count after the whole operation is 2, then it's prime, otherwise not prime.

# Taking input from the user
num = int(input("Enter a number for prime checking: "))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
