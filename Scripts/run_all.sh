#!/bin/bash
python data_collection/fred_data_collection.py
python data_preprocessing/clean_data.py
python data_preprocessing/preprocess_data.py
python analysis/exploratory_analysis.py
python analysis/change_point_analysis.py
python modeling/arima_model.py
python modeling/garch_model.py
python visualization/plot_results.py
python visualization/insights.py
