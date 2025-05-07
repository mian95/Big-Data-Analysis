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
data = np.random.rand(5, 5)  # Create random 5x5 matrix
sns.heatmap(data, 
    annot=True,  # Show numbers in each cell
    cmap='coolwarm'  # Color scheme: other options include 'viridis', 'plasma', 'magma', 'YlOrRd'
)
plt.title("Heatmap Example")
plt.show()

# 2. Boxplot Example
# Boxplots show the distribution of data based on five number summary
sns.boxplot(
    x='day',  # Categorical variable for x-axis
    y='total_bill',  # Numerical variable for y-axis
    data=tips,  # DataFrame containing the data
    # palette='Set3'  # Optional: color palette for different categories
)
plt.title("Boxplot of Total Bill Amounts by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()

# 3. Pairplot Example
# Pairplots show relationships between multiple variables
sns.pairplot(
    iris,  # DataFrame to plot
    hue='species',  # Color points by this categorical variable
    # palette='husl',  # Optional: color scheme
    # diag_kind='kde'  # Optional: 'kde' for density, 'hist' for histogram
)
plt.suptitle("Pairplot Example", y=1.02)
plt.show()

# 4. Distribution Plot Example
# Histograms with KDE show the distribution of a single variable
sns.histplot(
    tips['total_bill'],  # Data to plot
    kde=True,  # Show density curve
    # bins=30,  # Optional: number of bins
    # color='skyblue'  # Optional: color of the histogram
)
plt.title("Distribution Plot with KDE")
plt.show()

# 5. Correlation Heatmap Example
# Shows relationships between numeric variables
numeric_tips = tips.select_dtypes(include='number')  # Select only numeric columns
corr = numeric_tips.corr()  # Calculate correlation matrix
sns.heatmap(
    corr,  # Correlation matrix
    annot=True,  # Show correlation values
    cmap='viridis',  # Color scheme
    # vmin=-1, vmax=1  # Optional: set color scale limits
)
plt.title("Correlation Heatmap of Numeric Variables")
plt.show()

# 6. Plot Aesthetics and Customization
# Set the visual style of the plots
sns.set_style('dark')  # Style options: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
sns.set_palette('bright')  # Color palette options: 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("Customized Boxplot")
plt.show()

# 7. Context Adjustment
# Adjust the scale of plot elements
sns.set_context('notebook')  # Context options: 'paper', 'notebook', 'talk', 'poster'
sns.scatterplot(
    x='total_bill',  # X-axis variable
    y='tip',  # Y-axis variable
    data=tips,  # DataFrame
    # hue='day',  # Optional: color points by this variable
    # size='size',  # Optional: vary point size by this variable
    # alpha=0.5  # Optional: transparency (0 to 1)
)
plt.title("Scatterplot with Notebook Context")
plt.show()

# 8. Violin Plot Example
# Violin plots show the distribution of data
sns.violinplot(
    x='day',  # Categorical variable
    y='total_bill',  # Numerical variable
    data=tips,  # DataFrame
    palette='pastel',  # Color scheme
    # inner='box'  # Optional: 'box', 'quartile', 'point', 'stick'
)
plt.title('Violin Plot of Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill ($)')
plt.show()

# 9. Swarm Plot Example
# Swarm plots show individual data points
sns.swarmplot(
    x='day',  # Categorical variable
    y='total_bill',  # Numerical variable
    data=tips,  # DataFrame
    palette='muted',  # Color scheme
    # size=8,  # Optional: size of points
    # alpha=0.7  # Optional: transparency
)
plt.title('Swarm Plot of Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill ($)')
plt.show()


