# Brent Oil Prices Analysis

## Project Description

This project aims to analyze the impact of major political and economic events on Brent oil prices using various time series and econometric models. The project is structured into data collection, preprocessing, exploratory analysis, change point analysis, and modeling.

## Project Structure

Refer to the project structure outlined in the initial overview.

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the data collection script: `python data_collection/fred_data_collection.py`.
4. Preprocess the data: `python data_preprocessing/clean_data.py` and `python data_preprocessing/preprocess_data.py`.
5. Perform exploratory data analysis: `python analysis/exploratory_analysis.py`.
6. Conduct change point analysis: `python analysis/change_point_analysis.py`.
7. Run the ARIMA model: `python modeling/arima_model.py`.
8. Run the GARCH model: `python modeling/garch_model.py`.
9. Plot the forecast results: `python visualization/plot_results.py`.
10. Generate insights: `python visualization/insights.py`.


.
├── Code
│   ├── analysis
│   ├── data_collection
│   ├── data_preprocessing
│   ├── modeling
│   └── visualization
├── Inputs
│   └── data
├── Metadata
│   ├── project_description.md
│   └── README.md
├── Notebook
│   ├── arima_model.ipynb
│   ├── data_preprocessing.ipynb
│   ├── EDA.ipynb
│   ├── exploratory_analysis.ipynb
│   └── garch_model.ipynb
├── README.md
├── requirements.txt
├── Results
│   ├── arima
│   ├── bocpd
│   ├── bsts
│   ├── extended_model
│   ├── garch
│   ├── model_validation
│   ├── ms_arima
│   ├── rulsif
│   └── var
└── Scripts
    ├── run_all.sh
    └── setup_env.sh


    workflow 
    
    +-------------------+        +-------------------+        +-------------------+
|    Data           |        |    Data           |        |    Exploratory    |
|    Collection     +------->|    Preprocessing  +------->|    Data Analysis  |
+-------------------+        +-------------------+        +-------------------+
         |                           |                           |
         v                           v                           v
+-------------------+        +-------------------+        +-------------------+
|  Model Building   |        |  Factor Analysis  |        |  Model Validation |
+-------------------+        +-------------------+        +-------------------+
         |                           |                           |
         v                           v                           v
+-------------------+        +-------------------+        +-------------------+
|  Adapt Model to   |        |  Extend Model with|        |  Generate         |
|  New Scenarios    +------->|  New Variables    +------->|  Insights         |
+-------------------+        +-------------------+        +-------------------+
