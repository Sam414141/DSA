n = int(input("Enter the lenght of list :"))
arr = []
print(f"Enter {n} list elements :")
for i in range(0,n):
    arr.append(int(input(":")))
    
arr.sort()
print("Largest Number :",arr[len(arr)-1])
print("Second Largest Number :",arr[len(arr)-2])
print("Smallest Number :",arr[0])
print("Second samllest Number :",arr[1])

