import numpy as np
import googlemaps
import pandas as pd

API_key = 'AIzaSyAF2K0eUKUbmwC5fvxEY3a-Yw1IGlG4FPM' #your API here
gmaps = googlemaps.Client(key=API_key)

df = pd.read_excel('coordinate.xlsx', engine='openpyxl', sheet_name='Sheet1')
df = df[['latitude', 'longitude']]
sales1 = np.array(df)

m,n = sales1.shape
hasil = np.zeros((m, m))

for i in range(m):
    for j in range(len(df)):

        origin = sales1[i, 0], sales1[i, 1]
        destination = sales1[j, 0], sales1[j, 1]
        
        koord = gmaps.distance_matrix((origin) , (destination))
        jarak = koord['rows'][0]['elements'][0]['distance']['value']/1000 #convert to kilometers

        print("Origin= ", i, "Destination= ", j,"Distance=", jarak)
        hasil[i, j] = jarak

dfh = (pd.DataFrame(hasil))
dfh.to_csv('calculated_distances.csv', sep=';', index=None)
print('Calculating is done, the result saved to CSV!')
