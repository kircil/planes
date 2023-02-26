import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import distance

# Create a geolocator object
geolocator = Nominatim(user_agent="distance_calculator")

# Read the csv file into a DataFrame
df = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_0.csv')

# Ask user for input
dep = input("Enter departure city: ")
arr = input("Enter arrival city: ")

# Handle exceptions that may occur while geocoding the input cities
try:
    location1 = geolocator.geocode(dep)
    location2 = geolocator.geocode(arr)

    # Check if both cities were found
    if location1 and location2:
        coords1 = (location1.latitude, location1.longitude)
        coords2 = (location2.latitude, location2.longitude)
        dist = int(distance(coords1, coords2).nm)
        print(f"The distance between {dep} and {arr} is {dist} nautical miles.")
    else:
        print("One or both cities not found.")
except:
    print("Error occurred while geocoding the cities.")

# Ask user for the passenger count
try:
    capacity = int(input("How many passengers? "))
except:
    print("Invalid input for passenger count.")

# Filter the sector column
filtered_sector = df.iloc[:, -3].astype(str).str.replace(',', '').str.slice(0, 4).astype(int)

# Create a new DataFrame with some conditions
filtered_fps = df[(df['Seats'] > capacity) & (filtered_sector > dist)]

# Specify the color of the bars in the bar plot
plt.bar(filtered_fps.iloc[:,0], filtered_fps.iloc[:,2], color='blue')

# Add labels to the plot
plt.xlabel('Aircraft Model')
plt.ylabel('Flight Range (nm)')
plt.title('Aircraft List for this trip')

# Show the plot
plt.show()
