# Sentiment-Based Dynamic Pricing App

## Overview
This Streamlit app allows users to upload a CSV file containing product information and customer sentiment data. Based on the sentiment, the app adjusts product prices dynamically to optimize sales. It is designed to be user-friendly, enabling businesses to enhance their pricing strategies based on customer feedback.

## Features
- **Upload CSV File:** Users can upload a CSV file containing product names, prices, and sentiment scores.
- **Dynamic Pricing Adjustment:** Prices are adjusted based on customer sentiment:
  - Positive sentiment increases prices by 10%.
  - Negative sentiment decreases prices by 10%.
  - Neutral sentiment keeps prices the same.
- **Data Preview:** Users can view the uploaded data and adjusted prices.
- **Download Adjusted Pricing:** Users can download the adjusted pricing as a new CSV file.

## Requirements
To run this app, ensure you have the following installed:
- Python 3.7 or higher
- Streamlit
- Pandas

## Usage
Clone this repository to your local machine or download the files.

Navigate to the directory where the streamlit_app.py file is located.

 Run the Streamlit app using the following command: streamlit run streamlit_app.py

Open your web browser and go to the URL provided in the terminal

 Upload your CSV file with the following columns:

Product: The name of the product.
Price: The original price of the product.
Sentiment: The sentiment score (-1 for negative, 0 for neutral, 1 for positive).
View the adjusted prices and download the results.

