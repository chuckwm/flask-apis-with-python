# should_continue = True
# if should_continue: # == True: This can be left out it is assumed
#     print("Hello")
#
# known_people = ["John", "Anna", "Mary"]

# person = input("Enter the person you know: ")
# if person in known_people:
#     print("You know this {}".format(person))
# #    print("You know this person!")
# else:
#     print("You don't know this {}".format(person))
#    print("You don't know this person!")
#if person not in known_people:
#    print("You don't know this person")
def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    # Return that list
    string_names = input("Enter list of people you know, separated by commas: ")
    list_names = string_names.split(",")
    list_names_without_spaces = [ name.strip().lower() for name in list_names ]
    # list_names_without_spaces = []
    # for name in list_names:
    #     list_names_without_spaces.append(name.strip())
    return  list_names_without_spaces

#print(who_do_you_know())

def ask_user():
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person
    list_names = who_do_you_know()
    person = input("Enter the name of a person you know:  ")
    if person in list_names:
        print("You know this {}".format(person))
    #    print("You know this person!")
    else:
        print("You don't know this {}".format(person))
ask_user()
