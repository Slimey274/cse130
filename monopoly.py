# 1. Name:
#      Briant Woolley
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This assignment is ment to get a Hotel on Pennsylvania Ave
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python? The syntax was fairly hard to understand at first but once I figured it out it was pretty easy
#      Was it an aspect of the problem you are to solve? no i had a fairly easy time once it understood it.
#      Was it the instructions or any part of the problem definition? The instructions were fairly hard to understand butwith som clarification it made it pretty easy
# 5. How long did it take for you to complete the assignment?
#      3 hours

def solution():
    # All properties owned
    all_properties = input("Do you own all the green properties? (y/n) ")
    if all_properties == "No":
        print("You must own all the properties")
        return
    # inputs for the options
    pacific_avenue = int(
        input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    north_carolina_avenue = int(input(
        "What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    pennsylvania_avenue = int(input(
        "What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    cash = int(input("How much cash do you have to spend?"))
    houses_available = int(input("How many houses are there to purchase? "))
    hotels_avalible = int(input("How many hotels are there to purchase? "))

    if cash <= 0:
        print("You do not have sufficient funds to purchase a hotel at this time.")
        return

    if houses_available <= 0:
        print("There are not enough houses available for purchase at this time.")
        return

    if hotels_avalible <= 0:
        print("There are not enough hotels available for purchase at this time.")
        return
    # Swapping Hotels
    swap_decision = input(
        "Do you want to swap a hotel? (y/n) ").strip().lower()
    if swap_decision == "y":
        swap_type = input(
            "Which property do you want to swap? (NC/PC) ").strip().upper()
        if swap_type == "NC":
            houses_available, cash(north_carolina_avenue,
                                   pennsylvania_avenue, houses_available, cash)
        elif swap_type == "PC":
            houses_available, cash(
                pacific_avenue, pennsylvania_avenue, houses_available, cash)
    # Continuation of house and hotel bulding
    # The cost of the houses
    house_cost = 200
    # The cost of hotels after 4 houses
    hotel_cost = 200

    if pennsylvania_avenue == 5:
        print("You cannot purchase a hotel if the property already has one.")
        return

    if (pacific_avenue < 4 or north_carolina_avenue < 4 or pennsylvania_avenue < 4):
        print(
            "You cannot purchase a hotel until all properties in the color group have four houses.")
        return

    property_houses = {
        "Pacific Avenue": pacific_avenue,
        "North Carolina Avenue": north_carolina_avenue,
        "Pennsylvania Avenue": pennsylvania_avenue
    }

    sorted_properties = sorted(property_houses.items(), key=lambda x: x[1])

    for property_name, houses in sorted_properties:
        while houses < 4 and houses_available > 0:
            houses += 1
            houses_available -= 1
            cash -= house_cost
            print(
                f"Placed 1 house on {property_name}. Cash left: ${cash}. Houses available: {houses_available}.")

    if (pacific_avenue == 4 and north_carolina_avenue == 4 and pennsylvania_avenue == 4):
        if cash >= hotel_cost:
            cash -= hotel_cost
        print(f"This will cost ${hotel_cost}.")
        print("Purchase 1 hotel for Pennsylvania Avenue and return 4 houses to the bank.")
        print(
            f"You have successfully built a hotel on Pennsylvania Avenue. Cash left: ${cash}.")
        return


solution()
