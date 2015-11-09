
# coding: utf-8

# #Cycl.co - A bike share clustering analysis via K-Means

import pandas as pd
from pandas import DataFrame, Series
from sklearn.cluster import KMeans as km
from sklearn.metrics import silhouette_samples, silhouette_score
import random

import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)


# ###Loading the data

TRIP_FILE = ('201508_trip_data.csv')
STATION_DATA = ('201508_station_data.csv')

trip_data = pd.read_csv(TRIP_FILE)
station_data = pd.read_csv(STATION_DATA)

len(trip_data)
print("Initial data description")
print(trip_data.describe())


# ###Joining tables to add coordinates to main df for analysis

trip_data = trip_data.merge(station_data[['station_id', 'lat', 'long', 'landmark']], left_on = 'Start Terminal',                             right_on = 'station_id')
trip_data = trip_data.merge(station_data[['station_id', 'lat', 'long']], left_on = 'End Terminal',                             right_on = 'station_id')
print("Stations Added")
print(trip_data.head(2))


# ###Compiling San Francisco specific data

trip_data_sf = trip_data[trip_data.landmark == 'San Francisco'].copy()
print("Compiled San Francisco city data")
print(trip_data_sf.head(2))


# ###Cleaning up column names

trip_data_sf.rename(columns={'station_id_x': 'start_station', 'lat_x': 'start_lat', 'long_x': 'start_long', 'station_id_y': 'end_station', 'lat_y': 'end_lat', 'long_y': 'end_long'}, inplace=True)
#trip_data_sf.drop('name', axis=1, inplace=True)
print("Renamed columns")
print(trip_data_sf.head(2))


# ###Euclidean distance formula

def measure_distance(start_lat, start_long, end_lat, end_long):
    x_difference = start_lat - end_lat
    y_difference = start_long - end_long
    x_squared = x_difference**2
    y_squared = y_difference**2
    added = x_squared + y_squared
    squart_root_ = np.sqrt(added)
    to_feet = squart_root_ * 2390.31 / 0.0082459784137541101
    return to_feet

def compute_distance_df(trip_data_sf, start_lat_name, start_long_name, end_lat_name, end_long_name):
    distances_list = []
    for row in trip_data_sf.index:
        distance_between_points = measure_distance(trip_data_sf[start_lat_name][row], trip_data_sf[start_long_name][row],                                trip_data_sf[end_lat_name][row], trip_data_sf[end_long_name][row])
        #print(distance_between_points)
        distances_list.append(distance_between_points)
        #print(distances_list)
    return distances_list


distances_list = compute_distance_df(trip_data_sf,"start_lat","start_long","end_lat","end_long")

trip_data_sf['distance_start_stop'] = distances_list


#Converting to datetime
print("One sec. Converting to datetime objects...")
trip_data['Start Date'] = pd.to_datetime(trip_data['Start Date'])


# ###Setting up my bicycle trip features for K-Means
print("Bear with me. Setting up features for clustering...")
features = trip_data_sf[['Duration', 'distance_start_stop']].copy()
features['day_of_week'] = pd.DatetimeIndex(trip_data_sf['Start Date']).dayofweek
features['hours'] = pd.DatetimeIndex(trip_data_sf['Start Date']).hour

print("How do I look?")
print(features.head())


# ###Normalizing the data and clustering


cols_to_norm = ['Duration','distance_start_stop', 'day_of_week', 'hours'] 
features[cols_to_norm] = features[cols_to_norm].apply(lambda x: (x - x.mean()) / (x.max() - x.min()))
print("Normalized")
print(features.head(2))


cluster_num = 11
model = km(n_clusters = cluster_num, n_init=5, max_iter=20)
model.fit_transform(features)
print("Model created")


features['labels'] = model.labels_
print("Got some labels.")
print(features.head(2))


#sampling my data to run the silhouette score
sample = features.sample(4000)


silhouette_score(sample.values, sample['labels'].values)


#finding the cluster centers
model.cluster_centers_[0]


# ###Visualizing the cluster centers to double check accuracy of model

#Uncomment to see cluster center bar graphs
#bars are features - duration, distance, day of the week, and time of the day
#for i in range(11):
#    plt.bar([0,1,2,3], model.cluster_centers_[i])
#    plt.show()




