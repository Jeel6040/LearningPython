n1 = int(input("Enter value of n1: "))
n2 = int(input("Enter value of n2: "))
n3 = int(input("Enter value of n3: "))

if n1<n2 and n1<n3:
    print("n1 is smallest")
elif n2<n1 and n2<n3:
    print("n2 is smallest")
else:
    print("n3 is smallest")
