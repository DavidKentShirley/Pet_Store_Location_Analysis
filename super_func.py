# Imports all relevant libraries
import requests
import json 
import pandas as pd
import csv
import os
import numpy as np
import folium
from folium import plugins
import geocoder
import geopy
import geojson
import geopandas as gpd
import matplotlib.pyplot as plt

# Functions
def yelp_call(url_params, creds):
    results = []
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer ' + creds['key'],
    }             
    
    rq_j = requests.get(url, headers=headers, params=url_params) 
    results.append(rq_j.text)
    return results 
                          

def parse_results(results):
    parsed_data = [] 
    list_of_data = json.loads(results[0])['businesses']
    for business in list_of_data:
        biz_tuple = (business['id'], business['name'],business['review_count'],business['rating'],business['location']['zip_code'], business['coordinates']['latitude'], business['coordinates']['longitude'], business['categories'][0]['alias'])
        parsed_data.append(biz_tuple)
        
    return pd.DataFrame(parsed_data, columns= ['id', 'name', 'reviews', 'rating', 'zip', 'latitude', 'longitude', 'alias'])
    
 

def df_save(parsed_results, csv_filename):
    if not os.path.isfile(str(csv_filename)):
      parsed_results.to_csv(str(csv_filename), header='column_names')
    else: # else it exists so append without writing the header
      parsed_results.to_csv(str(csv_filename), mode='a', header=False)


def yelp_call_reviews(creds, business_ids):
    reviews = []
    
    while len(reviews) < len(business_ids) :
        for business in business_ids:
            url = 'https://api.yelp.com/v3/businesses/' + business + '/reviews'
            headers = {'Authorization': 'Bearer ' + creds['key']}
            rq_j = requests.get(url, headers=headers) 
            reviews.append(rq_j.text)
    return reviews


def business_ids_get():
    business_ids = []
    business_names = []
    business_ids_names = []
    mycsv = csv.reader(open('./csv/petstores.csv'))
    for row in mycsv:
        bus_id = row[1]
        bus_name = row[2]
        business_ids.append(bus_id)
        business_names.append(bus_name)
    business_ids = business_ids[1:]
    business_names = business_names[1:]
    business_ids_names = []
    for i in range(len(business_ids)):
        business_ids_names.append({'bus_id': business_ids[i], 'bus_name': business_names[i]})
    return business_ids, business_ids_names, business_names

def list_of_reviews(reviews,business_ids, business_ids_names, business_names):
    list_of_reviews = []
    for i in range(len(reviews)):
        for rev_ in json.loads(reviews[i])['reviews']:
            list_of_reviews.append({'business':business_ids_names[i]['bus_name'], 'business_id':business_ids_names[i]['bus_id'],
                                'review_id':rev_['id'], 'review_url':rev_['url'], 'text_excerpt':rev_['text'],
                                'rating':rev_['rating'],'time_created':rev_['time_created'], 'used_id':rev_['user']['id'],
                                'user_profile_url':rev_['user']['profile_url'], 'user_image_url':rev_['user']['image_url'],
                                'user_name': rev_['user']['name']})  
    return list_of_reviews
        
 
# All Map related Stuff
url_geo = 'https://data.beta.nyc/dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson'



lat = 40.72
long = -73.794


geoJSON_df = gpd.read_file(url_geo)

geo_data_Q1 = geoJSON_df['borough'] == "Queens"
geo_data_Q = geoJSON_df[geo_data_Q1]

geo_data_M1 = geoJSON_df['borough'] == "Manhattan"
geo_data_M = geoJSON_df[geo_data_M1]

geo_data_r1 = geoJSON_df['neighborhood'] == "Upper East Side"
geo_data_r = geoJSON_df[geo_data_r1]



M_zips = pd.read_csv('./csv/Mzips.csv')
Mzips = list(M_zips['Zip'])

Q_zips = pd.read_csv('./csv/Qzips.csv')
Qzips = list(Q_zips['Zip Code'])


# Data Cleaning 

zipcodesinqueenscounty = list(pd.read_csv('QueensZipCodes.csv')['Zip'])

zipcodesinNYcounty = list(pd.read_csv('ManhattanZipCodes.csv')['Zip'])

DogParks_Manhattan_DF = pd.read_csv('dogparkmanhattan.csv')

actualdogpark = DogParks_Manhattan_DF[DogParks_Manhattan_DF['category1'] == 'dog_parks']

dogparksinNYzipcodes = actualdogpark[actualdogpark['zip_code'].isin(zipcodesinNYcounty)]