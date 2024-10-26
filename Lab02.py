# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      My program is ment to athentcate the user
# 4. What was the hardest part? Be as specific as possible.
#      I feel that I mostly struggled with idetifying the right sintax to use for the program.
#      The hardest part for me was getting the program to work correctly for me.
#      There was a bug that I had a hard time finding but once i noticed it it became super easy to fix the issue
#      I feel like the instructions for the program are a little to difficult to understand.
# 5. How long did it take for you to complete the assignment?
#      3 hours
import json


def authentification():
    input_username = input('Username: ')
    input_password = input('Password: ')
    try:
        file = open('Lab02.json', 'r')
        users = json.load(file)

        usernames = users['username']
        passwords = users['password']
        file.close()
    except:
        usernames = []
        passwords = []

    if input_username in usernames:
        username_index = usernames.index(input_username)
        if passwords[username_index] in input_password:
            print('You are authenticated!')
            return True

    print('You are not authorized to use the system.')
    return False


if __name__ == '__main__':
    authentification()
