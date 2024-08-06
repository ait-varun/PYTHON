import sys

try:
   x = int(input("x: "))
   y = int(input("y: "))
except ValueError:
  print("Invalid input. Please enter a number.")
  sys.exit(1)



# result = x / y

# print(result)


# when x is 0 or y is 0


try:
    result = x / y
except ZeroDivisionError:
    print("You can't divide by zero!")
    sys.exit(1)

print(f"{x} / {y} i : {result}")