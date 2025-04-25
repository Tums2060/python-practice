#1. Sum all elements in a list

#At first i thought of a string, lets say Hello, Tumaini and it outputs "Hello Tumaini"
#But i didn't know if you mean digits and or string by "elements"

#So i did for both

#This one sums all elements in a list but for integers only
def sum_elements():
    elements = input("Enter elements you wish to add: ")
    #using list() to use lists
    #and map(int, ..) to convert inputted strings to integers
    #map() iterates throught the whole list
    inputted = list(map(int, elements))

    total = sum(inputted)
    print(total)


#This "adds" strings together
#my logic was since you are inputting strings you want to input together, i can just print your inout out back again
#cause writting them is just technically adding them
def sum_strings():
    strings = input("Enter elements you wish to add: ")
    print(strings)


def main():
    sum_elements()

    sum_strings()
#calling the functions
main()