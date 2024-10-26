# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      -It needs to search the program for languages-
# 4. Algorithmic Efficiency
#      -Identify the algorithmic efficiency and tell why it is as you say it is-
# 5. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 6. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json
import os

def Advanced_Search():
    #asking for user input for the file name and language
    file_name = input("What is the name of the file? ")
    language = input("What name are we looking for? ")

    if not os.path.exists(file_name):
        print("The specified file does not exist.")
        return []

    with open(file_name, 'r') as file:
        data = json.load(file)
        languages = data.get('array', [])
    
    if not languages:
        print("No languages were found in the file")
        return
    
    left, right = 0, len(languages) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if languages[mid] == language:
            print(f"{language} was found in the list.")
            return True
        elif languages[mid] < language:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{language} was not found in the list.")

if __name__ == "__main__":
    Advanced_Search()