import sys
from datetime import datetime, date
import inflect

import sys
from datetime import datetime, date
import inflect

def calculate_age_in_minutes(birthdate, today=None):
    if today is None:
        today = date.today()

    if today < birthdate:
        sys.exit("Invalid input. Birthdate cannot be in the future.")

    # Find difference between two dates
    delta = today - birthdate

    # Convert difference in days to minutes
    minutes = delta.days * 24 * 60

    # Convert numerals into English words
    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes)
    # Remove 'and' from string and Capitalize the first letter
    minutes_in_words = minutes_in_words.replace(" and", "").capitalize()

    return minutes_in_words + " minutes"

def main():
    date_string = input("Please enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format. Expected YYYY-MM-DD.")
    print(calculate_age_in_minutes(birthdate))

if __name__ == "__main__":
    main()

