import pandas as pd 
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For creating static visualizations
import numpy as np  # For numerical operations

# Load example datasets
iris = sns.load_dataset("iris") # Famous iris flower dataset
mpg = sns.load_dataset('mpg')    # Car fuel consumption dataset
tips = sns.load_dataset('tips')  # Restaurant tips dataset

# 1. Heatmap Example
# Heatmaps are useful for visualizing matrix-like data
# data = np.random.rand(5, 5)  # Create random 5x5 matrix
# Create heatmap with annotations
# Args:
# - data: The data to plot. Can be a DataFrame, numpy array, or list of lists.
# - annot: If True, write the data value in each cell. Default is False.
# - cmap: The colormap to use. 'coolwarm' is a diverging colormap, suitable for data that has a critical middle point. Other options include 'viridis', 'plasma', 'inferno', 'magma', 'cividis', etc.
# sns.heatmap(data, annot=True, cmap='magma')
# plt.title("Heatmap Example")
# plt.show()

# 2. Boxplot Example
# Boxplots show the distribution of data based on five number summary
# Args:
# - x: The column name in the dataset for the x-axis. In this case, 'day' to categorize the data by day of the week.
# - y: The column name in the dataset for the y-axis. In this case, 'total_bill' to plot the total bill amounts.
# - data: The dataset to use for plotting. In this case, 'tips' dataset is used.
# Other possible values for x and y can be any column names in the dataset that are relevant for the analysis.
# For example, x could be 'sex' to categorize by sex, and y could be 'tip' to plot tip amounts.
# sns.boxplot(x='day', y='total_bill', data=tips)  # Create boxplot of total bill by day
# plt.title("Boxplot of Total Bill Amounts by Day")
# plt.xlabel("Day of the Week")
# plt.ylabel("Total Bill ($)")
# plt.show()

# 3. Pairplot Example
# Pairplots show relationships between multiple variables
# Args:
# - data: The dataset to use for plotting. In this case, 'iris' dataset is used.
# - hue: The column name in the dataset to map plot aspects to different colors. In this case, 'species' to color the plots by species.
# Purpose: To create a pairplot that visualizes relationships between all pairs of variables in the dataset, with different colors for each species.
# Other possible values for hue can be any column name in the dataset that is relevant for the analysis.
# For example, if the dataset had a 'color' column, hue could be 'color' to plot by color.
# sns.pairplot(iris, hue='species')  # Create pairplot colored by species
# plt.suptitle("Pairplot Example", y=1.02)  # Add title at the top
# plt.show()

# 4. Distribution Plot Example
# Histograms with KDE (kernel density estimate) show the distribution of a single variable
# Args:
# - data: The data to plot. In this case, 'total_bill' column from the 'tips' dataset.
# - kde: If True, compute and plot a kernel density estimate (KDE) on the data. Default is False.
# Purpose: To create a histogram with a density curve to visualize the distribution of the 'total_bill' variable.
# Other possible values for kde can be False to only plot the histogram without the density curve.
# sns.histplot(tips['total_bill'], kde=True)  # Create histogram with density curve
# plt.title("Distribution Plot with KDE")
# plt.show()

# # 5. Correlation Heatmap Example
# # Shows relationships between numeric variables
# # Select only numeric columns from the 'tips' dataset
# numeric_tips = tips.select_dtypes(include='number')  
# # Calculate the correlation matrix for the numeric columns
# corr = numeric_tips.corr()  
# # Create a heatmap to visualize the correlation matrix
# # heatmap => depicts values for a main variable of interest across two axis variables as a grid of colored squares
# # Args:
# # - data: The data to plot. In this case, the correlation matrix 'corr'.
# # - annot: If True, write the data value in each cell. Default is False. In this case, set to True to display correlation values.
# # - cmap: The colormap to use. 'viridis' is a perceptually uniform colormap, suitable for visualizing data with a continuous range. Other options include 'coolwarm', 'plasma', 'inferno', 'magma', 'cividis', etc.
# sns.heatmap(corr, annot=True, cmap='viridis')  
# plt.title("Correlation Heatmap of Numeric Variables")  # Set the title of the plot
# plt.show()  # Display the plot


# # 6. Plot Aesthetics and Customization
# # Set the visual style of the plots
# sns.set_style('dark')  # Set dark background style. This argument controls the overall aesthetic of the plot, including the background color, grid lines, and other elements. Other possible values include 'white', 'darkgrid', 'whitegrid', 'ticks', and 'dark'.
# sns.set_palette('bright')  # Set color palette. This argument determines the color scheme used for the plot. Other possible values include 'deep', 'muted', 'pastel', 'dark', 'colorblind', and 'Paired'.
# sns.boxplot(x='day', y='total_bill', data=tips)  # Create a boxplot with customized aesthetics.
# plt.title("Customized Boxplot")  # Set the title of the plot.
# plt.show()  # Display the plot.

# # 7. Context Adjustment
# # Adjust the scale of plot elements
# # Args:
# # - 'notebook': The context to set for the plot. This argument controls the scale of plot elements such as font sizes, line widths, and marker sizes. 'notebook' is suitable for Jupyter notebooks, but other options include 'paper', 'talk', 'poster', and 'presentation' for different display environments.
# # Purpose: To adjust the visual elements of the plot to be suitable for the display environment.
# # Other possible values for context can be 'paper', 'talk', 'poster', 'presentation' depending on the intended display environment.
# sns.set_context('notebook')  # Set the context for the plot
# sns.scatterplot(x='total_bill', y='tip', data=tips)  # Create scatter plot
# plt.title("Scatterplot with Notebook Context")
# plt.show()

# # 8. Violin Plot Example
# # Violin plots show the distribution of data
# # Args:
# # - x: The column name in the dataset for the x-axis. In this case, 'day' to categorize the data by day of the week.
# # - y: The column name in the dataset for the y-axis. In this case, 'total_bill' to show the distribution of total bills.
# # - data: The dataset to plot. In this case, 'tips' dataset.
# # - palette: The color palette to use for the plot. In this case, 'pastel' for a soft, pastel color scheme. Other possible values include 'deep', 'muted', 'bright', 'dark', 'colorblind', 'Paired', etc.
# sns.violinplot(x='day', y='total_bill', data=tips, palette='pastel')
# plt.title('Violin Plot of Total Bill by Day')  # Set the title of the plot
# plt.xlabel('Day of the Week')  # Set the label for the x-axis
# plt.ylabel('Total Bill ($)')  # Set the label for the y-axis
# plt.show()  # Display the plot

# 9. Swarm Plot Example
# Swarm plots show individual data pointsj
# Args:
# - x: The column name in the dataset for the x-axis. In this case, 'day' to categorize the data by day of the week.
# - y: The column name in the dataset for the y-axis. In this case, 'total_bill' to show the distribution of total bills.
# - data: The dataset to plot. In this case, 'tips' dataset.
# - palette: The color palette to use for the plot. In this case, 'muted' for a muted color scheme. Other possible values include 'deep', 'pastel', 'bright', 'dark', 'colorblind', 'Paired', etc.
sns.swarmplot(x='day', y='total_bill', data=tips, palette='muted')
plt.title('Swarm Plot of Total Bill by Day')  # Set the title of the plot
plt.xlabel('Day of the Week')  # Set the label for the x-axis
plt.ylabel('Total Bill ($)')  # Set the label for the y-axis
plt.show()  # Display the plot


