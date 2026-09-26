```python
import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Shopping Behavior Analysis",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("customer_shopping_behavior.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns
    df["Purchase Amount (USD)"] = pd.to_numeric(
        df["Purchase Amount (USD)"],
        errors="coerce"
    )

    df["Review Rating"] = pd.to_numeric(
        df["Review Rating"],
        errors="coerce"
    )

    df["Age"] = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )

    df["Previous Purchases"] = pd.to_numeric(
        df["Previous Purchases"],
        errors="coerce"
    )

    return df


df = load_data()

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🛍️ Customer Shopping Behavior Analysis")

st.markdown(
    """
    An interactive dashboard built using **Python, Pandas, Plotly and Streamlit**
    to explore customer purchasing behavior and shopping patterns.
    """
)

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Filters")

# Category
categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

# Gender
genders = sorted(df["Gender"].dropna().unique())

selected_genders = st.sidebar.multiselect(
    "Gender",
    genders,
    default=genders
)

# Season
seasons = sorted(df["Season"].dropna().unique())

selected_seasons = st.sidebar.multiselect(
    "Season",
    seasons,
    default=seasons
)

# Subscription
subscriptions = sorted(
    df["Subscription Status"].dropna().unique()
)

selected_subscriptions = st.sidebar.multiselect(
    "Subscription Status",
    subscriptions,
    default=subscriptions
)

# Location
locations = sorted(df["Location"].dropna().unique())

selected_locations = st.sidebar.multiselect(
    "Location",
    locations,
    default=locations
)

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df[
    df["Category"].isin(selected_categories)
    & df["Gender"].isin(selected_genders)
    & df["Season"].isin(selected_seasons)
    & df["Subscription Status"].isin(selected_subscriptions)
    & df["Location"].isin(selected_locations)
]

# --------------------------------------------------
# Check Filter Result
# --------------------------------------------------

if filtered_df.empty:

    st.warning(
        "No data available for the selected filters. "
        "Please change your filter selection."
    )

    st.stop()

# --------------------------------------------------
# KPI Calculations
# --------------------------------------------------

total_customers = filtered_df["Customer ID"].nunique()

total_purchase = filtered_df["Purchase Amount (USD)"].sum()

average_purchase = filtered_df["Purchase Amount (USD)"].mean()

average_rating = filtered_df["Review Rating"].mean()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "💰 Total Purchase",
        f"${total_purchase:,.0f}"
    )

with col3:
    st.metric(
        "🛒 Average Purchase",
        f"${average_purchase:,.2f}"
    )

with col4:
    st.metric(
        "⭐ Average Rating",
        f"{average_rating:.2f}"
    )

st.divider()

# --------------------------------------------------
# Category Analysis
# --------------------------------------------------

st.subheader("📊 Purchase Amount by Category")

category_data = (
    filtered_df
    .groupby("Category", as_index=False)["Purchase Amount (USD)"]
    .sum()
    .sort_values("Purchase Amount (USD)", ascending=False)
)

fig_category = px.bar(
    category_data,
    x="Category",
    y="Purchase Amount (USD)",
    text_auto=".2s",
    title="Purchase Amount by Category"
)

fig_category.update_layout(
    xaxis_title="Category",
    yaxis_title="Purchase Amount (USD)",
    showlegend=False
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# --------------------------------------------------
# Product Analysis
# --------------------------------------------------

st.subheader("🛍️ Product Performance")

product_data = (
    filtered_df
    .groupby("Item Purchased", as_index=False)["Purchase Amount (USD)"]
    .sum()
    .sort_values("Purchase Amount (USD)", ascending=False)
    .head(10)
)

fig_product = px.bar(
    product_data,
    x="Purchase Amount (USD)",
    y="Item Purchased",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Products by Purchase Amount"
)

fig_product.update_layout(
    yaxis_title="Product",
    xaxis_title="Purchase Amount (USD)"
)

st.plotly_chart(
    fig_product,
    use_container_width=True
)

# --------------------------------------------------
# Season Analysis
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    season_data = (
        filtered_df
        .groupby("Season", as_index=False)["Purchase Amount (USD)"]
        .sum()
    )

    fig_season = px.bar(
        season_data,
        x="Season",
        y="Purchase Amount (USD)",
        title="Purchase Amount by Season",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_season,
        use_container_width=True
    )

# --------------------------------------------------
# Gender Analysis
# --------------------------------------------------

with col2:

    gender_data = (
        filtered_df
        .groupby("Gender", as_index=False)["Purchase Amount (USD)"]
        .sum()
    )

    fig_gender = px.pie(
        gender_data,
        names="Gender",
        values="Purchase Amount (USD)",
        title="Purchase Amount by Gender",
        hole=0.4
    )

    st.plotly_chart(
        fig_gender,
        use_container_width=True
    )

# --------------------------------------------------
# Payment Method
# --------------------------------------------------

st.subheader("💳 Payment Method Analysis")

payment_data = (
    filtered_df
    .groupby("Payment Method", as_index=False)
    .agg(
        Total_Purchase=("Purchase Amount (USD)", "sum"),
        Customers=("Customer ID", "nunique")
    )
    .sort_values(
        "Total_Purchase",
        ascending=False
    )
)

fig_payment = px.bar(
    payment_data,
    x="Payment Method",
    y="Total_Purchase",
    text_auto=".2s",
    title="Purchase Amount by Payment Method"
)

fig_payment.update_layout(
    xaxis_title="Payment Method",
    yaxis_title="Purchase Amount (USD)"
)

st.plotly_chart(
    fig_payment,
    use_container_width=True
)

# --------------------------------------------------
# Subscription Analysis
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    subscription_data = (
        filtered_df["Subscription Status"]
        .value_counts()
        .reset_index()
    )

    subscription_data.columns = [
        "Subscription Status",
        "Customers"
    ]

    fig_subscription = px.pie(
        subscription_data,
        names="Subscription Status",
        values="Customers",
        title="Subscription Status",
        hole=0.4
    )

    st.plotly_chart(
        fig_subscription,
        use_container_width=True
    )

# --------------------------------------------------
# Discount Analysis
# --------------------------------------------------

with col2:

    discount_data = (
        filtered_df["Discount Applied"]
        .value_counts()
        .reset_index()
    )

    discount_data.columns = [
        "Discount Applied",
        "Customers"
    ]

    fig_discount = px.bar(
        discount_data,
        x="Discount Applied",
        y="Customers",
        text_auto=True,
        title="Discount Applied"
    )

    fig_discount.update_layout(
        xaxis_title="Discount Applied",
        yaxis_title="Number of Customers"
    )

    st.plotly_chart(
        fig_discount,
        use_container_width=True
    )

# --------------------------------------------------
# Location Analysis
# --------------------------------------------------

st.subheader("📍 Purchase Amount by Location")

location_data = (
    filtered_df
    .groupby("Location", as_index=False)["Purchase Amount (USD)"]
    .sum()
    .sort_values(
        "Purchase Amount (USD)",
        ascending=False
    )
    .head(15)
)

fig_location = px.bar(
    location_data,
    x="Purchase Amount (USD)",
    y="Location",
    orientation="h",
    text_auto=".2s",
    title="Top 15 Locations by Purchase Amount"
)

fig_location.update_layout(
    xaxis_title="Purchase Amount (USD)",
    yaxis_title="Location"
)

st.plotly_chart(
    fig_location,
    use_container_width=True
)

# --------------------------------------------------
# Purchase Frequency
# --------------------------------------------------

st.subheader("🔁 Purchase Frequency")

frequency_data = (
    filtered_df["Frequency of Purchases"]
    .value_counts()
    .reset_index()
)

frequency_data.columns = [
    "Frequency of Purchases",
    "Customers"
]

fig_frequency = px.bar(
    frequency_data,
    x="Frequency of Purchases",
    y="Customers",
    text_auto=True,
    title="Customer Purchase Frequency"
)

fig_frequency.update_layout(
    xaxis_title="Purchase Frequency",
    yaxis_title="Number of Customers"
)

st.plotly_chart(
    fig_frequency,
    use_container_width=True
)

# --------------------------------------------------
# Customer Data
# --------------------------------------------------

with st.expander("📋 View Customer Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Customer Shopping Behavior Analysis | "
    "Python • PostgreSQL • Power BI • Streamlit"
)
```

