import pandas as pd 
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For creating static visualizations
import numpy as np  # For numerical operations

# Load example datasets
iris = sns.load_dataset('iris')  # Famous iris flower dataset
mpg = sns.load_dataset('mpg')    # Car fuel consumption dataset
tips = sns.load_dataset('tips')  # Restaurant tips dataset

# 1. Heatmap Example
# Heatmaps are useful for visualizing matrix-like data
data = np.random.rand(5, 5)  # Create random 5x5 matrix
sns.heatmap(data, annot=True, cmap='coolwarm')  # Create heatmap with annotations
plt.title("Heatmap Example")
plt.show()

# # 2. Boxplot Example
# # Boxplots show the distribution of data based on five number summary
# sns.boxplot(x='day', y='total_bill', data=tips)  # Create boxplot of total bill by day
# plt.title("Boxplot of Total Bill Amounts by Day")
# plt.xlabel("Day of the Week")
# plt.ylabel("Total Bill ($)")
# plt.show()

# # 3. Pairplot Example
# # Pairplots show relationships between multiple variables
# sns.pairplot(iris, hue='species')  # Create pairplot colored by species
# plt.suptitle("Pairplot Example", y=1.02)  # Add title at the top
# plt.show()

# # 4. Distribution Plot Example
# # Histograms with KDE show the distribution of a single variable
# sns.histplot(tips['total_bill'], kde=True)  # Create histogram with density curve
# plt.title("Distribution Plot with KDE")
# plt.show()

# # 5. Correlation Heatmap Example
# # Shows relationships between numeric variables
# numeric_tips = tips.select_dtypes(include='number')  # Select only numeric columns
# corr = numeric_tips.corr()  # Calculate correlation matrix
# sns.heatmap(corr, annot=True, cmap='viridis')  # Create correlation heatmap
# plt.title("Correlation Heatmap of Numeric Variables")
# plt.show()

# # 6. Plot Aesthetics and Customization
# # Set the visual style of the plots
# sns.set_style('dark')  # Set dark background style
# sns.set_palette('bright')  # Set color palette
# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title("Customized Boxplot")
# plt.show()

# # 7. Context Adjustment
# # Adjust the scale of plot elements
# sns.set_context('notebook')  # Set the context for the plot
# sns.scatterplot(x='total_bill', y='tip', data=tips)  # Create scatter plot
# plt.title("Scatterplot with Notebook Context")
# plt.show()

# # 8. Violin Plot Example
# # Violin plots show the distribution of data
# sns.violinplot(x='day', y='total_bill', data=tips, palette='pastel')
# plt.title('Violin Plot of Total Bill by Day')
# plt.xlabel('Day of the Week')
# plt.ylabel('Total Bill ($)')
# plt.show()

# # 9. Swarm Plot Example
# # Swarm plots show individual data points
# sns.swarmplot(x='day', y='total_bill', data=tips, palette='muted')
# plt.title('Swarm Plot of Total Bill by Day')
# plt.xlabel('Day of the Week')
# plt.ylabel('Total Bill ($)')  # Fixed missing quote
# plt.show()


