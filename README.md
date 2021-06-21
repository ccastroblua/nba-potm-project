![portada](https://github.com/ccastroblua/nba-potm-project/blob/main/images/spacejam.jpg)

# NBA - Player of the month - Pipeline Project:

The goal of this project is to analize which are the stats that influence more in the decision of the "Player of the month" award in the National Basketball Association (NBA) and what are the minimum requirenments for a player to get that award.

This project has 3 stages well defined:
1. Web-scrapping
2. Data cleaning and manipulation
3. Analyzing data and obtaining insights


## Questions:

- Is there any correlation between some stats and "Player of the month" award?
- Is there any YoY diference between "Player of the month" performance?
- Is there any MoM diference between "Player of the month" performance?
- Which are the minimum stats requiered to be the "Player of the month" with 90% of precision?


## Files structure:

- "data" folder with:
    - JSON file from the web-scrapping (pom-database.JSON)
    - Final clean dataset to analyze (pom-database.csv)
- "notebooks" folder (With comments): 
    - Cleaning Jupyter Notebook file (cleaning.ipynb): Project cleaning stage.
    - Web-scrapping Jupyter Notebook file (scrapping.ipynb): Project web-scrapping stage.
- "src" folder with (For execute pourpose only):
    - Cleaning Jupyter Python file (cleaning.py): Project cleaning stage.
    - Web-scrapping Jupyter Python file (scrapping.py): Project web-scrapping stage.
- "image" folder with:
    - Coverpage image (spacejam.jpg)
- Analysis Jupyter Notebook file (analysis.ipynb): Project Analysis stage.

## Files needed to download for this project:

- NBA Dataset from kaggle (games.csv) <https://www.kaggle.com/kenhuang41/nba-basic-game-data-by-player?select=games.csv> 
    - You need to dowload it in the "data" folder of this project.

## Library used:

- Pandas - <https://pandas.pydata.org/>
- Seaborn - <https://seaborn.pydata.org/#>
- Matplotlib - <https://matplotlib.org/>
- Plotly - <https://plotly.com/>
- BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/>
- JSON - <https://docs.python.org/3/library/json.html>
- Datetime - <https://docs.python.org/3/library/datetime.html>
- Requests - <https://docs.python-requests.org/en/master/>