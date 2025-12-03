import pandas as pd

# Step 1: Create dummy data using dictionary
data = {
    "Country": ["Indonesia", "Japan", "India", "China", "United States", 
                "Brazil", "Russia", "Germany", "France", "Australia"],
    "Capital": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", 
                "Brasilia", "Moscow", "Berlin", "Paris", "Canberra"],
    "Continent": ["Asia", "Asia", "Asia", "Asia", "America", 
                  "America", "Asia", "Europe", "Europe", "Oceania"],
    "Area": [1905, 377, 3287, 9597, 9834, 8515, 17098, 357, 551, 7692],
    "Population": [264, 143, 1252, 1357, 329, 210, 146, 83, 67, 25]
}

# Step 2: Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Step 3: Write DataFrame to CSV file
df.to_csv("countries.csv", index=False)

# Step 4: Print confirmation
print("CSV file 'countries.csv' has been created successfully!")
print(df)

