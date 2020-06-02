import time
import pandas as pd
import numpy as np
from scipy import stats

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityes = ['chicago', 'new york city', 'washington']
    while True:
        try:
            city=str(input("enter one of the following cityes ['chicago', 'new york city', 'washington'] : "))
            if city in cityes:
                break
            else:
                print("please enter the month in the requested form")
        except:
            print("please enter the month in the requested form")



    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    #month='january'
    while True:
        try:
            month=str(input("enter one of the following months ['january', 'february', 'march', 'april', 'may', 'june'] or select 'all' for all the months : "))
            if month in months:
                break
            else:
                print("please enter the month in the requested form")
        except:
            print("please enter the month in the requested form")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    #day='monday'
    while True:
        try:
            day=str(input("enter one of the following days of the week ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] or select 'all' for all the days of the week : "))
            if day in days:
                break
            else:
                print("please enter the month in the requested form")
        except:
            print("please enter the month in the requested form")
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
        month = months[month]
        df = df[df['Start Time'].dt.month==month]

    # filter by day of week if applicable
    if day != 'all':
        days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
        df = df[df['Start Time'].dt.weekday == days[day.title()]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    #common_month=int(stats.mode(df['Start Time'].dt.month.values)[0])
    #common_month=months[common_month].title()
    common_month=months[int(stats.mode(df['Start Time'].dt.month.values)[0])].title()
    #print(common_month)
    print("the most common month is {}".format(str(common_month)))

    # TO DO: display the most common day of week
    #common_day=int(stats.mode(df['Start Time'].dt.weekday.values)[0])
    #common_day=days[common_day].title()
    common_day=days[int(stats.mode(df['Start Time'].dt.weekday.values)[0])].title()
    print("the most common day is {}".format(str(common_day)))

    # TO DO: display the most common start hour
    common_hour=int(stats.mode(df['Start Time'].dt.hour.values)[0])
    #print(common_hour)
    print("the most common start hour is {}".format(str(int(common_hour))))
    #print(df.info())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=stats.mode(df['Start Station'])[0]
    common_start_station="".join(common_start_station)
    print("the most common Start Station is {}".format(str(common_start_station)))

    # TO DO: display most commonly used end station
    common_end_station=stats.mode(df['End Station'])[0]
    common_end_station="".join(common_end_station)
    print("the most common End Station is {}".format(str(common_end_station)))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start - End Station']=df['Start Station']+" - "+df['End Station']
    common_start_end_station=stats.mode(df['Start - End Station'])[0]
    common_start_end_station="".join(common_start_end_station)
    print("the most common Start - End Station is {}".format(str(common_start_end_station)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df["Trip Duration"].sum()
    print("the total travel time is {} minutes, or in other way the total travel time is {} hours".format(str(int(total_time/60)),str(int(total_time/(60*60)))))

    # TO DO: display mean travel time
    mean_travel_time=(df['Trip Duration']).mean()
    mean_travel_time=int(mean_travel_time)
    print("the mean travel time is {} minutes".format(str(float(mean_travel_time/60))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df.groupby("User Type")["User Type"].count()
    print("the total trips of customers are {}, and the total trip by suscriber are {}".format(str(count_of_user_types[0]),str(count_of_user_types[1])))

    # TO DO: Display counts of gender
    count_of_gender=df.groupby("Gender")["Gender"].count()
    print("the total trips of famele are {}, and the total trip by male are {}".format(str(count_of_gender[0]),str(count_of_gender[1])))

    # TO DO: Display earliest, most recent, and most common year of birth
    min_year = int(df["Birth Year"].min())
    max_year = int(df["Birth Year"].max())
    mode_year = int(stats.mode(df['Birth Year'])[0])
    print("the most youg user born in {}, the eldeer user born in {}, most common year of birth is {}".format(str(max_year),str(min_year),str(mode_year)))

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
