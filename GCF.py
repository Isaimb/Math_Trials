def gcf(a,b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

gcd = gcf(num1,num2)
print(gcd)