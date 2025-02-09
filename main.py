import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
os.makedirs("images", exist_ok=True)

# Question 1: How does carat affect price?
x = data["carat"].values
y = data["price"].values

def model(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = opt.curve_fit(model, x, y)
plt.scatter(x, y, alpha=0.3)
plt.plot(x, model(x, *params), color='red')
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Curve Fit: Carat vs Price")
plt.savefig("images/carat_vs_price.png")
plt.close()

# Question 2: Is the price distribution normal?
test_stat, p_value = stats.shapiro(data["price"])
print("Shapiro-Wilk Test:", test_stat, p_value)

plt.hist(data["price"], bins=50, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Distribution")
plt.savefig("images/price_distribution.png")
plt.close()

# Question 3: What are the principal components of the dataset?
pca = PCA(n_components=2)
pca_data = pca.fit_transform(data[["carat", "depth", "table", "price", "x", "y", "z"]])
plt.scatter(pca_data[:, 0], pca_data[:, 1], alpha=0.3)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Analysis")
plt.savefig("images/pca_analysis.png")
plt.close()

# Follow-up Question 1: How does cut quality impact price?
data.groupby("cut")["price"].mean().plot(kind='bar', color='green', edgecolor='black')
plt.xlabel("Cut Quality")
plt.ylabel("Average Price")
plt.title("Average Price by Cut Quality")
plt.savefig("images/price_by_cut.png")
plt.close()

# Follow-up Question 2: What is the correlation between table and price?
correlation = np.corrcoef(data["table"], data["price"])[0, 1]
print("Correlation between table and price:", correlation)

plt.scatter(data["table"], data["price"], alpha=0.3)
plt.xlabel("Table")
plt.ylabel("Price")
plt.title("Table vs Price")
plt.savefig("images/table_vs_price.png")
plt.close()

# Follow-up Question 3: How does carat weight compare across different cut qualities?
data.boxplot(column="carat", by="cut", grid=False)
plt.xlabel("Cut Quality")
plt.ylabel("Carat")
plt.title("Carat Distribution by Cut Quality")
plt.suptitle("")
plt.savefig("images/carat_by_cut.png")
plt.close()
