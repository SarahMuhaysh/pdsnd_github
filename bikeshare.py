import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


    #The user will enter the data

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
    city=input("Would you like to see data for Chicago, New York City, or Washington? \n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Invalid input please choose between Chicago, New York city, or Washington: \n").lower()

    """
    try:
        pd.read_csv(CITY_DATA[city])
    except:
      print('Invalid input please try again')
    """

    # TO DO: get user input for month (all, january, february, ... , june)

    month=input("Which month? January, February, March, April, May, or June? \n").lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
         month=input("Invalid input please choose a month from January to June: \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Which day? please enter a day (e.g., Sunday): \n").lower()
    while day not in ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
         day=input("Invalid input please type a correct day: \n")

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

       # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode())

    # TO DO: display the most common day of week
    print("The most common day of the week is: ", df['day_of_week'].mode())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df ['Start Station'].mode()
    print("The most common start station is: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df ['End Station'].mode()
    print("The most common end station is: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    mcsaes = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(mcsaes)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time in hours is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time in hours is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
    # Only access Gender column in this case
     gender = df['Gender'].value_counts()
     print(gender)

    else:
     print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
     years_of_birth = df['Birth Year'].unique()
     earliest_yob = int (df['Birth Year'].min())
     most_recent_yob = int (df['Birth Year'].max())
     most_common_yob = int (df['Birth Year'].mode())
     print("The earliest year of birth is: ", earliest_yob)
     print("The most recent year of birth is: ", most_recent_yob)
     print("The most common year of birth is: ", most_common_yob)
    else:
        print('Birth year cannot be calculated because birth year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

<<<<<<< HEAD
#This loop will present data to the user
||||||| 1b2af3c
#This is the main function that will continue to loop till the user exit
=======
>>>>>>> 7b196b8db534c4d9591ca2c335c7de55591b9077
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
        start_loc = 0
        while (view_data == 'yes'):
            start_loc += 1
            for i in range(start_loc*5,start_loc*5+5):
                print(df.iloc[i])
            view_data = input("Do you wish to continue?: \n").lower()

        restart = input('\nWould you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
