import pandas as pd

# read data into CSV file as pandas data frame
bikes = pd.read_csv(r'C:\Users\jvort\Downloads\archive\london_merged.csv')

#explore the data
bikes.info()


print(bikes.shape)
print(bikes.head())

# count the unique values in the weather_code column
print(bikes.weather_code.value_counts())

# count the unique values in season column
print(bikes.season.value_counts())

#updating column names dictionary
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_c',
    't2':'temp_feels_like_c',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)

#Changing the humidity to percentage values
bikes.humidity_percent = bikes.humidity_percent / 100

# creating season dictionary for mapping the season
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'fall',
    '3.0':'winter'
}


weather_dict = {

    '1.0':'clear',
    '2.0':'scattered clouds',
    '3.0':'broken clouds',
    '4.0':'cloudy',
    '7.0':'rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'snowfall'
}

#changing the season column data type to string
bikes.season = bikes.season.astype('str')
#mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

#changing the weahter column data to string
bikes.weather = bikes.weather.astype('str')
#mapping the values to actual written weather
bikes.weather = bikes.weather.map(weather_dict)


#reviewing updated names
print(bikes.head())

#writing data frame to excel file.
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')