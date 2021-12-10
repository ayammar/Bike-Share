import time
import pandas as pd
import numpy as np
from datetime import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    while True:
        city = str(input("Which city would you like to explore Chicago, Washinton , New York City?\n")).lower()

        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)
    months = ["jan", "feb", "mar", "apr", "may", "june","all"]
    while True:
        month = str(input("Which month would you like to see? Jan,Feb,Mar,Apr,May,June,all\n")).lower()
        
        if month in months:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat","all"]
    while True:
        day = str(input("Which day would you like to see? Sun,Mon,Tue,Wed,Thu,Fri,Sat,all\n")).lower()
        
        if day in days:
            break

    
    return city, month, day
    print('-'*40)

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Month'] = pd.DatetimeIndex(df['Start Time']).month
    common_month = df["Month"].mode()
    print("Most common month:\n",common_month)

    # display the most common day of week
    df["Day of week"] = pd.DatetimeIndex(df["Start Time"]).dayofweek
    common_day_week = df["Day of week"].mode()
    # display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    common_start_hour = df["hour"].mode()
    print("Most common start hour:\n", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()
    print("Most commonly used start station:\n", common_start_station)

    # display most commonly used end station
    common_end_station = df["End Station"].mode()
    print("Most commonly used end station:\n", common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_end_station = (df["Start Station"] + " , "+ df["End Station"]).mode()
    print("Most frequent combination of start station and end station trip:\n", common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time:\n", total_travel_time)

    # display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print("Average travel time:\n", avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print("Number of Users:\n", user_counts)

    # Display counts of gender
    count_of_gender = df["Gender"].value_counts()
    print("Counts of gender:\n", count_of_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_year = df["Birth Year"].min()
    print("Earliest year of birth:\n", earliest_year)
    
    most_recent_year = df["Birth Year"].max()
    print("Most recent year of birth:\n", most_recent_year)
    
    most_common_year = df["Birth Year"].mode()
    print("Most common year of birth:\n", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
