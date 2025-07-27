# fns_and_dsa/explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days: int):
    """
    Calculates and prints the date after adding a specified number of days.

    Args:
        days (int): Number of days to add.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Save future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    display_current_datetime()
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please e
