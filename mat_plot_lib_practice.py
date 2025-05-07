import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import subplot


air = pd.read_csv('air.csv')
# print(air.head())

# air['station_paris'].plot()
# air.plot.scatter(x='station_london',y="station_paris")
# air.plot.box()
# air.plot.area(figsize=(9,4), subplots=True)
# plt.show()

# ---------------------------------------

# plt.plot(air["station_london"], air["station_paris"], "g^")
# we can you these args for different types of plots
"""Plotting Style Codes:
- 'ro': Red circles
- 'g^': Green triangles
- 'b*': Blue stars
- 'c+': Cyan inlines
- 'ko': Black squares
- 'o': 
- 'rx': Red x's
- 'gD': Green diamonds
- 'g--': Green dashed line
- 'r--': Red dashed line
- 'bs': Blue squares
- 'k-': Black solid line
- 'm--': Magenta dashed line"""
# plt.plot([1,5,15,35], [23,34,55,45],"k-")                                                     #use for line 
# plt.scatter(air["station_london"], air["station_paris"],)                                     #use to show the data as of points
# plt.hist(air["station_london"], density=True, facecolor="g" , histtype="stepfilled" )         #use to show the data in the form of histogram

# ---Hist is mostly use for the distribution of data---
# density=True:
# When set to True, the histogram will display the probability density instead of the raw counts. This means that the area under the histogram will sum to 1, which is useful for comparing distributions.
# facecolor="g":
# This specifies the color of the histogram bars. In this case, "g" stands for green. You can change this to other color codes (like "r" for red, "b" for blue, etc.) or use hex color codes (like #FF5733).
# histtype="step":
# This argument determines the type of histogram to draw. The "step" type creates a line plot that outlines the histogram instead of filling it with color. Other options include:
# "bar": Traditional filled bars.
# "step"
# "barstacked": Stacked bars.
# "stepfilled": Filled step histogram.

# plt.xlabel("Station London Values")
# plt.ylabel("Probability Density")
# plt.suptitle("Histogram of Station London Values")
# plt.show()




# ------------------- This code creates a figure with 3 subplot.
groups = ['group 1', 'group2', 'group3']
values = [5,25,100]
# plt.figure(figsize=(9,4))
# # Creating a bar plot for the groups and their corresponding values
# plt.subplot(131)
# plt.bar( groups,values )
# # Creating a scatter plot for the values and groups
# plt.subplot(132)
# plt.scatter(values, groups, color='r')
# # Creating a line plot for the values and groups
# plt.subplot(133)
# plt.plot(values, groups, 'ro-')
# plt.show()

# --------------------- other way for subplot
# plt.figure(figsize=(9,3))
# plt.subplot(1,3,1)
# plt.bar(groups, values)
# plt.subplot(1, 3, 2)
# plt.scatter (values, values)
# plt.subplot(1, 3, 3)
# plt.plot(values) 
# plt.suptitle("this is categorical")
# # plt.tight_layout(pad=2.0)
# plt.show()



#subplots this is not same from the previous both  ==> we can say that this is for the 2_D plots
# fig , axs = plt.subplots(2,3,figsize=(9.3))
# axs[0,0].bar(groups,values)
fig, axs = plt.subplots(2, 3, figsize=(9,3))
axs[0,0].bar(groups, values, color='purple')
axs[0,0].set_title('Bar Chart')
axs[0,1].hist(values)
axs[0,1].set_title("histogram")
axs[0,2].plot(groups, values, 'g--')
axs[0,2].set_title("line charts")
axs[1,0].bar(groups, values, color='yellow')
axs[1,1].scatter(groups, values)
axs[1,2].plot(values, groups, 'rs')
plt.show()