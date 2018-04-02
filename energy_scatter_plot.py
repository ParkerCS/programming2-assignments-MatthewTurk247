'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.  
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)


Challenge (for fun):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intensity show in red.
- Add colleges and universities (use a different marker type)

'''
import matplotlib.pyplot as plt
import numpy as np
import csv

t = "Hello"
result = ''
for i in range(len(t)):
    result += (t[-i + (len(t) - 1)])

print(result)

with open('files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)
print(data)
data = [x for x in data if x[6] == 'K-12 School']
# di that lambda thing that Mr. Lee said to make it sorted by the intensity and then only plot those
names = []
square_footage = []
output = []

# look in 21 and delete the blanks

# for i in range(len(data[21])):
#     try:
#         data[21][i] = int(data[21][i])
#     except:
#         data[21][i] = 0


data = [x for x in data if x[21] != ""]
data.sort(key=lambda x: float(x[21])) # sorts the data by GHG intensity

for i in range(len(data)):
    try:
        sf = float(data[i][7])
        op = float(data[i][20])
        square_footage.append(sf)
        names.append(data[i][2])
        output.append(op)
    except:
        print("failed", data[i][2])

print(len(square_footage), len(output))

# GHG/sq footage
# lambda - anonymous single line function
# lambda parameter: returned value

products = lambda x, y: x*y
print(products(9, 8))

plt.figure(1, figsize=(12, 7), facecolor='lightslategray')

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(square_footage, output)

yfit = [a + b * xi for xi in square_footage]
plt.plot(square_footage, yfit)

plt.scatter(square_footage, output, alpha=0.5)

# top 10% is 39 schools

for i in range(1):
    plt.annotate(names[i], xy=(square_footage[i], output[i]))

for i in range(2):
    plt.annotate(names[-i], xy=(square_footage[-i], output[-i]))

parker_index = names.index("Francis W Parker School")
print(parker_index)

plt.annotate(names[parker_index], xy=(square_footage[parker_index], output[parker_index]))

# color the dots
green = [names[x] for x in range(40)]
green_sq = [square_footage[x] for x in range(40)]
green_output = [output[x] for x in range(40)]
print(green)
red = [names[-x] for x in range(40)]
red_sq = [square_footage[-x] for x in range(40)]
red_output = [output[-x] for x in range(40)]
print(red)

plt.scatter(green_sq, green_output, color='green', alpha=0.5)
plt.scatter(red_sq, red_output, color='red', alpha=0.5)
plt.scatter([square_footage[0]], [output[0]], color='green')

'''
for i in range(len(green)):
    if i < 10:
        plt.annotate(green[i], xy=(square_footage[i], output[i]), color="green", alpha=0.5)
    else:
        plt.annotate('', xy=(square_footage[i], output[i]), color="green", alpha=0.5)

for i in range(len(red)):
    if i < 10:
        plt.annotate(red[i], xy=(square_footage[i], output[i]), color="red", alpha=0.5)
    else:
        plt.annotate('', xy=(square_footage[i], output[i]), color="red", alpha=0.5)
'''
plt.title("Efficiency of Schools in Chicago", fontsize=20)
plt.ylabel("CO2 Output in metric tons")
plt.xlabel("Square footage (mi^2)")
plt.show()

# run to classes
