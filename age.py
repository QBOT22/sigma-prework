from datetime import datetime

def calculate_age(date_str):
    try:
        input_date = datetime.strptime(date_str, '%d-%m-%Y')
    
        today = datetime.today()
        
        age = today.year - input_date.year
        
        if (today.month, today.day) < (input_date.month, input_date.day):
            age -= 1

        return age
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return None

date_str = input("Enter a date in DD-MM-YYYY format: ")

age = calculate_age(date_str)
if age is not None:
    print(f"The age is: {age}")



