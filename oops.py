class Point():
  def __init__(self, input1, input2):
    self.x = input1
    self.y = input2

p = Point(1, 2)
print(p.x)
print(p.y)






class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passengers(self, name):
    if not self.open_seat():
      return False
    self.passengers.append(name)
    return True

  def open_seat(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["John", "Mary", "Peter", "Anna"]
for person in people:
  if flight.add_passengers(person):
      print(f"{person} is added to the flight")
  else:
      print(f"No Seats Available for {person}")

print(flight.passengers)

# prints
# John is added to the flight
# Mary is added to the flight
# Peter is added to the flight
# No Seats Available for Anna
# ['John', 'Mary', 'Peter']