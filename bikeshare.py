import time
import pandas as pd
import numpy as np
import calendar

cities = ['Chicago', 'New York City', 'Washington'] 
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']   
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all']

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

    while True:
       print('Which city you would like to view? Please select:')
       city = input('Chicago,\n'
                     'New York City,\n'
                     'Washington\n').lower()
       if city in CITY_DATA:
             break
       else:
           print('\nPlease enter a valid city name.')
    
   
    #2-ask the user to input month (jan, feb, ... , jun, all)
    #check for input validation for month
    months = ["jan", "feb", "mar", "apr", "may", "jun", "all"]
    while True:
        month = input("Please select a month - Jan, Feb, Mar, Apr, May, Jun - or select 'All' for no filter:\n").lower()
        if month in months:
            break
        else:
            print("Please select a valid input.")
    
    # 3- ask the user to input day of week (sat , sun, mon ... fri, all)
    #check for input validation
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun", "all"]
    while True:
        day = input("Please select a weekday - Mon, Tue, Wed, Thu, Fri, Sat, Sun - or select 'All' for no filter:\n").lower()
        if day in days:
            break
        else:
            print("Please select a valid input.")

    
    return city, month, day
       
   
    print('-'*40)
    return city, month, day
 
   
def load_data(city, month, day):
    #Applies user's city, month, day selection to bikeshare stats data
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # data file as a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # converting (Start Time) column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    common_month = df['month'].mode()[0]
    print("Most common month is ", common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week is ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station is:', common_start) 

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most commonly used end station is:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    freq_combination = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('Most frequent combination of start and end stations is:', freq_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time took:", (total_travel_time/3600), " hours")

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time took:", (average_travel_time/3600), " hours")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_type = df['User Type'].value_counts()
    print("Counts by user type:\n", counts_user_type)

    # TO DO: Display counts of gender 
    try:
        counts_gender = df['Gender'].value_counts()
        print("\nCounts by gender:\n", counts_gender)
    except KeyError:
        print("\nThere is no gender data to return")
        
    # Display earliest, most recent, and most common year of birth
    try:
        print("\nThe earliest year of birth is: ", int(df['Birth Year'].min()))
        print("The most recent year of birth is: ", int(df['Birth Year'].max()))
        print("The most common year of birth is: ", int(df['Birth Year'].mode()[0]))
    except KeyError:
        print("\nThere is no birth year data to return")
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

# Asking if the user want show more data
def more_data(df):
    more_data = input("Would you like to view 5 rows of data? Please enter yes or no? ").lower()
    start_loc = 0
    while more_data == 'yes':
        print(df.iloc[0:5])
        start_loc += 5
        more_data = input("Would you like to view an additional 5 rows of data? Please enter yes or no? ").lower()
        
    return df


# Asking if the user would like to restart
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()