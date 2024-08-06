def announce(f):
  def wrapper():
    print("About to call the function")
    f()
    print("Done with the function")
  return wrapper

@announce
def hello():
  print("Hello")

hello()

# prints
# About to call the function
# Hello
# Done with the function