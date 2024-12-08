import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

# Load the dataset
df = pd.read_csv('/workspaces/solar-radiation-analysis/notebooks/benin-malanville.csv')

# Clean the data
df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB'])
for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB']:
    df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
    df[col].fillna(method='ffill', inplace=True)

# Function for summary statistics
def summary_statistics():
    st.subheader("Summary Statistics")
    stats_df = df.describe().T
    stats_df['mean'] = stats_df['mean'].round(2)
    stats_df['std'] = stats_df['std'].round(2)
    stats_df['min'] = stats_df['min'].round(2)
    stats_df['25%'] = stats_df['25%'].round(2)
    stats_df['50%'] = stats_df['50%'].round(2)
    stats_df['75%'] = stats_df['75%'].round(2)
    stats_df['max'] = stats_df['max'].round(2)
    st.write(stats_df)

# Function for Data Quality Check
def data_quality_check():
    st.subheader("Data Quality Check")

    # Missing values
    st.write("### Missing Values:")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])

    # Negative values in GHI, DNI, DHI
    st.write("### Negative Values in GHI, DNI, DHI:")
    negative_values = df[['GHI', 'DNI', 'DHI']].lt(0).sum()
    st.write(negative_values)

    # Outliers (Using IQR for ModA, ModB, WS)
    st.write("### Outlier Detection (using IQR):")
    Q1 = df[['ModA', 'ModB', 'WS']].quantile(0.25)
    Q3 = df[['ModA', 'ModB', 'WS']].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[['ModA', 'ModB', 'WS']] < (Q1 - 1.5 * IQR)) | (df[['ModA', 'ModB', 'WS']] > (Q3 + 1.5 * IQR))).sum()
    st.write(outliers)

# Function for Time Series Analysis
def time_series_analysis():
    st.subheader("Time Series Analysis")
    
    # Plot GHI, DNI, DHI over time
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Timestamp'], df['GHI'], label='GHI', color='orange')
    ax.plot(df['Timestamp'], df['DNI'], label='DNI', color='blue')
    ax.plot(df['Timestamp'], df['DHI'], label='DHI', color='green')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Irradiance (W/m²)')
    ax.set_title('Solar Irradiance over Time')
    ax.legend()
    st.pyplot(fig)

# Function for Correlation Analysis
def correlation_analysis():
    st.subheader("Correlation Analysis")
    correlation_matrix = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb']].corr()
    fig = plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    st.pyplot(fig)

# Function for Wind Analysis (Wind Rose)
def wind_analysis():
    st.subheader("Wind Analysis (Wind Rose)")
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(df['WS'], kde=True, color='purple', bins=50)
    st.pyplot(fig)

# Function for Temperature Analysis
def temperature_analysis():
    st.subheader("Temperature vs Solar Radiation (GHI)")
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Tamb'], y=df['GHI'], color='red')
    plt.title('Temperature vs Solar Radiation (GHI)')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('GHI (W/m²)')
    st.pyplot(fig)

# Function for Histograms
def create_histograms():
    st.subheader("Histograms for GHI, DNI, DHI, WS, Tamb")
    
    fig, axes = plt.subplots(3, 2, figsize=(15, 10))

    sns.histplot(df['GHI'], bins=50, kde=True, color='orange', ax=axes[0, 0])
    axes[0, 0].set_title('GHI Distribution')
    
    sns.histplot(df['DNI'], bins=50, kde=True, color='blue', ax=axes[0, 1])
    axes[0, 1].set_title('DNI Distribution')
    
    sns.histplot(df['DHI'], bins=50, kde=True, color='green', ax=axes[1, 0])
    axes[1, 0].set_title('DHI Distribution')
    
    sns.histplot(df['WS'], bins=50, kde=True, color='purple', ax=axes[1, 1])
    axes[1, 1].set_title('WS Distribution')

    sns.histplot(df['Tamb'], bins=50, kde=True, color='red', ax=axes[2, 0])
    axes[2, 0].set_title('Temperature (Tamb) Distribution')

    st.pyplot(fig)

# Function for Z-Score Analysis
def z_score_analysis():
    st.subheader("Z-Score Analysis (Outliers Detection)")
    z_scores = np.abs(stats.zscore(df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS']]))
    outliers = (z_scores > 3).sum(axis=0)
    st.write("Outliers (Z-score > 3):")
    st.write(outliers)

# Function for Bubble Chart
def bubble_chart():
    st.subheader("Bubble Chart: GHI vs Temperature vs Wind Speed")
    fig = px.scatter(df, x="GHI", y="Tamb", size="WS", color="RH", 
                     title="Bubble Chart: GHI vs Temperature vs Wind Speed",
                     labels={"GHI": "Global Horizontal Irradiance", "Tamb": "Temperature", "WS": "Wind Speed"})
    st.plotly_chart(fig)

# Function for Cleaning Impact Analysis
def cleaning_impact_analysis():
    st.subheader("Impact of Cleaning on Sensor Readings (ModA, ModB)")
    cleaned_df = df[df['Cleaning'] == 'Clean']
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(cleaned_df['Timestamp'], cleaned_df['ModA'], label='ModA Cleaned', color='orange')
    ax.plot(cleaned_df['Timestamp'], cleaned_df['ModB'], label='ModB Cleaned', color='blue')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Sensor Reading')
    ax.set_title('Impact of Cleaning on Sensor Readings')
    ax.legend()
    st.pyplot(fig)

# Streamlit app UI components
st.title("Solar and Weather Data Analysis Dashboard")

# Selectbox for different analyses
option = st.selectbox(
    'What would you like to analyze?',
    ('Summary Statistics', 'Data Quality Check', 'Time Series Analysis', 'Correlation Analysis', 
     'Wind Analysis', 'Temperature Analysis', 'Histograms', 'Z-Score Analysis', 
     'Bubble Chart', 'Impact of Cleaning on Sensor Readings')
)

# Execute corresponding analysis based on user input
if option == 'Summary Statistics':
    summary_statistics()
elif option == 'Data Quality Check':
    data_quality_check()
elif option == 'Time Series Analysis':
    time_series_analysis()
elif option == 'Correlation Analysis':
    correlation_analysis()
elif option == 'Wind Analysis':
    wind_analysis()
elif option == 'Temperature Analysis':
    temperature_analysis()
elif option == 'Histograms':
    create_histograms()
elif option == 'Z-Score Analysis':
    z_score_analysis()
elif option == 'Bubble Chart':
    bubble_chart()
else:
    cleaning_impact_analysis()

