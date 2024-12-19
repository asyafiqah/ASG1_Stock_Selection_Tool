# ASG1_STOCK_SELECTION_TOOL

This project is a **Stock Selection Tool** built with Python to analyze closing prices of stocks in the Malaysian market using **YFinance** for historical stock data and **Pandas** for data manipulation. The tool allows user registration, stock price analysis, and record-keeping for future reference. Below are instructions on setting up, running, and using the application.

---

## Features
- **User Registration and Login**: Secure login with email and password.
- **Fetch Stock Data**: Users can retrieve historical closing prices of stocks for a specific period.
- **Data Analysis**: Perform basic analysis on closing prices:
  - Calculate the average closing price.
  - Determine percentage change between the first and last closing prices.
  - Identify the highest and lowest closing prices in the selected period.
- **Data Storage**: Save user details, stock tickers, and analysis results to a CSV file.
- **Data Access**: Users can view previously stored data.

---

## Requirements
Ensure the following are installed on your system:
1. Python 3.7 or higher
2. Libraries:
   - **YFinance**
   - **Pandas**

---

## Setup Instructions

### 1. Clone the Repository
Download or clone the project files into your local system.
```bash
# Clone the repository
git clone https://github.com/username/stock-selection-tool.git
cd stock-selection-tool
```

### 2. Install Python Libraries
Install the required dependencies:
```bash
pip install yfinance pandas
```

### 3. Configure the Environment
- Ensure the CSV file (`user_data.csv`) for storing user interactions is created in the same directory.
- (Optional) Use a virtual environment to manage dependencies.
  ```bash
  python -m venv venv
  source venv/bin/activate   # Activate for macOS/Linux
  .\venv\Scripts\activate  # Activate for Windows
  ```

---

## How to Run

### 1. Start the Program
Run the `main.py` file from the terminal.
```bash
python main.py
```

### 2. Follow the Menu Options
The program offers a simple menu-driven interface:
- **1. Register**: Create a new user account.
- **2. Login**: Log in to an existing account.
- **3. Exit**: Exit the program.

---

## User Guide

### **1. Register and Login**
- Select **"Register"** to create an account with your email and password.
- Log in using the credentials.

### **2. Stock Analysis**
- Input the stock ticker (e.g., "1155.KL" for Maybank).
- Enter the start and end dates in the format `YYYY-MM-DD`.
- View the calculated analysis:
  - Average closing price.
  - Percentage change in price.
  - Highest and lowest prices.

### **3. Save Data**
- Analysis results are automatically saved in a CSV file (`user_data.csv`) with the following information:
  - Email
  - Stock ticker
  - Analysis results

---

## Files in the Project
- **`main.py`**: The primary program file handling the menu, user interaction, and workflows.
- **`functions.py`**: Contains reusable functions for stock data fetching, analysis, and CSV operations.
- **`user_data.csv`**: CSV file used to store user interaction data (created automatically after first use).

---

## Troubleshooting

### Common Issues
1. **ModuleNotFoundError: No module named 'yfinance' or 'pandas'**
   - Ensure the required libraries are installed:
     ```bash
     pip install yfinance pandas
     ```

2. **Invalid Stock Ticker**
   - Verify the entered stock ticker is correct.

3. **File Not Found (CSV)**
   - Ensure the directory is writable for saving the `user_data.csv` file.

---

## Acknowledgements
This project utilizes:
- [YFinance](https://pypi.org/project/yfinance/) for financial data retrieval.
- [Pandas](https://pandas.pydata.org/) for data manipulation and CSV operations.

---

Thank you for using the Stock Selection Tool! If you encounter any issues, feel free to reach out.

