
#Morning Review Questions!
animals = ["dog", "cat", "mouse"]

#What is animals[2]?
#What is anmials[len(animals) - 1]?

#What is the resulting new list?
animals.append("gorilla")
animals.insert("fish",1)
animals.insert("bear",2)
animals[0] = "goat"


#What does this print using the new list above?
for animal in animals:
    print(animal)

#What does this print?
for index in range(0,len(animals)):
    print(index)

#What does this print?
for index in range(0, len(animals)):
    print(animals[index])

# CHALLENGE QUESTION - Write a function that takes in a name, and prints out a good morning greeting with given name

# CHALLENGE QUESTION
# Write a function that takes a list of numbers and prints out all the elements of the list that are less than 5.
    # BONUS: Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
