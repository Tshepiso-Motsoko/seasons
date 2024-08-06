from datetime import date
import seasons


def test_calculate_age_in_minutes():
    # Set a fixed today's date for testing
    today = date(2023, 1, 1)

    # Test 1: One year difference
    birthdate = date(2022, 1, 1)
    assert seasons.calculate_age_in_minutes(birthdate, today) == "five hundred twenty-five thousand six hundred"

    # Test 2: Two years difference
    birthdate = date(2021, 1, 1)
    assert seasons.calculate_age_in_minutes(birthdate, today) == "one million fifty-one thousand two hundred"

    # Add more test cases as required
