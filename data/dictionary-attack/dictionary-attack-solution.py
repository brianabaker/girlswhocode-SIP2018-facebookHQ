def main():
    f = open("dictionary.txt","r")
    in_dictionary = False
    while not in_dictionary:
        print("Can your password survive a dictionary attack?")
        password_list = []
        words_list = []
        for line in f:
            words_list.append(line.strip())
        in_dictionary = check_password(words_list)

def check_password(words_list):
    test_password = input("Type in a trial password: ")

    if test_password in words_list:
        print('first if')
        print("Password match found: ", test_password)
        return True
    elif multiword_check(words_list, test_password):
        print('second if')
        print("Password match found: ", test_password)
        return True
    else:
        print("Password not found... in this dictionary attack")
        return True

def multiword_check(words_list, password):
    answer = []
    placeholder = ""
    for char in password:
        placeholder += char
        if placeholder in words_list:
            print('placeholder', placeholder)
            if len(placeholder) > 3:
                answer.append(placeholder)
                placeholder = ""
                print('if answer', answer)
    full_word = "".join(answer)
    if len(full_word) == len(password):
        return True
    else:
        return False

# For extension project only:
# Check and convert common letter-to-number substitutions

# def find_variations(password):
#     password = password.replace("1", "l")
#     password = password.replace("!", "i")
#     password = password.replace("2", "z")
#     password = password.replace("3", "e")
#     password = password.replace("@", "a")
#     password = password.replace("4", "a")
#     password = password.replace("$", "s")
#     password = password.replace("5", "s")
#     password = password.replace("6", "g")
#     password = password.replace("7", "t")
#     password = password.replace("8", "b")
#     password = password.replace("9", "g")
#     password = password.replace("0", "o")
#     return password

if __name__ == '__main__':
    main()
