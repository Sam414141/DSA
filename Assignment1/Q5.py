n = int(input("How many number you want to enter :"))
arr = []
print(f"Enter {n} Number :")
for i in range(0,n):
    arr.append(int(input(":")))

print(arr[::-1])