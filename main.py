from datetime import datetime, timedelta
import calendar


def get_birthdays_per_week(users):
    today = datetime.now().date()
    week_ahead = today + timedelta(days=7)

    birthdays = {day: [] for day in calendar.day_name}

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        if today <= birthday_this_year < week_ahead:
            day_of_week = birthday_this_year.strftime("%A")

            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"

            birthdays[day_of_week].append(user["name"])

    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")
