import matplotlib.pyplot as plt
import csv

# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.

with open('files/Libraries_-_2017_Visitors_by_Location.csv') as f:
    reader = csv.reader(f) # make a reader object
    data = list(reader) # casting the reader object as a list

'''names = [x[0].strip() for x in data][1:] # all chi library names (alphabetical)
name_index = [x for x in range(len(names))]
print(name_index)'''

# print(data)
ytd = [x[1] for x in data][1:]
ytd = [int(x) for x in ytd] # year to date computer sessions for libraries
month_data = []
for i in range(12):
    month_data.append([x[i + 1] for x in data][1:])

for x in range(len(month_data)):
    for y in range(len(month_data[x])):
        try:
            month_data[x][y] = int(month_data[x][y])
        except:
            month_data[x].pop(y)
print(month_data[11])

# add upp all the libararies for each month and display
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
plt.figure(1, figsize=(16, 8), tight_layout=True)
plt.bar([x for x in range(12)], [sum(x) for x in month_data])
plt.xticks([x for x in range(12)], months, rotation=90, fontsize=8) # indexed list, strings as list
plt.ylabel("Computer Sessions Across Chicago")
plt.title("Total Public Library Computer Sessions in Chicago During 2017", fontsize=20)
# plt.show()

# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.
plt.figure(2, figsize=(16, 8), tight_layout=True, facecolor='blue')
transit_methods = ['Bus', 'Paratransit', 'Rail']
with open('files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f) # make a reader object
    t_data = list(reader) # casting the reader object as a list

# print('wflhweoufouwehnfbc', transit_data[1][1:]) # first year of data is 1988
transit_data = []
for i in range(len(t_data)):
    transit_data.append(t_data[i][1:])

for x in range(len(transit_data[1:])):
    for y in range(len(transit_data[1:][x])):
        transit_data[1:][x][y] = int(transit_data[1:][x][y])

transit_data.pop(0)
print(transit_data)
bus_by_year = [x[0] for x in transit_data]
paratransit_by_year = [x[1] for x in transit_data]
rail_by_year = [x[2] for x in transit_data]
total_by_year = [x[3] for x in transit_data]

plt.plot([x for x in range(1988, 2017)], [x for x in bus_by_year], label="Bus")
plt.plot([x for x in range(1988, 2017)], [x for x in paratransit_by_year], label="Paratransit")
plt.plot([x for x in range(1988, 2017)], [x for x in rail_by_year], label="Rail")
plt.plot([x for x in range(1988, 2017)], [x for x in total_by_year], label="Total")
plt.grid(color='b', linestyle='-', linewidth=2)
plt.ylabel("Public Transportation Rides Given (x10^8)", color="white")
plt.title("Public Transportation Usage from 1988 to 2016", fontsize=20, color="white")
plt.legend(bbox_to_anchor=(0.9, 0.25), loc="center")
plt.show()