#Loop Defination
#
#
# 1- 1000
# print(1)
# print(2)
# print(3)
# print(4)

# for i in range(1,11):
#     print("Gazala")


for i in range(1,11):
    print("3 * ", i , " = " , 3*i)


#HW- 2, make the multiplication table dynamic by user Input
num = int(input("Enter a number for multiplication table: "))
limit = int(input("Enter the limit (e.g. 10, 20): "))
print(f"\nMultiplication Table of {num} up to {limit}\n")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")

