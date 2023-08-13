# sqlalchemy-challenge

# Climate Analysis and Flask API

## Introduction

Congratulations on planning your holiday vacation in Honolulu, Hawaii! As part of your trip planning, you'll be conducting a climate analysis using Python, SQLAlchemy, Pandas, and Matplotlib. Additionally, you'll create a Flask API to provide access to the analysis results. This README will guide you through the necessary steps.

## Part 1: Analyze and Explore the Climate Data

### Setup

1. Use the SQLAlchemy `create_engine()` function to connect to your SQLite database.
2. Use `automap_base()` to reflect the tables into classes: `station` and `measurement`.
3. Establish a SQLAlchemy session to interact with the database.

**Note**: Always remember to close your session at the end of your notebook.

### Precipitation Analysis

1. Find the most recent date in the dataset.
2. Retrieve the previous 12 months of precipitation data based on the most recent date.
3. Load the query results into a Pandas DataFrame, specifying column names.
4. Sort the DataFrame by date and plot the results as a precipitation chart.
5. Use Pandas to print summary statistics for the precipitation data.

### Station Analysis

1. Calculate the total number of stations in the dataset.
2. Find the most active stations (highest number of observations) by listing stations and observation counts in descending order.
3. Calculate the lowest, highest, and average temperatures for the most active station.
4. Query the previous 12 months of temperature observations (TOBS) for the most active station.
5. Plot the temperature observations as a histogram with 12 bins.

## Part 2: Design Your Climate App

### Flask API Routes

- `/`: Start at the homepage. List all available routes.
- `/api/v1.0/precipitation`: Convert the last 12 months of precipitation data to a dictionary and return it as JSON.
- `/api/v1.0/stations`: Return a JSON list of all stations from the dataset.
- `/api/v1.0/tobs`: Query temperature observations for the most active station in the previous year and return as JSON.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return JSON lists of minimum, average, and maximum temperatures for a specified date range.

### Hints

- Join the `station` and `measurement` tables for some queries.
- Utilize Flask's `jsonify` function to convert API data into valid JSON responses.

## Conclusion

By following the steps outlined in this README, you'll conduct a comprehensive climate analysis of Honolulu, Hawaii, and create a Flask API to share your findings. Enjoy your trip planning and exploration!


### References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.
