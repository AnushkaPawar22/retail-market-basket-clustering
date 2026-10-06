
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Retail Clustering Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("retail_dashboard_data.csv")

with open("model_info.json", "r") as f:
    model_info = json.load(f)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🛒 Retail Market Basket Clustering Dashboard")

st.markdown(
    "### Retail Transaction Analysis and Customer Segmentation"
)

st.markdown("---")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

categories = sorted(df["Product Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Product Category",
    categories,
    default=categories
)

genders = sorted(df["Gender"].dropna().unique())

selected_genders = st.sidebar.multiselect(
    "Select Gender",
    genders,
    default=genders
)

# Apply filters
filtered_df = df[
    (df["Product Category"].isin(selected_categories)) &
    (df["Gender"].isin(selected_genders))
].copy()

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.subheader("📊 Retail Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Transactions",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Total Revenue",
        f"${filtered_df['Total Amount'].sum():,.0f}"
    )

with col3:
    st.metric(
        "Average Transaction",
        f"${filtered_df['Total Amount'].mean():,.2f}"
    )

with col4:
    st.metric(
        "Clusters",
        model_info["clusters"]
    )

with col5:
    st.metric(
        "Silhouette Score",
        model_info["silhouette_score"]
    )

st.markdown("---")

# --------------------------------------------------
# PRODUCT CATEGORY ANALYSIS
# --------------------------------------------------

st.subheader("🛍️ Product Category Analysis")

col1, col2 = st.columns(2)

with col1:

    category_count = filtered_df["Product Category"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 5))

    category_count.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Transactions by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Number of Transactions")
    plt.xticks(rotation=0)

    st.pyplot(fig)

with col2:

    category_revenue = filtered_df.groupby(
        "Product Category"
    )["Total Amount"].sum()

    fig, ax = plt.subplots(figsize=(7, 5))

    category_revenue.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Revenue by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Revenue")
    plt.xticks(rotation=0)

    st.pyplot(fig)

# --------------------------------------------------
# GENDER ANALYSIS
# --------------------------------------------------

st.subheader("👥 Gender Analysis")

col1, col2 = st.columns(2)

with col1:

    gender_count = filtered_df["Gender"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 5))

    gender_count.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Transactions by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Number of Transactions")

    st.pyplot(fig)

with col2:

    gender_revenue = filtered_df.groupby(
        "Gender"
    )["Total Amount"].sum()

    fig, ax = plt.subplots(figsize=(7, 5))

    gender_revenue.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Revenue by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Total Revenue")

    st.pyplot(fig)

# --------------------------------------------------
# CUSTOMER / TRANSACTION ANALYSIS
# --------------------------------------------------

st.subheader("📈 Transaction Analysis")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.hist(
        filtered_df["Age"],
        bins=20
    )

    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Transactions")

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.hist(
        filtered_df["Total Amount"],
        bins=20
    )

    ax.set_title("Total Transaction Amount Distribution")
    ax.set_xlabel("Total Amount")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

# --------------------------------------------------
# QUANTITY VS TOTAL AMOUNT
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        filtered_df["Quantity"],
        filtered_df["Total Amount"],
        alpha=0.6
    )

    ax.set_title("Quantity vs Total Amount")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Total Amount")

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        filtered_df["Price per Unit"],
        filtered_df["Total Amount"],
        alpha=0.6
    )

    ax.set_title("Price per Unit vs Total Amount")
    ax.set_xlabel("Price per Unit")
    ax.set_ylabel("Total Amount")

    st.pyplot(fig)

# --------------------------------------------------
# CLUSTER ANALYSIS
# --------------------------------------------------

st.markdown("---")

st.header("🎯 Cluster Analysis")

st.write(
    "K-Means clustering was performed using Age, "
    "Price per Unit and Total Amount."
)

# --------------------------------------------------
# CLUSTER DISTRIBUTION
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    cluster_count = filtered_df["Cluster"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(7, 5))

    cluster_count.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Number of Transactions in Each Cluster")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Number of Transactions")

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(7, 5))

    for cluster in sorted(filtered_df["Cluster"].unique()):

        cluster_data = filtered_df[
            filtered_df["Cluster"] == cluster
        ]

        ax.scatter(
            cluster_data["Price per Unit"],
            cluster_data["Total Amount"],
            alpha=0.6,
            label=f"Cluster {cluster}"
        )

    ax.set_title("K-Means Cluster Visualization")
    ax.set_xlabel("Price per Unit")
    ax.set_ylabel("Total Amount")
    ax.legend()

    st.pyplot(fig)

# --------------------------------------------------
# CLUSTER SUMMARY
# --------------------------------------------------

st.subheader("📋 Cluster-wise Summary")

cluster_summary = filtered_df.groupby("Cluster")[
    ["Age", "Price per Unit", "Total Amount"]
].mean()

st.dataframe(
    cluster_summary.round(2),
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER + PRODUCT CATEGORY
# --------------------------------------------------

st.subheader("🛍️ Product Category Distribution by Cluster")

cluster_category = pd.crosstab(
    filtered_df["Cluster"],
    filtered_df["Product Category"]
)

st.dataframe(
    cluster_category,
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER + GENDER
# --------------------------------------------------

st.subheader("👥 Gender Distribution by Cluster")

cluster_gender = pd.crosstab(
    filtered_df["Cluster"],
    filtered_df["Gender"]
)

st.dataframe(
    cluster_gender,
    use_container_width=True
)

# --------------------------------------------------
# CLUSTER INTERPRETATION
# --------------------------------------------------

st.markdown("---")

st.header("🔎 Cluster Interpretation")

for cluster in sorted(filtered_df["Cluster"].unique()):

    cluster_data = filtered_df[
        filtered_df["Cluster"] == cluster
    ]

    avg_age = cluster_data["Age"].mean()
    avg_price = cluster_data["Price per Unit"].mean()
    avg_amount = cluster_data["Total Amount"].mean()

    st.write(
        f"**Cluster {cluster}:** "
        f"Average Age = {avg_age:.1f}, "
        f"Average Price per Unit = {avg_price:.2f}, "
        f"Average Transaction Amount = {avg_amount:.2f}"
    )

# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

st.markdown("---")

st.subheader("⚙️ Clustering Model Information")

st.write(
    f"**Algorithm:** K-Means Clustering"
)

st.write(
    f"**Number of Clusters:** {model_info['clusters']}"
)

st.write(
    f"**Features Used:** "
    f"{', '.join(model_info['features'])}"
)

st.write(
    f"**Silhouette Score:** "
    f"{model_info['silhouette_score']}"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Retail Market Basket Clustering | "
    "K-Means based retail transaction analysis"
)
