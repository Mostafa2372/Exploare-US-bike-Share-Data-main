import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_month():
    # Ask the user which month to filter the data
    month = ""
    my_month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    while month not in my_month_list:
        month = input("Which month? January , February, March, April, May or June ").strip()
        month = month.lower()
    return month


# Ask the user which day to filter the data
def get_day():
    day = " "
    my_day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while day not in my_day_list:
        day = (input("Which day? Monday , Tuesday ... Sunday")).strip()
        day = day.lower()
        return day


def format_time(time):
    # Convert seconds to days, hours, minutes and seconds
    day = int(time // (24 * 3600))
    time = int(time % (24 * 3600))
    hour = int(time // 3600)
    time %= 3600
    minutes = int(time // 60)
    time %= 60
    seconds = int(time)
    return day, hour, minutes, seconds


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = " "
    my_city_list = ["chicago", "new york city", "new york", "washington"]
    while city not in my_city_list:
        city = input("Would you like to data for Chicago , New York , or Washington?").strip()
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    choose = ""
    choose_list = ["month", "day", "none", "both"]
    while choose not in choose_list:
        choose = input(
            "Would you like to filter the data by month, day ,both, or not at all? Type 'none' for no time filter.").strip()
        choose = choose.lower()
        if choose == "both":
            month = get_month()
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_day()
            print('-' * 40)
            return city, month, day
        # ====================================================================
        elif choose == "month":
            month = get_month()
            print('-' * 40)
            day = "all"
            return city, month, day
        # ====================================================================

        elif choose == "day":
            day = get_day()
            month = "all"
            print('-' * 40)
            return city, month, day
        # ====================================================================
        elif choose == "none":
            month = "all"
            day = "all"
            print('-' * 40)
            return city, month, day
        else:
            choose = ""


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print('Hello! Let\'s explore some US bikeshare data!')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    most_common_month = df['month'].mode().max()
    most_common_month = months[most_common_month]
    print(f"The most common month {df['month'].mode()[0]} is ({most_common_month})")

    # TO DO: display the most common day of week
    print(f"The most common day {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print(f"The most common start hour {df['hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"most commonly used start station is {df['Start Station'].mode()[0]}")

    # TO DO: display most commonly used end station
    print(f"most commonly used end station is {df['End Station'].mode()[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    df["path"] = df["Start Station"] + " - " + df["End Station"]
    print(f"most frequent combination of start station and end station trip is {df['path'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    day, hour, minutes, seconds = format_time(total_travel)
    print(f"Total travel time d:h:m:s {day}:{hour}:{minutes}:{seconds}")

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    day, hour, minutes, seconds = format_time(mean_travel)
    print(f"Mean travel time d:h:m:s {day}:{hour}:{minutes}:{seconds}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Counts of user types is {df['User Type'].count()}")

    # TO DO: Display counts of gender
    print(f"Counts of each gender is {df.groupby(df['User Type'])['User Type'].count()}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print(f"Earliest year of birth is {df['Birth Year'].min()}")
        print(f"Most recent year of birth is {df['Birth Year'].max()}")
        print(f"most common year of birth is {df['Birth Year'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(city):
    # Ask user if he likes to see another 5 rows of the raw data
    no_list = ['no']
    for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
        print(chunk)
        show_raw = input('Would you like to see another 5 rows of the raw data? Enter yes or no.\n').strip()
        show_raw = show_raw.lower()
        if show_raw in no_list:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
