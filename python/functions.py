
# SCOPE
# One
# def can_you_see_me():
#     response = input("Say a thing: ")
#     print('INSIDE', response)
#
# can_you_see_me()
# print('OUTSIDE', response)

# Two - say hello global

# Three - say hello local

# Four - say hello params
def say_hello(name):
    print("Hi " + name)

def main():
    user = "Michelle"
    say_hello(user)

if __name__ == "__main__":
  main()

# Five - show versatility by doing it with input()
