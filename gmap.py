from gmplot import *
import csv
import random

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

mymap = GoogleMapPlotter(41.8339037, -87.6439047, 12, apikey=apikey) # lat, long, zoom_label, apikey=

mymap.marker(41.9228518, -87.6404075)
mymap.circle(41.9228518, -87.6404075, 1000, "#FF0000") # lat, long, radius (in meters), web_color

mylats = [41.9228518 + x/50 for x in range(10)]
mylongs = [-87.6404075 + x/50 for x in range(10)]
mymap.plot(mylats, mylongs, "blue")

mylats = [41.9228518, 41.9328518, 41.9228518]
mylongs = [-87.6304075, -87.6404075, -87.6504075]
mymap.polygon(mylats, mylongs)

with open('../files/Parks_-_Public_Art.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
size = [random.randrange(1, 500) for x in data]
print(lats[1], longs[1])

mymap.scatter(lats, longs, marker=False, color='green', size=10)

# for i in range(len(lats)):
#     mymap.circle(lats[i], longs[i], size[i])

mymap.heatmap(lats, longs, threshold=4, radius=20, dissipating=True)

mymap.draw('./mymap.html') # la pièce de résistance