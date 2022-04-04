# Create a loop function to get: "1 1 2 3 5 8 13 21 ...n". This on loops till the user number (n) is reached,
# if it matches it will print the number at the end but if the number surpasses the user number it won't print it.

a=0
b=1
n=int(input("Please enter a number, it has to be greater than 1: "))

while b<=n:
    print(b, end=" ")
    a,b=b,a+b
    
print("\n")

#Got it.
