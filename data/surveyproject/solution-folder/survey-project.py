
import json

survey = [
    "What is your name?", #0
    "How old are you?" #1
]
keys = ["name", "age"]

dictionaries = []

done = "YES"
while done == "YES":
    answers = {}
    for x in range(len(survey)):
        response = input(survey[x]+":  ")
        answers[keys[x]] = response

    dictionaries.append(answers)
    done = input("Would you like to continue collecting data? YES or NO?").upper()

file = open("user-responses.json", "r")
olddata = json.load(file)

dictionaries.extend(olddata)
print(dictionaries)
file.close()

file = open("user-responses.json", "w")
file.write("[\n")
counter = 0
for obj in dictionaries:
    if counter < (len(dictionaries)-1):
        json.dump(obj, file)
        file.write(",\n")
    else:
        json.dump(obj, file)
        file.write("\n")
    counter += 1

file.write("]")
file.close()
