from functions import register_user, authenticate_user, fetch_closing_prices, analyze_closing_prices, save_user_data

def main():
    while True:
        print("\n***** Welcome to the Stock Selection Tool *****")
        choice = input("1. Register\n2. Login\n3. Exit\n\nChoose an option: ")

        if choice == '1':
            email = input("\nEnter your email: ")
            password = input("Enter your password: ")
            register_user(email, password)
            print("<< User registered successfully! >>\n")

        elif choice == '2':
            email = input("\nEnter your email: ")
            password = input("Enter your password: ")

            if authenticate_user(email, password):
                print("<< Login successful! >>\n")
                while True:
                    ticker = input("\nEnter stock ticker (or 'exit' to logout): ")
                    if ticker.lower() == 'exit':
                        break
                    
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    
                    closing_prices = fetch_closing_prices(ticker, start_date, end_date)
                    if closing_prices is not None and not closing_prices.empty:
                        analysis_result = analyze_closing_prices(closing_prices)
                        print("\nAnalysis Results:\n", analysis_result)
                        save_user_data(email, ticker, analysis_result)
                    else:
                        print("\n<< No data found for the specified ticker and date range. >>\n")
                
            else:
                print("\n<< Authentication failed. Please try again. >>\n")

        elif choice == '3':
            print("******** Exiting the program. ********")
            break

        else:
            print("<< Invalid choice. Please try again. >>")

if __name__ == "__main__":
    main()
