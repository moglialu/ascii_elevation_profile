from tokenize import String
from xml.dom import minidom
import pandas as pd
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r



#read out gpx file and converts to pandas
user_input = input('Put your gpx file in the same folder as this script and enter the name here: ')
doc = minidom.parse(user_input)#your gpx file
trkpts = doc.getElementsByTagName('trkpt')
df = pd.DataFrame(columns= ['elevation', 'latitude', 'longitude', 'distance', 'altimeter'])
distances =[0,]
for trkpt in trkpts:
     elevation = trkpt.getElementsByTagName('ele')
     latitude = trkpt.getAttribute('lat')
     longitude = trkpt.getAttribute('lon')
     distance = 0
     altimeter = 0
     df.loc[len(df)]= (elevation[0].firstChild.data, latitude, longitude, distance, altimeter)
df = df.astype(float)

#calculating and writing distance
for i in range(len(df)):
    if i == 0:
        continue
    else:
        distances.append(haversine(
            lat1 = df.iloc[i-1]['latitude'],
            lon1 = df.iloc[i-1]['longitude'],
            lat2 = df.iloc[i]['latitude'],
            lon2 = df.iloc[i] ['longitude']
        ))
df['distance'] = distances

#calc and draw ascii for elevation profile
max_ele = df['elevation'].max()
min_ele = df['elevation'].min()
steps = (max_ele - min_ele)/5
dist250 = 0
loopcount = 0
x = ""
for index, row in df.iterrows():
    if loopcount < 1:
        if float(row['elevation']) <= (min_ele + (1*steps)):
            x = x + '.'
        elif float(row['elevation']) < (min_ele + (2*steps)):
            x = x + ':'
        elif float(row['elevation']) < (min_ele + (3*steps)):
            x = x + 'i'
        elif float(row['elevation']) < (min_ele + (4*steps)):
            x = x + 'I'
        elif float(row['elevation']) <= (min_ele + (5*steps)):
            x = x + 'Î'    
    elif dist250 < 0.24: # this value is an estimation so far (everytime the distance goes above it it takes a value and generates a symbol) this depends on how acurate and often your trackpoints are
        dist250 = dist250 + row['distance']
        continue
    else:
        if float(row['elevation']) <= (min_ele + (1*steps)):
            x = x + '.'
        elif float(row['elevation']) < (min_ele + (2*steps)):
            x = x + ':'
        elif float(row['elevation']) < (min_ele + (3*steps)):
            x = x + 'i'
        elif float(row['elevation']) < (min_ele + (4*steps)):
            x = x + 'I'
        elif float(row['elevation']) <= (min_ele + (5*steps)):
            x = x + 'Î'
        dist250 = 0   
    loopcount += 1



print('Total distance: ' + str(df['distance'].sum()))
print('Highest Point: ' + str(max_ele))
print('Lowest Point: ' + str(min_ele))
print('Elevation Profile: ' + x)
print(f'Steps: {steps} (Height difference between symbols)')

exit = input('Enter any key to close')







