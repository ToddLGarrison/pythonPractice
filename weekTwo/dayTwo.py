programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary)

programming_dictionary["Loop"] = "The action of doing something over and over again"

# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in the computer"

# for key in programming_dictionary:
#     print(key)


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])