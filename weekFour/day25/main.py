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

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(len(temp_list))

print(sum(temp_list))