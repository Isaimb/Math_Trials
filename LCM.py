def find_lcm(a,b):
    if a > b:
        max = a
    else:
        max = b

    while True:
        if max % a == 0 and max % b == 0:
            lcm = max
            break
        max += 1
    return lcm

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = find_lcm(num1,num2)
print(result)