import pandas as pd, numpy as np, sqlite3

# Inner Join: Chinook
conn = sqlite3.connect("chinook.db")
cust = pd.read_sql("SELECT * FROM customers", conn)
inv = pd.read_sql("SELECT * FROM invoices", conn)
joined = pd.merge(cust, inv, on="CustomerId", how="inner")
invoice_count = joined.groupby("CustomerId").InvoiceId.count().reset_index(name="TotalInvoices")

# Outer Join: Movie Data
movie = pd.read_csv("movie.csv")
df1 = movie[["director_name", "color"]]
df2 = movie[["director_name", "num_critic_for_reviews"]]
left_join = pd.merge(df1, df2, on="director_name", how="left")
outer_join = pd.merge(df1, df2, on="director_name", how="outer")
left_rows, outer_rows = len(left_join), len(outer_join)

# Grouping: Titanic
titanic = pd.read_csv("titanic.csv")
grouped = titanic.groupby("Pclass").agg(Avg_Age=("Age", "mean"), Total_Fare=("Fare", "sum"), Count=("PassengerId", "count")).reset_index()

# Grouping: Movies
movie_grouped = movie.groupby(["color", "director_name"]).agg(Total_Critics=("num_critic_for_reviews", "sum"), Avg_Duration=("duration", "mean")).reset_index()

# Grouping: Flights
flights = pd.read_csv("flights.csv")
flight_grouped = flights.groupby(["Year", "Month"]).agg(
    Total_Flights=("FlightNum", "count"),
    Avg_ArrDelay=("ArrDelay", "mean"),
    Max_DepDelay=("DepDelay", "max")
).reset_index()

# Apply: Titanic Child/Adult
titanic["Age_Group"] = titanic["Age"].apply(lambda x: "Child" if pd.notna(x) and x < 18 else "Adult")

# Normalize Salaries
emp = pd.read_csv("employee.csv")
emp["Salary_Norm"] = emp.groupby("Department")["Salary"].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

# Movie Duration Classification
def classify(dur): return "Short" if dur < 60 else "Medium" if dur <= 120 else "Long"
movie["Length_Category"] = movie["duration"].apply(classify)

# Titanic Pipe
def titanic_pipeline(df):
    return (df[df["Survived"] == 1]
            .assign(Age=lambda d: d["Age"].fillna(d["Age"].mean()))
            .assign(Fare_Per_Age=lambda d: d["Fare"] / d["Age"]))
titanic_result = titanic.pipe(titanic_pipeline)

# Flights Pipe
def flights_pipeline(df):
    return (df[df["DepDelay"] > 30]
            .assign(Delay_Per_Hour=lambda d: d["DepDelay"] / d["AirTime"]))
flight_result = flights.pipe(flights_pipeline)
