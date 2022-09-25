# INF 601 Advanced Python Programming
# Fall 2022
# Thomas Kerley
# Mini Project 2
# Due 9/25/2022

import requests
import pandas as pd

countryList = ['Austria', 'Belgium', 'Brazil', 'Canada','Chile', 'China', 'Czech Republic', 'Denmark', 'Estonia', 
    'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Israel', 
    'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Norway', 'Poland', 'Portugal', 'Slovakia', 'Slovenia', 'South Africa',
    'Sweden', 'Switzerland', 'Turkey', 'United States']
inflationTypes = ['CPI', 'HICP']

for country in countryList:
    for iType in inflationTypes:
        api_url = 'https://api.api-ninjas.com/v1/inflation?country={}&type={}'.format(country, iType)
        response = requests.get(api_url, headers={'X-Api-Key': 'XAnRBGt717T92RQT6/9rig==UD2M9TYjxtSswYLY'})
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)
