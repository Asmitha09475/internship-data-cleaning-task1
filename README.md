## Task 1: Data Cleaning and Preprocessing(Netflix Movies and TV Shows) :-

## Project Overview :-
This project performs end-to-end data cleaning and exploratory data analysis (EDA) on the Netflix Movies & TV Shows dataset. The goal is to demonstrate proficiency in data preprocessing, handling missing values, feature engineering, and visualizing insights.

## Dataset :-
Source: Kaggle "Netflix Movies and TV Shows" dataset
Location: data/raw/netflix_titles.csv

## Setup & Installation :-

1)Create and activate a virtual environment :-
-> python -m venv venv
-> .\venv\Scripts\Activate.ps1

2)Install dependencies :-
-> pip install -r requirements.txt

## Data Cleaning :-

Run the cleaning script to process the raw dataset and generate a cleaned CSV:
-> python scripts\data_cleaning.py

This script will:
Parse and standardize date_added to datetime
Forward/back-fill and drop remaining missing dates and durations
Impute missing director, cast, country, and rating with "Unknown"
Extract duration_int (numeric) and duration_unit (min/Seasons)
Remove duplicate rows
Standardize text columns to Title Case
Rename column headers to lowercase with underscores
Save diagnostics plot (missing_values.png) and output cleaned data to data/cleaned/netflix_cleaned.csv

## Exploratory Data Analysis :-

After cleaning, run the EDA script:-
-> python scripts\eda.py

This will produce four key charts:-
Missing Values Diagnostic (missing_values.png)
Duration Distribution (duration_histogram.png)
Top 10 Countries by Number of Shows (top_countries.png)
Shows Added Per Year (shows_per_year.png)

## Dependencies :-

pandas >= 1.3
matplotlib >= 3.4