import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels],
}

dataframe = pd.DataFrame(squirrel_dict)
dataframe.to_csv("squirrel_count")

# print(data.astype("Primary Fur Color").values)
