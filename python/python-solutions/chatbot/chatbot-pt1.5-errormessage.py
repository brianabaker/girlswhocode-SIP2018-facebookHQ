# The chatbot introduces itself and gives the user instructions.
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")

 # gives NameError: name 'answer' is not defined
 # let's talk about scope!

def process_input(answer):
  if answer == "hi":
    say_greeting()
  else:
    say_default()

def say_greeting():
  print("Hey there!")

def say_default():
  print("That's cool!")

def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
