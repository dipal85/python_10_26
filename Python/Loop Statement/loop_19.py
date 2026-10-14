#19. Check whether a number is prime.

n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: prime = False; break
    print("Prime" if prime else "Not Prime")