from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            next_birthday_date = today + timedelta(days=delta_days)
            if next_birthday_date.weekday() >= 5:
                weekday = "Monday"
            else:
                weekday = next_birthday_date.strftime("%A")

            birthday_dict[weekday].append(name)

    result = ""
    for day, names in birthday_dict.items():
        result += f"{day}: {', '.join(names)}\n"

    return result