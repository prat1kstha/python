# import csv

# with open("Panda/WeatherData/002 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
    
#     temperature = []

#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])

# print(temperature)

import pandas

# read data from csv
data = pandas.read_csv("Panda/WeatherData/002 weather-data.csv")
# print(data["temp"])

# convert data to dictionary
data_dict = data.to_dict()
# print(data_dict)

# covert column to list
temp_list = data["temp"].to_list()

# aggregate functions
print(data["temp"].mean())
print(data["temp"].max())

# get data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print((monday_temp * 9/5) + 32)


# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("Panda/WeatherData/new_data.csv")
