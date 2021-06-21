import pandas as pd
import json
import datetime

# Getting each game date with format:

def date(string):
    return string[17:19]+"/"+string[15:17]+"/"+string[11:15]


# Getting each game month in an integer:

def get_month(string):
    return int(string[15:17])


# Getting each game year in an integer:

def get_year(string):
    return int(string[11:15])


# Using datetime library to convert full name month to 

def convert_month(string):

    datetime_object = datetime.datetime.strptime(string, "%B")

    month_number = datetime_object.month

    return month_number


# Seasons starts after september and ends before august:

def convert_season(row):
    if row["month"] >= 8:
        return int(row["season"][:4])
    else:
        return int(row["season"][-4:])


# Importing kaggle dataset:

data = pd.read_csv("../data/games.csv", encoding="ISO-8859-1")


# This dataset is extremely clean but we will have to manipulate it in order to get some new columns to proceed with our analysis:
# We generate a few new columns:

data["DATE"] = data["GAME_ID"].apply(date)
data["MONTH"] = data["GAME_ID"].apply(get_month)
data["YEAR"] = data["GAME_ID"].apply(get_year)


# Let's import the json file of the scrapped dataset:

f = open("../data/pom_database.json",)
pom_data = json.load(f)
f.close()

pom = pd.DataFrame(pom_data)


# Let's manipulate the data and generate some new useful columns with this dataset too:

pom["month"] = pom["pom_month"].apply(convert_month)
pom["year"] = pom.apply(convert_season, axis=1)


# Web scrapping dataset goes since 1979 and kaggle dataset only since 1996.
# We will keep information from the years since 1996:

pom = pom[pom["year"] >= 1996]


# Finally we, cross information from both datasets and keep only games from each player of the month:

for i, pom_player in pom.iterrows():
    print(i)
    
    data.loc[
        (data.PLAYER == pom_player.player) &
        (data.MONTH == pom_player.month) &
        (data.YEAR == pom_player.year),
        "POM"
    ] = True


# Now let's get a shorter dataframe from each "Player of the month" stats:

data_pom = data[data["POM"] == True]


# Finally, we will export this dataset as .csv:

data_pom.to_csv("../data/data_pom.csv", index = False)
