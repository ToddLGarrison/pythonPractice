# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# # print(programming_dictionary)

# programming_dictionary["Loop"] = "The action of doing something over and over again"

# # print(programming_dictionary)

# programming_dictionary["Bug"] = "A moth in the computer"

# # for key in programming_dictionary:
# #     print(key)


# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Stuttgart"],
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8,
        },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
        "total_visits": 3,
        },
}

print(travel_log["Germany"]["cities_visited"][2])