import datetime

users = [{'name': "Bill", 'birthday': datetime.datetime(year=1990, month=12, day=31)},
         {'name': "William", 'birthday': datetime.datetime(year=2005, month=10, day=11)},
         {'name': "Marie", 'birthday': datetime.datetime(year=1999, month=8, day=26)},
         {'name': "Max", 'birthday': datetime.datetime(year=1998, month=7, day=5)},
         {'name': "Elena", 'birthday': datetime.datetime(year=2000, month=5, day=23)},
         {'name': "Pavel", 'birthday': datetime.datetime(year=1996, month=4, day=24)}]


def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if today.weekday() == 0:
        start_week = today
    else:
        start_week = today - datetime.timedelta(days=today.weekday() - 1)
        print(start_week)
    end_week = start_week + datetime.timedelta(days=6)

    print("Birthdays for the week of {} to {}".format(start_week, end_week))

    birthdays_for_the_week = [list() for weekday in range(7)]
    for user in users:
        birthday = datetime.date(year=start_week.year, month=user["birthday"].month, day=user["birthday"].day)
        difference = (birthday - start_week).days
        if difference >= 7:  # later than this week
            continue
        elif difference == -1 or difference == -2:  # last weekend
            birthdays_for_the_week[0] += [user["name"]]
        else:  # during this week
            birthdays_for_the_week[difference] += [user["name"]]

    for weekday, names in zip(weekdays, birthdays_for_the_week):
        print(f"{weekday}: {', '.join(names)}")


get_birthdays_per_week(users)