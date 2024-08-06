houses = {"Harry":"Gryffindor", "Ron":"Ravenclaw", "Hermione":"Slytherin", "Ginny":"Hufflepuff"}

print(houses["Harry"]) # prints Gryffindor

houses["Hermione"] ="Gryffindor" # changes the value of Hermione's house

print(houses["Hermione"]) # prints Gryffindor

del houses["Ron"] # removes Ron from the dictionary

print(houses) # prints {'Harry': 'Gryffindor', 'Hermione': 'Gryffindor'}