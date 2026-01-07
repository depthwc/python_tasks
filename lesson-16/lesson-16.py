import pandas as pd, sqlite3

# Part 1: Reading Files
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("Customers:\n", customers_df.head(10))

iris_df = pd.read_json("iris.json")
print("\nIris Shape:", iris_df.shape, "\nColumns:", iris_df.columns.tolist())

titanic_df = pd.read_excel("titanic.xlsx")
print("\nTitanic:\n", titanic_df.head())

flights_df = pd.read_parquet("flights.parquet")
print("\nFlights Info:"); flights_df.info()

movie_df = pd.read_csv("movie.csv")
print("\nMovie Sample:\n", movie_df.sample(10))

# Part 2: Exploring DataFrames
iris_df.columns = iris_df.columns.str.lower()
print("\nIris Sepal Columns:\n", iris_df[["sepal_length", "sepal_width"]])

print("\nTitanic Age > 30:\n", titanic_df[titanic_df["Age"] > 30])
print("\nGender Counts:\n", titanic_df["Sex"].value_counts())

print("\nFlights Columns:\n", flights_df[["origin", "dest", "carrier"]])
print("Unique Destinations:", flights_df["dest"].nunique())

long_movies = movie_df[movie_df["duration"] > 120]
print("\nLong Movies Sorted:\n", long_movies.sort_values("director_facebook_likes", ascending=False))

# Part 3: Challenges
print("\nIris Stats:\nMean:\n", iris_df.mean(numeric_only=True),
      "\nMedian:\n", iris_df.median(numeric_only=True),
      "\nStd:\n", iris_df.std(numeric_only=True))

print("\nTitanic Age Stats:\nMin:", titanic_df["Age"].min(), 
      "Max:", titanic_df["Age"].max(), "Sum:", titanic_df["Age"].sum())

director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum()
print("\nTop Director:", director_likes.idxmax(), "with", director_likes.max(), "likes")

print("\n5 Longest Movies:\n", movie_df.sort_values("duration", ascending=False).head(5)[["movie_title", "duration", "director_name"]])

print("\nMissing Flights Data:\n", flights_df.isnull().sum())
if "air_time" in flights_df.columns:
    flights_df["air_time"].fillna(flights_df["air_time"].mean(), inplace=True)
