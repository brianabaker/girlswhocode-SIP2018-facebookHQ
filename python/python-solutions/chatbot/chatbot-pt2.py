# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions.
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")

# Choose a response based on the user's input.
def process_input(answer):
  valid_greetings = ["hi", "hello", "hey"]
  valid_goodbye = ["bye", "ciao", "get out of here"]
  if is_valid_input(answer, valid_greetings):
    say_greeting()
  elif is_valid_input(answer, valid_goodbye):
    say_goodbye()
  else:
    say_default()

def is_valid_input(answer, list_to_check):
  lowercase = answer.lower()
  for item in list_to_check:
    if lowercase == item:
      return True
  return False

# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

def say_goodbye():
  print("BYEEEEE")

# Display a default message to the user.
def say_default():
  print("That's cool!")


# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
