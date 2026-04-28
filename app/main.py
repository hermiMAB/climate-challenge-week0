import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="COP32 Climate Dashboard", layout="wide")
st.title("🌍 COP32 Regional Climate Analytics")
st.markdown("Interactive dashboard exploring climate volatility across Ethiopia, Kenya, Nigeria, Sudan, and Tanzania.")

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    # Adjust this path based on where your combined CSV is stored!
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'combined_climate_data.csv')
    
    if not os.path.exists(data_path):
        st.error(f"Data file not found at {data_path}. Please ensure your CSV is in the data/ folder.")
        return pd.DataFrame()
        
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    return df

df = load_data()

if not df.empty:
    # --- 3. SIDEBAR WIDGETS (The Interactive Elements) ---
    st.sidebar.header("Filter Data")
    
    # Widget 1: Country Selector (Multi-select)
    available_countries = df['Country'].unique()
    selected_countries = st.sidebar.multiselect(
        "Select Countries", 
        options=available_countries, 
        default=available_countries
    )
    
    # Widget 2: Year Range Slider
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    selected_years = st.sidebar.slider(
        "Select Year Range", 
        min_value=min_year, 
        max_value=max_year, 
        value=(min_year, max_year)
    )
    
    # Widget 3: Variable Selector Dropdown
    variables = {
        "Temperature (°C)": "T2M",
        "Precipitation (mm)": "PRECTOTCORR",
        "Relative Humidity (%)": "RH2M"
    }
    selected_var_label = st.sidebar.selectbox("Select Variable to Plot", options=list(variables.keys()))
    selected_var_col = variables[selected_var_label]

    # --- 4. DATA FILTERING ---
    mask = (df['Country'].isin(selected_countries)) & (df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])
    filtered_df = df[mask]

    # --- 5. VISUALIZATIONS ---
    if not filtered_df.empty:
        col1, col2 = st.columns(2)
        
        # Chart 1: Trend Line Chart
        with col1:
            st.subheader(f"{selected_var_label} Trends")
            # Grouping by Year and Country for a cleaner line chart
            trend_df = filtered_df.groupby(['Year', 'Country'])[selected_var_col].mean().reset_index()
            
            fig_line, ax_line = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=trend_df, x='Year', y=selected_var_col, hue='Country', marker='o', ax=ax_line)
            ax_line.set_ylabel(selected_var_label)
            st.pyplot(fig_line)

        # Chart 2: Distribution Boxplot
        with col2:
            st.subheader(f"{selected_var_label} Distribution")
            fig_box, ax_box = plt.subplots(figsize=(10, 6))
            sns.boxplot(data=filtered_df, x='Country', y=selected_var_col, hue='Country', palette='Set2', ax=ax_box)
            ax_box.set_ylabel(selected_var_label)
            st.pyplot(fig_box)
            
    else:
        st.warning("No data matches the selected filters.")