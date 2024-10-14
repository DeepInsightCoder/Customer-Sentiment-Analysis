
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Sentiment-based pricing function
def adjust_price(original_price, sentiment_score):
    if sentiment_score == 1:  # Positive Sentiment
        return original_price * 1.10  # Increase price by 10%
    elif sentiment_score == -1:  # Negative Sentiment
        return original_price * 0.90  # Decrease price by 10%
    else:  # Neutral Sentiment
        return original_price  # Keep the price the same

# Title for the web app
st.title("Sentiment-Based Dynamic Pricing")

# Function to show progress
def show_progress():
    progress_bar = st.progress(0)
    
    # Step 1: Waiting for user to upload file
    for i in range(1, 5):
        time.sleep(1)  # Simulate time-consuming task
        progress_bar.progress(i / 4)  # Update progress bar

    # Step 2: File uploaded
    st.success("File uploaded! Processing the data...")
    time.sleep(1)
    progress_bar.progress(2 / 4)  # Update progress bar

    # Step 3: Adjusting prices
    st.info("Adjusting prices based on sentiment...")
    time.sleep(1)
    progress_bar.progress(3 / 4)  # Update progress bar

    # Final step
    st.success("Pricing adjustments complete!")
    progress_bar.progress(1.0)  # Complete the progress bar

# File upload option for users to upload sentiment data
uploaded_file = st.file_uploader("Upload Sentiment Data CSV", type=["csv"])

if uploaded_file is not None:
    # Load the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    st.write("Uploaded Sentiment Data:")
    st.write(data.head())  # Display first few rows

    # Call progress function
    show_progress()

    # Ask user for original price input
    st.subheader("Input Product Prices")

    original_prices = []
    product_names = list(data['Product'])  # Assuming 'Product' column in data
    for product in product_names:
        price = st.number_input(f"Enter original price for {product}", min_value=0.0, step=0.01)
        original_prices.append(price)

    # Adjust pricing based on sentiment score
    sentiment_scores = data['Sentiment']  # Assuming 'Sentiment' column in data
    adjusted_prices = [adjust_price(price, sentiment) for price, sentiment in zip(original_prices, sentiment_scores)]

    # Show adjusted prices
    st.subheader("Adjusted Prices Based on Sentiment")
    for product, adj_price in zip(product_names, adjusted_prices):
        st.write(f"New price for {product}: ${adj_price:.2f}")

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(product_names, original_prices, label='Original Price', alpha=0.5)
    ax.bar(product_names, adjusted_prices, label='Adjusted Price', alpha=0.5)
    ax.set_ylabel('Price')
    ax.set_title('Price Adjustments Based on Sentiment')
    ax.legend()
    st.pyplot(fig)

# Add a button to run the pricing adjustment
if st.button("Generate Pricing Recommendations"):
    st.success("Pricing adjustments complete!")
