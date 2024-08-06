import sys


x = int(input("x: "))
y = int(input("y: "))

# result = x / y

# print(result)


# when x is 0 or y is 0
# try:
#     result = x / y
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print(result)


try:
    result = x / y
except ZeroDivisionError:
    print("You can't divide by zero!")
    sys.exit(1)

print(f"{x} divided by {y} is {result}")