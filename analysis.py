import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/customer_data.csv")

# Show dataset
print("\nDataset Preview:")
print(df.head())

# -----------------------------
# 1. Total Sales by Product
# -----------------------------
plt.figure()
sns.barplot(x="Product", y="PurchaseAmount", data=df)
plt.title("Sales by Product")
plt.show()

# -----------------------------
# 2. Region-wise Sales
# -----------------------------
plt.figure()
sns.barplot(x="Region", y="PurchaseAmount", data=df)
plt.title("Region-wise Sales")
plt.show()

# -----------------------------
# 3. Gender Analysis
# -----------------------------
plt.figure()
sns.barplot(x="Gender", y="PurchaseAmount", data=df)
plt.title("Gender vs Purchase Amount")
plt.show()

# -----------------------------
# 4. Age Distribution
# -----------------------------
plt.figure()
sns.histplot(df["Age"], bins=5)
plt.title("Customer Age Distribution")
plt.show()