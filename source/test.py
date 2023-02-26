import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import distance
geolocator = Nominatim(user_agent="distance_calculator")

# put this csv file on a data frame
df = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency.csv') 


dep = input("Enter departure city: ") # Ask user to enter a departure city
arr = input("Enter arrival city: ") # Ask user to enter an arrival city
capacity = int(input("How many passengers? ")) # Ask user for the passenger count

location1 = geolocator.geocode(dep) 
location2 = geolocator.geocode(arr)

if location1 and location2:
    coords1 = (location1.latitude, location1.longitude) # coordinates of the departure city
    coords2 = (location2.latitude, location2.longitude) # coordinates of the arrival city
    dist = int(distance(coords1, coords2).nm) #returns the distance in nautical miles
    print(dist)
else:
    print("One or both cities not found.")


dist_km = dist * 1.852
print(dist_km)

# Still working on the next few lines. Trying to calculate the price of fuel burnt and display it on the plot.

# filtered_fps = df.iloc[:, -1].str.slice(0, 4) 
# tr = (dist_km * filtered_fps.astype(float))/100
# gas_price = 4 # Price of fuel per liter in dollars
# total_price = tr*gas_price # Total fuel price
# print(total_price)


# In the bottom line, we take the first 4 characters of the sector column.
# During this process, we get rid of the ',' (by using str.replace) in order to return this value as an integer. 
filtered_sector = df.iloc[:, -3].str.slice(0, 5)
real_sector = filtered_sector.str.replace(',', '')
real_sector = real_sector.astype(int)

# Create a new data frame with some conditions
new_list = df[(df['Seats'] > capacity) & (real_sector > dist)]
print(new_list.iloc[:, 0])


plt.bar(new_list.iloc[:,0], new_list.iloc[:,-1])
plt.xticks(rotation=90, fontsize = 9)
plt.xlabel('Aircraft Model', labelpad=10)
plt.ylim(bottom=0)
plt.ylabel('Fuel Per Seat')
plt.title('Aircraft List for this trip')
fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.subplots_adjust(bottom=0.35, left=0.35)
plt.show()
