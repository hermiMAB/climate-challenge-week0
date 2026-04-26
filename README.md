# 🌍 COP32 African Climate Data Analysis (Week 0)

## 📌 Project Overview
This project explores daily climate data for five African countries: **Ethiopia, Kenya, Nigeria, Sudan, and Tanzania**. The goal is to analyze temperature, rainfall, wind, and humidity patterns from 2015 to 2026 to help understand regional climate trends for the upcoming COP32 climate conference.

## 🗂️ Folder Structure
* `data/`: Contains the raw and cleaned `.csv` data files. *(Note: CSV files are ignored by git to save space).*
* `notebooks/`: Contains the Jupyter Notebooks for each country's Exploratory Data Analysis (EDA).
* `src/`: (If applicable) Contains reusable Python scripts.
* `README.md`: Project documentation.
* `.gitignore`: Ensures large data files are not pushed to GitHub.

## 🧹 Data Cleaning & Outlier Strategy
We used data from the **NASA POWER** database. During the cleaning process:
1. **Missing Values:** NASA uses `-999.00` to mark missing data. We successfully found and replaced these with `NaN` (blank) values to keep our math accurate.
2. **Outliers (Z-Score):** We used a Z-score check to find extreme weather days. We discovered rare, massive rainstorms (like a 166mm drop in Nigeria) and extreme temperature swings. 
3. **Decision:** We chose to **keep** all extreme weather outliers because they represent real, critical climate events (like tropical storms and desert flash floods) that are important for the COP32 report.

## 📊 Exploratory Data Analysis (EDA) Highlights
For each of the five countries, we created four main visual reports:
1. **Temperature Timeline (Line Chart):** Shows the yearly wave of hot and cold seasons over 11 years.
2. **Rainfall Patterns (Bar Chart):** Identifies the peak rainy seasons and dry months for each region.
3. **Variable Links (Heatmap & Scatter Plots):** Shows how heat, humidity, and wind affect each other.
4. **Climate Recipe (Bubble Chart):** Combines temperature, humidity, and rain size into one chart to show exactly what weather mix creates a heavy storm.

## 🚀 How to Run the Notebooks
1. Clone this repository to your local machine.
2. Ensure you have the required climate `.csv` files inside the `data/` folder.
3. Install the required Python libraries (Pandas, NumPy, Matplotlib, Seaborn, SciPy).
4. Open the `notebooks/` folder and run the `_eda.ipynb` files in Jupyter or VS Code.

## 📚 References
* NASA POWER Data Access Viewer (for understanding the `-999` sentinel values).
* Pandas Documentation (for `%Y%j` date parsing and time-series resampling logic).
