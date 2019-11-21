import numpy as np
import pandas as pd
import time


CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = None
    month = None
    day = None

    city_dict = {'1': 'chicago', '2': 'new york city', '3': 'washington'}
    month_dict = {'1': 'january', '2': 'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june', '0': 'all' }
    day_dict = {
        '1': 'monday', 
        '2': 'tuesday', 
        '3': 'wednesday', 
        '4': 'thursday', 
        '5': 'friday', 
        '6': 'saturday',
        '7': 'sunday',
        '0': 'all'
    }

    while True:
        print(
            "Please select a city by number:\n \
            1=Chicago; 2=New York; 3=Washington"
        )
        city_input = input("Enter your chosen city: ")

        if city_input in city_dict:
            city = city_dict[city_input]
            break
        else:
            print("You have entered an invalid option")

    while True:
        print(
            "Please select your month by number:\n \
            1=January; 2=February; 3=March; 4=April; 5=May; 6=June; 0=All"
        )
        month_input = input("Enter your month: ")

        if month_input in month_dict:
            month = month_dict[month_input]
            break
        else:
            print("You have entered an invalid option")

    while True:
        print(
            "Please select your day by number:\n \
            1=Monday; 2=Tuesday; 3=Wednesday; 4=Thursday; 5=Friday; 6=Saturday; 7=Sunday; 0=All"
        )
        day_input = input("Enter your day: ")

        if day_input in day_dict:
            day = day_dict[day_input]
            break
        else:
            print("You have entered an invalid option")

    print("You have selected the following: city={}, month={}, day={}".format(city, month, day))          
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
    
    # Load data fiel into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Convert the End Time column to datatime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Extract hour from from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # Filter by month to create new new dataframe
        df = df[df['month'] == month]
        
    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week:", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour:", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start station: {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common end station: {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most frequent combination of start station and end station trip: \n{}".format(popular_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total tavel time: {total_travel_time}")

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {avg_travel_time}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_type_counts = df['User Type'].value_counts()

        print("User type counts:\n{}".format(user_type_counts))
        print("\n")

        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()

        print("Gender counts:\n{}".format(gender_counts))
        print("\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print(f"Earliest birth on record is: {earliest_birth}")

        popular_birth_year = df['Birth Year'].mode()[0]
        print(f"Most common birth year is: {popular_birth_year}")

        recent_birth = df['Birth Year'].max()
        print(f"Most recent birth on record is: {recent_birth}")
        
    except KeyError:
        print("Columns 'Gender' and 'Birth Year' do not exist for Wahsington city.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """Prompts the user to display data 5 rows at time"""
    
    print('\nCalculating Display of Raw Data...\n')
    start_time = time.time()
    
    user_input = None       
        
    for i in range(0, (df.shape[0]), 5):
        user_input = input("\nWould you like to view 5 rows or the next 5 rows of the dataframe? Enter yes or no.\n")
        
        if user_input == 'yes':
            print(f"\nDisplaying {i} to {i+5} rows of the dataframe")
            print(df[i:i+5])
        else:
            print('Thank you! Have a nice day!')
            break
    
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
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
