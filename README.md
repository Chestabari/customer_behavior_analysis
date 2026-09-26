# Customer Shopping Behavior Analysis

An end-to-end data analytics project analyzing customer shopping behavior using Python, PostgreSQL, Power BI, and Streamlit.

The project focuses on customer purchasing patterns, product categories, discounts, payment methods, subscriptions, locations, and other shopping trends.

## Business Objective

The main goal of this project was to analyze customer shopping data, identify useful patterns, and generate insights that can support data-driven business decisions.

## Tools & Technologies

* **Python** – Pandas, NumPy, Matplotlib
* **PostgreSQL** – SQL queries and data analysis
* **Power BI** – Dashboard and data visualization
* **Streamlit** – Interactive web dashboard
* **Plotly** – Interactive charts and visualizations

## Project Workflow

Raw Customer Data
        ↓
Python / Pandas
Data Cleaning & Analysis
        ↓
PostgreSQL
SQL Business Analysis
        ↓
Power BI & Streamlit
Dashboard & Visualization
        ↓
Business Insights

## Python Analysis

Python was used to clean, preprocess, and explore the customer shopping dataset.

Main activities included:

* Loading and exploring the dataset
* Checking missing values and duplicate records
* Cleaning and standardizing the data
* Converting data types
* Creating additional features for analysis
* Performing exploratory data analysis
* Analyzing customer purchasing patterns

## SQL Analysis

PostgreSQL was used to perform business-focused analysis and answer different questions related to customer behavior and sales.

The analysis included:

* Customer segmentation
* Product and category performance
* Customer purchasing trends
* Payment methods
* Discounts and subscriptions
* Location-based analysis

## Dashboard

The project includes both a Power BI dashboard and a Streamlit dashboard.

### 🌐 Live Interactive Dashboard

[View Live Streamlit Dashboard](https://customerbehavioranalysis-czqebs3ycqoh9co6knmp4k.streamlit.app/)

### 📊 Power BI Dashboard

The Power BI dashboard provides interactive KPIs and visualizations to explore customer behavior, sales patterns, categories, locations, payment methods, and other business metrics.

![Power BI Dashboard](dashboard.png)

### Dashboard Features

* Total customers and purchase KPIs
* Category analysis
* Product performance
* Location analysis
* Seasonal trends
* Payment method analysis
* Subscription analysis
* Discount analysis
* Customer purchase frequency
* Interactive filters and slicers

## Key Insights

The analysis helped identify:

* Customer purchasing patterns across different categories
* Top-performing products and categories
* Seasonal changes in purchasing behavior
* Popular payment methods
* Discount and subscription patterns
* Differences in purchasing behavior by location

## Business Recommendations

Based on the analysis:

* Focus on categories with higher customer demand
* Use customer behavior to plan targeted promotions
* Review discount strategies based on purchasing patterns
* Consider seasonal trends while planning sales
* Use customer segments for more focused marketing

## Project Structure

```text
customer_behavior_analysis/
│
├── app.py
├── requirements.txt
├── customer_shopping_behavior.csv
├── customer_behavior_python_powerbi.ipynb
├── customer_behavior_postgressql.sql
├── customer_behavior_dashboard.pbix
├── Business Problem Document.pdf
├── Customer Shopping Behavior Analysis Report.pdf
├── customer_behavior_PPT.pdf
└── README.md
```

## How to Run

### Python

1. Clone the repository.
2. Install the required Python libraries.
3. Open the Jupyter Notebook.
4. Run the notebook cells.

### PostgreSQL

1. Create a PostgreSQL database.
2. Import the customer shopping dataset.
3. Run the SQL queries provided in the project.

### Power BI

1. Open the `.pbix` file in Power BI Desktop.
2. Refresh the data if required.
3. Explore the dashboard and visualizations.

### Streamlit

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

The live version of the dashboard is also available here:

[View Live Streamlit Dashboard](https://customerbehavioranalysis-czqebs3ycqoh9co6knmp4k.streamlit.app/)

## Skills Demonstrated

* Python
* Pandas
* NumPy
* SQL
* PostgreSQL
* Power BI
* Streamlit
* Plotly
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Business Analysis
* Dashboard Development
* Business Insights

