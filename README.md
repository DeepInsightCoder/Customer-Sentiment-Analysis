# Customer Sentiment Analysis for Custom Pricing Models

## Project Overview
This project aims to analyze customer sentiment data from various sources to develop insights that can inform dynamic pricing models. By identifying trends in customer feedback, businesses can adjust their pricing strategies to better meet customer expectations and enhance sales.

## Data Sources
The following datasets will be utilized in this project:
- **Twitter Scraping Tweets Dataset**: Sentiment data from user-generated tweets regarding pricing.
- **Trustpilot Reviews Data**: Customer feedback related to product pricing and quality.
- **Amazon Reviews**: Customer reviews and ratings for various products, focusing on pricing aspects.
- **Sentiment140**: Pre-existing sentiment analysis dataset, providing insights into customer sentiments.
- **Product Rating Datasets**: Data containing ratings and reviews that provide insights into customer satisfaction and pricing perception.
  
## How to use the data

Download the zipped CSV file and extract it using a tool like `unzip` or `WinRAR`:
## Objectives

- Analyze customer sentiment data across multiple platforms.
- Develop insights into how sentiment impacts pricing models.
- Implement a comparison of different sentiment analysis models to identify the most effective one.
- Create a Streamlit web app to visualize sentiment analysis results and provide an interactive experience.

## Methodology
1. **Data Collection**: Gather data from the above-mentioned sources.
2. **Data Preprocessing**: Clean and prepare the data for analysis.
3. **Sentiment Analysis**: Use various sentiment analysis techniques to classify customer feedback.
4. **Model Comparison**: Evaluate multiple models to identify the best performing one.
5. **Visualization**: Use Streamlit to develop a web app that presents findings and insights in an interactive format.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, TextBlob, VADER, Tweepy, BeautifulSoup, praw, Streamlit
- **Data Visualization**: Matplotlib, Seaborn

## Instructions for Running the Project
1. Clone the repository:https://github.com/DeepInsightCoder/Customer-Sentiment-Analysis.git
2. Install the necessary libraries:pip install pandas numpy scikit-learn nltk matplotlib seaborn.
3. pip install -r requirements.txt
4. streamlit run Dynamic_Pricing_App.py
   
**App Url**:https://customer-sentiment-analysis-uefgaxrq9sxdbftcsfxzji.streamlit.app/

## Results
The project achieved an accuracy of 98% using logistic regression on the sentiment data.

This reflects the model's performance in predicting customer sentiment based on pricing feedback.






