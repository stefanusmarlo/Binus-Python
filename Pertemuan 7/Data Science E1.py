import pandas as pd

data = {
    "Country": ["Indonesia", "Japan", "India", "China", "United States", "Brazil", "Russia", "Italy", "Jerman", "Inggris"],
    "Capital": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moscow","Roma","Berlin","London"],
    "Continent": ["Asia", "Asia", "Asia", "Asia", "America", "America", "Asia", "Europe", "Europe", "Europe"],
    "Area": [1905, 377, 3287, 9597, 9834, 8515, 17098, 1308, 1412, 1907],
    "Population": [264, 143, 1252, 1357, 329, 210, 146, 138, 142, 197]
}
# df = pd.read_csv('filename.csv', index_col=0) # Used to read a CSV file
df = pd.DataFrame(data)
mean_population = df.Population.mean()
std_area = df.Area.std()

print("DataFrame:")
print(df)
print("\nMean Population:", mean_population)
print("Standard Deviation of Area:", std_area)
