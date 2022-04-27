""" 
with open("weather_data.csv") as data:
    weather_data = data.readlines()

print(weather_data)

import csv

with open("weather_data.csv") as data:
    weather_data = csv.reader(data)
    temperatures = []
    for row in weather_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
 """


def celsius_to_farenheit(temp):
    return 9.0 / 5.0 * temp + 32


import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data["temp"])

""" 
data_to_dict = data.to_dict()
print(data_to_dict)

temp_list = data["temp"].to_list()

print(data["temp"].max()) 


# Get data in column
# print(data.condition)

# Get data in row
max_temp = data.temp.max()
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(celsius_to_farenheit(monday.temp))
 """

# Create dataframe from scratch
data_dict = {"CA": ["Kurt", "Bosse", "Lennart"], "Assessments": [12, 44, 3]}

dataframe = pd.DataFrame(data_dict)
dataframe.to_csv("CA.csv")
