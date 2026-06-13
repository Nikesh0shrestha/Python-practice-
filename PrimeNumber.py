# programt to find the given  number is prime or not 

num = int(input("Enter the number:"))

if num == 1:
    print("The given number is not a primr number.")

if num > 1:
    for i in range (2,num):
        if num % i == 0:
            print("The given number is not a prime number.")
            break
    else:
        print("The given number is a prime number.")