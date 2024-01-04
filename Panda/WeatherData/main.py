# import csv

# with open("Panda/WeatherData/002 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
    
#     temperature = []

#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])

# print(temperature)

import pandas

data = pandas.read_csv("Panda/WeatherData/002 weather-data.csv")
print(data["temp"])