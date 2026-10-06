# 🛒 Retail Market Basket Clustering

## 📌 Project Overview

Retail businesses generate large amounts of transaction data containing information about customers, products, quantities, prices, and transaction values. Analyzing this data can help identify meaningful groups of transactions and understand different purchasing patterns.

This project applies **K-Means Clustering** to retail transaction data to group similar transactions based on selected numerical features. The project also provides an interactive **Streamlit dashboard** for exploring the dataset and visualizing the resulting clusters.

---

## 🚀 Live Dashboard

🔗 **[Open the Retail Market Basket Clustering Dashboard](https://retail-market-basket-clustering-8cahc3enf6pvqbpvwxfcre.streamlit.app/)**

The dashboard provides interactive filtering, retail overview statistics, product category analysis, K-Means cluster visualization, cluster summaries, and cluster interpretation.

---

## 🎯 Objectives

- Analyze retail transaction data.
- Perform data preprocessing and exploratory analysis.
- Select suitable numerical features for clustering.
- Apply the **K-Means clustering algorithm**.
- Determine a suitable number of clusters using the **Silhouette Score**.
- Visualize the resulting clusters.
- Compare the characteristics of different clusters.
- Develop an interactive Streamlit dashboard for presenting the results.

---

## 📂 Dataset

The dataset contains **1,000 retail transaction records** with the following attributes:

| Feature | Description |
|---|---|
| Transaction ID | Unique identifier for each transaction |
| Date | Transaction date |
| Customer ID | Unique customer identifier |
| Gender | Customer gender |
| Age | Customer age |
| Product Category | Category of the purchased product |
| Quantity | Quantity purchased |
| Price per Unit | Price of one unit of the product |
| Total Amount | Total transaction amount |
| Month | Month of the transaction |
| Cluster | Cluster assigned using K-Means |

---

## 🔍 Methodology

The project follows these major steps:

### 1. Data Loading

The retail transaction dataset was loaded and inspected to understand its structure, features, and data types.

### 2. Data Preprocessing

The data was prepared for clustering by selecting relevant numerical features and ensuring that the data was suitable for applying the K-Means algorithm.

### 3. Feature Selection

Different combinations of numerical features were evaluated to identify a suitable feature set for clustering.

The final model uses:

- **Age**
- **Price per Unit**
- **Total Amount**

### 4. Feature Scaling

Since the selected features have different numerical ranges, **StandardScaler** was used to standardize the features before applying K-Means.

### 5. K-Means Clustering

K-Means was applied with different values of K to compare the quality of clustering.

The Silhouette Score was used to evaluate how well the resulting clusters were separated.

### 6. Final Model

The final clustering model uses:

- **Algorithm:** K-Means Clustering
- **Number of Clusters:** 2
- **Features:** Age, Price per Unit, Total Amount
- **Silhouette Score:** approximately **0.503**

A higher Silhouette Score indicates better separation between clusters. The selected model provides a reasonable separation of the retail transactions.

---

## 📊 Cluster Visualization

The main visualization in the dashboard shows:

**Price per Unit vs Total Amount**

Each point represents a retail transaction, while the different cluster labels indicate the group assigned by the K-Means algorithm.

This visualization helps understand how the transactions are distributed across the two clusters.

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

### 📊 Retail Overview
- Total Transactions
- Total Revenue
- Average Transaction
- Number of Clusters
- Silhouette Score

### 🛍️ Product Category Analysis
- Transactions by Product Category
- Revenue by Product Category

### 🎯 K-Means Cluster Analysis
- Main K-Means cluster visualization
- Cluster distribution
- Cluster-wise average values
- Product Category distribution by cluster
- Cluster interpretation

### 🔎 Interactive Filters
Users can filter the dashboard based on:

- Product Category
- Gender

---

## 🧠 Cluster Analysis

The clusters are analyzed using the average values of:

- Age
- Price per Unit
- Total Amount

This helps compare the characteristics of the transactions assigned to each cluster.

The dashboard dynamically displays the cluster statistics and interpretation based on the selected filters.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Streamlit**
- **Jupyter Notebook / Google Colab**
- **Git & GitHub**

---

## 📁 Project Structure

```text
Retail-Market-Basket-Clustering/
│
├── app.py
├── retail_dashboard_data.csv
├── model_info.json
├── requirements.txt
└── README.md
