import pandas as pd

data = pd.read_csv("Panda/SquirrelCensus/004201~1.CSV")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len([data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

pd.DataFrame(data_dict).to_csv("Panda/SquirrelCensus/squirrel_count.csv")


# print(fur_colors.groupby(fur_colors).count())
# agg = data.groupby(data["Primary Fur Color"]).count(data["Unique Squirrel ID"])

# print(agg)