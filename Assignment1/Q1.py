n = int(input("How many number you want to enter :"))
arr = []
for i in range(0,n):
    arr.append(int(input("Enter number :")))
sum = 0
for i in arr:
    sum += i
print("Sum = ",sum)
    