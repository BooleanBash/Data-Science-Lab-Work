# Comparative Climate Change Analysis of India, USA, and China Using Machine Learning

## Description
This project performs a comparative analysis of climate change across three of the world's
largest economies — India, the United States, and China. Using a synthetic training dataset
of 1,200 rows and 20 features spanning 1980 to 2025, the project explores how temperature,
CO2 concentration, fossil fuel consumption, renewable energy adoption, and other environmental
indicators differ across the three countries. The workflow covers data cleaning, exploratory
data analysis, visualization, and linear regression modeling.

## Dataset
- Source: Kaggle — Beginner Climate Change Dataset (20 Features, 1200 Rows)
- Note: This is a synthetically generated training dataset created for beginner data science
  practice. It is not sourced from real-world climate observations, which is reflected in the
  near-zero feature correlations observed during the modeling phase.
- Rows: 1,200
- Features: 20 (including temperature, CO2 concentration, rainfall, sea level rise,
  heatwave days, fossil fuel consumption, renewable energy share, air quality index,
  climate risk index, and more)
- Countries in full dataset: Australia, Brazil, Canada, China, France, Germany,
  India, Pakistan, UK, USA
- Countries used in this project: India, USA, China

## Steps Performed
1. Data Cleaning
   - Checked for missing values — none found
   - Checked for duplicate rows — none found
   - Enforced correct data types for all columns
   - Normalized country name variants (e.g., 'USA' vs 'United States')
   - Filtered dataset to retain only India, USA, and China (373 rows)

2. Exploratory Data Analysis
   - Reviewed .info() and .describe() for structure and distributions
   - Checked unique countries, year range, and record counts per country
   - Computed Pearson correlation matrix across all numerical features
   - Confirmed near-zero correlations between all features and target variable,
     identifying the synthetic nature of the dataset

3. Visualization
   - Line plot: Year vs Average Temperature for all three countries
   - Line plot: CO2 concentration over time with a 400 ppm reference line
   - Scatter plot: CO2 vs Temperature with per-country trend lines
   - Correlation heatmap of all numerical features (lower triangle)
   - Box plots: Temperature, CO2, and renewable energy share by country
   - Scatter plot: Fossil fuel consumption vs renewable energy share
   - Normalized grouped bar chart: 5 key indicators compared across three countries

4. Model Building
   - Algorithm: Linear Regression (scikit-learn)
   - Target variable: global_avg_temperature
   - Features used: co2_concentration_ppm, sea_surface_temperature, heatwave_days,
     fossil_fuel_consumption, renewable_energy_share, air_quality_index, annual_rainfall_mm
   - Train-test split: 80% training / 20% testing (random_state=42)
   - Feature scaling: StandardScaler (Z-score normalization) applied before fitting
   - Statistical methods: descriptive statistics (mean, std, min/max), Pearson correlation
     analysis, train-test splitting, Z-score scaling, Linear Regression, MSE, RMSE, R²

## Results
- Key findings:
  - A general upward temperature trend from 1980 to 2025 is shown by all three countries
  - Temperature and CO2 show no meaningful correlation in this dataset (r = -0.025), which is
    consistent with the synthetic nature of the data
  - The USA shows the highest average fossil fuel consumption across the observed period
  - The fastest growth is shown by China, in renewable energy adoption in the recent years.
  - India demonstrated the widest temperature variability due to its diverse climate zones
  - Renewable energy growth has not produced a measurable decline in CO2 levels
    within this dataset, reflecting the energy addition phenomenon


- Metrics:
  - Mean Squared Error (MSE) : 0.3871
  - Root Mean Squared Error  : 0.6222 °C
  - R² Score                 : -0.0182
  - The negative R² confirms the model performs worse than a simple mean baseline,
    which is expected given the synthetic dataset — not a modeling error

## Tools Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook (.ipynb)

## Conclusion

As the dataset is a practice dataset generated with no real statistical relation between
Features and the target variable, the regression model produced a negative R² (-0.0182). 
Recognizing and explaining this outcome is itself a valid and important analytical finding — 
a good data scientist identifies when a model cannot perform well and explains why, rather 
than forcing misleading results.

In a real-world climate dataset, CO2 concentration and temperature would show strong
positive correlation, and a regression model would produce meaningful predictions.
This project successfully demonstrates the full workflow and the critical thinking
required to interpret results honestly.

## Author
Jay Tripathy
