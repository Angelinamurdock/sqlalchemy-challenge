# Climate Analysis and API Development  
**Creator**: Angelina Murdock  
**Date**: March 2025

## Table of contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Resources](#resources)

## Overview 
This project analyzes the climate in Honolulu, Hawaii using historical weather data. It includes data exploration with **SQLAlchemy ORM** and visualization using **Pandas** and **Matplotlib**, followed by the development of a **Flask-based API** to access key climate statistics.  

## Features
1. **Climate Data Analysis**
    - Connected to a SQLite database using SQLAlchemy ORM.
    - Reflected tables and established relationships using automap.
    - Queried and analyzed 12 months of precipitation data, with results visualized in a line plot.
    - Identified the most active weather station and performed a temperature analysis for that station over the past year.
    - Created a histogram to visualize the temperature distribution.

    **Precipitation over 12 Months**
!["precip_line_chart"](SurfsUp/precip_line_chart.png)

    **Temperatures at the Most Active Station over 12 Months**
!["temps_most_active_station"](SurfsUp/temps_most_active_station.png)

2. **Flask Climate API**
    - Developed an API with Flask to serve climate data from the database.
    - Implemented the following routes:
        - /api/v1.0/precipitation – Returns the last 12 months of precipitation data.
        - /api/v1.0/stations – Returns a list of weather stations.
        - /api/v1.0/tobs – Returns temperature observations for the most active station.
        - /api/v1.0/<start> and /api/v1.0/<start>/<end> – Returns min, avg, and max temperature stats for a specified date range.

## Installation
### Requirements
- Python 3.7 or later
- Jupyter Notebook
- Flask  
- SQLAlchemy  
- SQLite  

### Setup
1. Clone or download the repository from GitHub:
    ``` bash
    git clone https://github.com/Angelinamurdock/sqlalchemy-challenge.git
    ```
2. Open the `climate_final.ipynb` for data exploration and `app.py` to run the Flask API.

## Resources
- **DU Bootcamp Module 10:** Used challenge files and class materials from the bootcamp.
- **ChatGPT:** Assisted with code explanations and debugging.