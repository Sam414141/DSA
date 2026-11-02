# num = int(input("Enter a number :"))
# sum = 0
# while num > 0:
#     sum += num % 10
#     num = num // 10
# print(sum)

def count():
    for i in range(1,5):
        yield i

for i in count():
    print(i)