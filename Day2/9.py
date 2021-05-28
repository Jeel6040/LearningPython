#this is a comment

#creating an empty list
list = []

#number of elements as input
n= int(input("Enter Number of elements : "))

#iterating till the range
for i in range(0, n):
    ele = input("enter Value : ")

    list.append(ele)
print(list)