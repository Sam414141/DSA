n = int(input("How many number you want to enter :"))
arr = []
print(f"Enter {n} Number :")
for i in range(0,n):
    arr.append(int(input(":")))
    
even_count = 0
odd_count = 0
for i in arr:
    if i % 2==0:
        even_count += 1
        print(f"{i} is even")
    else:
        odd_count += 1
        print(f"{i} is odd")

print(f"Total number of even values : {even_count}")
print(f"Total number of odd values : {odd_count}")