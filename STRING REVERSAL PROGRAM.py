# print("----swapping a number using a temp variable----")
# a = int(input("Enter the first number :: "))
# b = int(input("Enter the second number :: "))
# print("The value of a is :: ",a)
# print("The value of b is :: ",b)
# temp = a
# a = b
# b = temp
# print("The new value of a after swapping is :: ",a)
# print("The new value of b after swapping is :: ",b)

# print("----swapping a number using arithmetic operations----")
# a = int(input("Enter the value of a :: "))
# b = int(input("Enter the value of b :: "))
# print("The value of a is :: ",a)
# print("The value of b is :: ",b)
# a = a + b
# b = a - b
# a = a - b
# print("The new value of a after swapping is :: ",a)
# print("The new value of b after swapping is :: ",b)

# print("----swapping a number using arithmetic operations----")
# a = int(input("Enter the value of a :: "))
# b = int(input("Enter the value of b :: "))
# print("The value of a is :: ",a)
# print("The value of b is :: ",b)
# a = a * b
# b = a // b
# a = a // b
# print("The new value of a after swapping is :: ",a)
# print("The new value of b after swapping is :: ",b)

# print("----swapping a number using coma operator----")
# a = int(input("Enter the value of a :: "))
# b = int(input("Enter the value of b :: "))
# print("The value of a is :: ", a)
# print("The value of b is :: ", b)
# a, b = b, a #python special
# print("The new value of a after swapping is :: ", a)
# print("The new value of b after swapping is :: ", b)


print("-----swapping a string-----")
a = str(input("Enter a string :: "))
for i in range(len(a)-1, -1, -1):
    print(end=a[i])
for i in range(0, len(a)):
    print(end=a[(len(a)-1)-i])
a = a[::-1]
print(a)
s = "".join(reversed(a))
print(s)
