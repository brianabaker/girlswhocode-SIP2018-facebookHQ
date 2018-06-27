
# FOR LOOP FOR ELEMENTS
# FOR LOOP FOR INDEX

animals = ["rabbit", "turkey", "panda"]

# for animal in animals:
#     print(animal)
#
# for index in range(len(animals)):
#     print(index)

# WHILE LOOPS
hungry = True #if you're going to change a variable in a loop-- you have to declare it outside
while hungry:
    response = input("Ugh I'm hungry. Did I remember to bring food? 'Yes' or 'No'")
    if response == "Yes":
        print("I'm so happy I brought food!")
        hungry = False
    elif response == "No":
        print("Oh no! I should have packed food.")
        hungry = False
    else:
        print("That's not an option!")

# ADD MORE HERE
