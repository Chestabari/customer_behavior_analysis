# customer_behavior_analysis

🔎 Overview
Data analytics project showcasing customer behavior analysis using Python, SQL and Power BI.
This project focuses on performing end-to-end data analytics on a customer shopping behavior dataset.

The objective was to:
- Analyze customer purchasing patterns
- Identify trends and insights
- Build an interactive Power BI dashboard
- Generate a professional analytical report and presentation
The project demonstrates skills in Python, SQL, Data Cleaning, EDA, and Data Visualization.


📁 Dataset
The dataset contains customer shopping behavior information, including:
- Customer ID
- Age
- Gender
- Item Purchased
- Category
- Purchase Amount
- Location
- Season
- Payment Method
- Review Rating
- Subscription Status
- Discount Applied
- Previous Purchases
- Frequency of Purchases
The dataset was loaded into Python and also imported into PostgreSQL/MySQL/SQL Server for SQL-based analysis.


🛠 Tools & Technologies Used
1. Python
   - Pandas
   - NumPy
   - Matplotlib
   - Seaborn

2. SQL
   - PostgreSQL
   - MySQL
   - SQL Server

3. Data Visualization
   - Power BI

4. Reporting & Presentation
    - Microsoft Word / PDF Report
    - Gamma (for PPT creation)


⚙️ Project Workflow / Steps
1️⃣ Data Loading
- Imported CSV dataset using Pandas
- Verified structure using .head(), .info(), .describe()

2️⃣ Data Cleaning
- Handled missing values
- Removed duplicates
- Standardized column names
- Converted data types
- Created new derived columns (e.g., age group, purchase frequency days)

3️⃣ Exploratory Data Analysis (EDA)
- Analyzed distribution of purchase amount
- Studied gender-wise and age-wise spending
- Identified seasonal trends
- Examined payment method usage
- Evaluated impact of discounts and subscriptions

4️⃣ SQL Analysis
- Dataset imported into:
- PostgreSQL
- MySQL
- SQL Server

Performed:
Aggregations (SUM, AVG, COUNT)
GROUP BY analysis
JOIN operations
Filtering with WHERE clauses
Ranking and sorting
Business-driven queries (Top locations, best-selling categories, etc.)

5️⃣ Dashboard Development (Power BI)
- Created an interactive dashboard including:
- KPI Cards (Total Revenue, Average Purchase, Total Customers)
- Sales by Category
- Sales by Location
- Gender Distribution
- Seasonal Trends
- Payment Method Analysis
- Filters/Slicers for dynamic exploration


📊 Dashboard Features
- Interactive filters
- Drill-down capability
- Clean and professional UI
- Business-focused KPIs
- Insight-driven visualizations
The dashboard helps stakeholders quickly understand customer behavior and revenue trends.


📈 Key Results & Insights
- Identified top-performing product categories
- Found seasonal purchasing patterns
- Determined high-revenue customer segments
- Analyzed discount impact on purchase amount
- Observed preferred payment methods
- Discovered location-based revenue trends
These insights can support business decision-making and marketing strategy improvements.


▶️ How to Run the Project

🔹 Python Analysis
~ Clone the repository
git clone <repository-link>

~ Install required libraries
pip install pandas numpy matplotlib seaborn

~ Run the Jupyter Notebook
jupyter notebook

Open the notebook and execute all cells

🔹 SQL Analysis
- Create a database in PostgreSQL / MySQL / SQL Server
- Import the dataset into a table
- Run the SQL queries provided in the /sql folder

🔹 Power BI Dashboard
- Open Power BI Desktop
- Load the dataset (or connect to SQL database)
- Open the .pbix file
- Refresh data if required


🚀 Skills Demonstrated
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis
3. SQL Query Writing
4. Database Handling
5. Business Insight Generation
6. Dashboard Design
7. Data Storytelling
8. Presentation Skills
