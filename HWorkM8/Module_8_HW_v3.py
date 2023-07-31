import datetime

users = [{'name': "Bill", 'birthday': datetime.datetime(year=1990, month=12, day=31)},
         {'name': "William", 'birthday': datetime.datetime(year=2005, month=10, day=11)},
         {'name': "Marie", 'birthday': datetime.datetime(year=1999, month=8, day=26)},
         {'name': "Max", 'birthday': datetime.datetime(year=1998, month=4, day=28)},
         {'name': "Elena", 'birthday': datetime.datetime(year=2000, month=4, day=30)},
         {'name': "Pavel", 'birthday': datetime.datetime(year=1996, month=4, day=23)}]


def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if today.weekday() == 0:
        start_week = today
    else:
        start_week = today - datetime.timedelta(days=today.weekday())
        print(f"start week: {start_week}")

    birthdays_for_the_week = [list() for weekday in range(7)]
    birthdays_for_the_next_week = [list() for weekday in range(1)]
    for user in users:
        birthday = datetime.date(year=start_week.year, month=user["birthday"].month, day=user["birthday"].day)
        difference = (birthday - start_week).days

        if difference >= 7:  # later than this week
            continue
        if difference == -1 or difference == -2 and today.weekday() == 0:  # last weekend
            birthdays_for_the_week[0] += [user["name"]]
        elif difference == 5 or difference == 6:  # next weekend
            birthdays_for_the_next_week[0] += [user["name"]]
        else:  # during this week
            birthdays_for_the_week[difference] += [user["name"]]

    for weekday, names in zip(weekdays, birthdays_for_the_week):
        print(f"{weekday}: {', '.join(names)}")
    print(f"Birthdays on this holidays:")
    for weekday, names in zip(weekdays, birthdays_for_the_next_week):
        print(f"{weekday}: {', '.join(names)}")

get_birthdays_per_week(users)




        # max_difference = (4 - today.weekday())
        # if difference >= max_difference:  # later than this week
        #     continue
        # elif difference == -1 or difference == -2:  # last weekend
        #     birthdays_for_the_week[0] += [user["name"]]
        # else:  # during this week
        #     birthdays_for_the_week[difference] += [user["name"]]
