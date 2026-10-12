n = int(input("How many number you want to enter :"))
arr = []
print(f"Enter {n} Number :")
for i in range(0,n):
    arr.append(int(input(":")))

num = int(input("Enter a Number to search :"))
if num not in arr:
    print("Entered Number does not exist in array !!")
else:
    print(num,"is present at position : ",arr.index(num)+1)
    
    
