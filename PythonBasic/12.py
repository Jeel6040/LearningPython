n1 = int(input("Enter value of n1: "))
n2 = int(input("Enter value of n2: "))
n3 = int(input("Enter value of n3: "))

if n1>n2:
    if n1>n3:
        print("n1 is largest")
    else:
        print("n3 is largest")
else:
    if n2>n3:
        print("n2 is largest")
    else:
        print("n3 is largest")
