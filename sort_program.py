# 1. Name:
#      Briant Woolley
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      the hardest thing for me in this program was gettin it to work in the first palce.
#       I also couldn't really find lots of spots to put asserts. It was also hard to focus this week for me.
# 5. How long did it take for you to complete the assignment?
#      it took me 3hrs
# Import unsorted json files
import json


def Sort_Program():
    """Reads the JSON file, sorts the data using Bubble Sort, and verifies it."""

    def bubble_sort(data):
        """Sorts the data using Bubble Sort."""
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if data[j]['name'] > data[j + 1]['name']:
                    # Swap the elements if they are in the wrong order
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break
        return data

    try:
        # Ask user for the filename
        filename = input("Please enter the JSON filename: ")

        # Open the file and load the data
        with open(filename, "r") as file:
            data = json.load(file)

        # Sort the data using Bubble Sort
        sorted_data = bubble_sort(data)

        # Print the sorted data for debugging
        print("Sorted data:")
        print(sorted_data)

        # Check if the data is sorted correctly
        for i in range(1, len(sorted_data)):
            if sorted_data[i - 1]['name'] > sorted_data[i]['name']:
                print(
                    f"Assertion failed: {sorted_data[i - 1]['name']} > {sorted_data[i]['name']}")
                raise AssertionError("Data is not sorted correctly.")

        # If everything is fine, print a success message
        print("Data has been sorted successfully!")
        print(sorted_data)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    Sort_Program()
