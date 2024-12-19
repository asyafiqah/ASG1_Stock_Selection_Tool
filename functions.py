import yfinance as yf
import pandas as pd
import os

users = {}  # A simple in-memory user storage (username/password pairs)

def register_user(email, password):
    """Register User"""
    users[email] = password

def authenticate_user(email, password):
    """Authenticate User Credentials to Login"""
    return users.get(email) == password

def fetch_closing_prices(ticker, start_date, end_date):
    """Fetch closing prices for a given stock ticker within a specific date range."""
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close'] if 'Close' in stock_data.columns else None

def analyze_closing_prices(stock_data):
    """Perform analysis on the closing prices."""
    average_price = stock_data.mean()
    percentage_change = ((stock_data.iloc[-1] - stock_data.iloc[0]) / stock_data.iloc[0]) * 100
    highest_price = stock_data.max()
    lowest_price = stock_data.min()
    return {
        'Average': average_price,
        'Percentage_Change': percentage_change,
        'Highest': highest_price,
        'Lowest': lowest_price
    }

def save_user_data(email, ticker, analysis_result, filename='user_data.csv'):
    """Save user data to a CSV file."""
    data = {
        'Email': email,
        'Ticker': ticker,
        'Average': analysis_result['Average'],
        'Percentage_Change': analysis_result['Percentage_Change'],
        'Highest': analysis_result['Highest'],
        'Lowest': analysis_result['Lowest'],
    }
    
    if not os.path.isfile(filename):
        df = pd.DataFrame(columns=data.keys())
    else:
        df = pd.read_csv(filename)
    
    new_data = pd.DataFrame([data])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(filename, index=False)

def read_user_data(filename='user_data.csv'):
    """Read and display user data from a CSV file."""
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        print(df)
    else:
        print("No data found.")
