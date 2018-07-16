
# Creates the dictionary to store responses.
# PART TWO -- MOVE THE ANSWERS DICTIONARY INSIDE THE LOOP BECAUSE YOU WANT TO MAKE A NEW ONE EACH TIME.
# answers = {}

# PART 3 include json library
import json

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

# Print the context of the dictionary.
# print(answers)

# END OF STARTER CODE

# PART ONE
# Let's start out with just two questions
survey = [
    "What is your name?",
    "How old are you?"
]

# We're going to iterate over both of these lists, and combine them with the input response from the user into a dictionary
keys = ["name", "age"]

# show them how to iterate over two loops like in this:
for x in range(len(survey)):
    print(survey[x])
    print(keys[x])
    print('----------')
# as long as our two lists are the same length, this won't error. And we're making both lists, so we're good!

# so now... let's ask for the user's input after each question, and then assign that input to a dictionary, with each input correspoding to the appropriate key

for x in range(len(survey)):
    response = input(survey[x]+":  ")
    print(response)
    # show them this works
#     # ASK: Now how do I assign this response to the dictionary....

    answers[keys[x]] = response

# print(answers)

# END OF PART ONE

# PART TWO -- gather responses from multiple surverys as a list of dictionaries

list_of_answers= []
done = "NO"
while done == "NO":
    # we need to make a new answers dictionary for each user, so we need to put this inside the loop so it makes a new one each time
    answers = {}
    print("New entry! Please answer questions below!")

    # this for loop still works, but after they're done answering questions we need to put it somewhere
    for x in range(len(survey)):
        response = input(survey[x]+":  ")
        answers[keys[x]] = response

    # how do we add things to a list?
    list_of_answers.append(answers)
    # Now we need a way to exit the loop, let's ask the user if they're done collecting information
    # input("Are you done collecting information? Type YES or NO.      ").upper()
    # the .upper() is a safe guard
    # so to exit the loop we need to change the value of done right?

    done = input("Are you done collecting information? Type YES or NO.   ").upper()


# print(list_of_answers)
# does this print need to be in the function?


# END OF PART TWO

# PART THREE - our data disappears when it exits the program! we need to have it in persistent storage!
# NEED TO GO TO SLIDES FOR THIS PART
# The standard is JSON!

# FIRST LET'S WRITE TO THIS FILE
# open it up and write your info in JSON
# this opens it as read only
file = open("all-the-answers.json", "r")
# # loads the file into this variable
olddata = json.load(file)
# print(olddata)
# here old data is just like in the json, so it's an array of objects
# how do we get the new answers and the old answers together? remember both arrays
list_of_answers.extend(olddata)
# now we've added the old data to the list_of_answers and saved it into the list_of_answers
print(list_of_answers)
file.close()

# \n makes a new line
file = open("all-the-answers.json", "w")
# # this is going to be a list of objects, so it needs to start with an opening square bracket, right?
file.write("[\n")
counter = 0

# cannot compare between 'int' and 'range'
for obj in list_of_answers:
    if counter < (len(list_of_answers)-1):
        json.dump(obj, file)
        file.write(',\n')
    else:
        print('in the else, counter:')
        print(counter)
        json.dump(obj, file)
        file.write('\n')
    counter += 1

file.write(']')
file.close()
