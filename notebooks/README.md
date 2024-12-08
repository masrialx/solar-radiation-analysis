# 🌞 **Solar Irradiance and Weather Data Analysis** 📊

## **Introduction**

This repository contains an in-depth **Exploratory Data Analysis (EDA)** of solar irradiance and weather data collected from **Malanville, Benin** (Latitude: **11.00° N**, Longitude: **3.25° E**). The analysis focuses on understanding patterns, assessing data quality, and visualizing trends in solar energy parameters such as **Global Horizontal Irradiance (GHI)**, **Direct Normal Irradiance (DNI)**, and **Diffuse Horizontal Irradiance (DHI)**. This project aims to support renewable energy research and weather forecasting applications.

---

## **Table of Contents**

1. [Features](#features)  
2. [Dataset](#dataset)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Visualization Examples](#visualization-examples)  
7. [Folder Structure](#folder-structure)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## **Features**

- ✅ **Data Cleaning**: Handling missing values and replacing negative entries.  
- ✅ **Time Series Analysis**: Visualizing daily and seasonal trends of solar irradiance.  
- ✅ **Correlation Analysis**: Exploring relationships between temperature, wind, and irradiance.  
- ✅ **Wind Analysis**: Wind speed and direction insights using wind rose plots.  
- ✅ **Statistical Summaries**: Descriptive statistics and Z-score outlier detection.  
- ✅ **Visualizations**: Detailed plots to support findings.  

---

## **Dataset**

- **File**: `benin-malanville.csv`  
- **Rows**: 525,600  
- **Columns**: 19  

### **Key Columns**

| **Column**  | **Description**                           |  
|-------------|-------------------------------------------|  
| `Timestamp` | Time of data collection                  |  
| `GHI`       | Global Horizontal Irradiance (W/m²)      |  
| `DNI`       | Direct Normal Irradiance (W/m²)          |  
| `DHI`       | Diffuse Horizontal Irradiance (W/m²)     |  
| `Tamb`      | Ambient Temperature (°C)                 |  
| `WS`        | Wind Speed (m/s)                         |  
| `RH`        | Relative Humidity (%)                    |  

---

## **Requirements**

To run the analysis, ensure you have the following packages installed:

```bash
pandas==2.0.3  
numpy==1.23.5  
matplotlib==3.5.1  
seaborn==0.11.2  
plotly==5.1.0  
jupyterlab==3.2.1  
```

---

## **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/masrialx/solar-eda.git  
   cd solar-eda  
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt  
   ```

---

## **Usage**

1. **Launch Jupyter Notebook**

   ```bash
   jupyter lab  
   ```

2. **Open the EDA Notebook**  

   In your browser, navigate to `eda.ipynb` to explore the analysis step-by-step.

---

## **Visualization Examples**

### **1. Solar Irradiance Trends**

![Solar Irradiance](path/to/ghi_dni_dhi_timeseries.png)  

### **2. Correlation Matrix**

![Correlation Matrix](path/to/correlation_matrix.png)  

### **3. Wind Rose Plot**

![Wind Rose](path/to/wind_rose.png)  

---

## **Folder Structure**

```plaintext
solar-eda/  
│  
├── data/  
│   └── benin-malanville.csv  
│  
├── eda.ipynb  
├── requirements.txt  
└── README.md  
```

---

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.  
2. Create a new branch: `git checkout -b my-feature`.  
3. Commit your changes: `git commit -m "Add my feature"`.  
4. Push to the branch: `git push origin my-feature`.  
5. Submit a pull request.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

🚀 **Happy Analyzing!** 🌞

