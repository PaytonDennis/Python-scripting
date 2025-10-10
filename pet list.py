pets = ["cat", "dog", "frog"]


while True:
    new_pet = input("add a pet or stop to quit: ")
    if new_pet == "quit":
        break
    pets.append(new_pet)

for index, pet in enumerate(pets):
    print(index, pet)


name = "bob"
name2 = "bill"

age = 2

