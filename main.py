from functions import register_user, authenticate_user, fetch_closing_prices, analyze_closing_prices, save_user_data

def main():
    while True:
        #WELCOME PAGE / MAIN MENU
        print("\n***** Welcome to the Stock Selection Tool *****")
        choice = input("1. Register\n2. Login\n3. Exit\n\nChoose an option: ")

        #Choose 1 to Register as a new user
        if choice == '1':
            email = input("\nEnter your email: ")
            password = input("Enter your password: ")
            register_user(email, password)
            print("<< User registered successfully! >>\n")

        #Choose 2 to Login after successful registration
        elif choice == '2':
            email = input("\nEnter your email: ")
            password = input("Enter your password: ")

            #If Login is successful, user may proceed to Analyzing process
            if authenticate_user(email, password):
                print("<< Login successful! >>\n")
                while True:
                    #Enter a ticker to start the Analysis
                    ticker = input("\nEnter stock ticker (or 'exit' to logout): ")
                    if ticker.lower() == 'exit':
                        break

                    #Enter a valid period and date, example: 2024-12-07
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    
                    closing_prices = fetch_closing_prices(ticker, start_date, end_date)
                    if closing_prices is not None and not closing_prices.empty:
                        analysis_result = analyze_closing_prices(closing_prices)
                        print("\nAnalysis Results:\n", analysis_result)
                        save_user_data(email, ticker, analysis_result)
                    else:
                        #Print error message if input invalid ticker and date range
                        print("\n<< No data found for the specified ticker and date range. >>\n")
                
            else:
                #Print error message if failed to authenticate user.
                print("\n<< Authentication failed. Please try again. >>\n")

        #Choose 3 to Exit the program.
        elif choice == '3':
            print("******** Exiting the program. ********")
            break

        else:
            #Print Error message if invalid input is entered (NOT 1/2/3)
            print("<< Invalid choice. Please try again. >>")

if __name__ == "__main__":
    main()