### Then create `requirements.txt`

Create another file in the same GitHub repository called **`requirements.txt`**:

```text
streamlit
pandas
plotly
```

### Your GitHub structure will become

```text
customer_behavior_analysis/
│
├── app.py                         ← NEW
├── requirements.txt               ← NEW
├── customer_shopping_behavior.csv
├── customer_behavior_python_powerbi.ipynb
├── customer_behavior_postgressql.sql
├── customer_behavior_dashboard.pbix
├── README.md
└── ...
```

### Then deploy it

Once both files are on GitHub:

1. Go to **Streamlit Community Cloud**.
2. Sign in with GitHub.
3. Click **Create app**.
4. Select your repository:
   `Chestabari/customer_behavior_analysis`
5. Select branch: **`main`**
6. For the main file, enter:
   **`app.py`**
7. Click **Deploy**.

Streamlit Community Cloud supports deploying apps directly from GitHub repositories.

You'll get a URL similar to:

```text
https://customer-behavior-analysis.streamlit.app
```

You can then put that link in your **resume, LinkedIn, and GitHub README**.

**One thing to note:** this Streamlit version is a Python recreation of your Power BI dashboard. Your original `.pbix` should stay in the repository because it demonstrates your Power BI work; the Streamlit app gives the interviewer a convenient browser-based interactive version.
