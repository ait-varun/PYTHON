people = [{"name": "Harry", "house": "Gryffindor"},
          {"name": "Ron", "house": "Gryffindor"},
          {"name": "Hermione", "house": "Gryffindor"}]

def f(person):
  return person["name"]

people.sort(key=f)

print(people)

# [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]


# SHORT VERSION

people.sort(key=lambda person: person["name"])
print(people)
# [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]