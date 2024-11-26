# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# # print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] * (9/5) + 32
# print(monday_temp)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data["Primary Fur Color"] == "Gray")
red_squirrels_count = len(data["Primary Fur Color"] == "Cinnamon")
black_squirrels_count = data["Age"] == "Black"
print(black_squirrels_count)