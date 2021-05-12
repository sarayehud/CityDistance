# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:24:49 2021

@author: 97250
"""

import requests
def places ():
    file= open("dests.txt",encoding="utf8")
    destinations_list=list()
    for line in file:
            destinations_list.append(line.strip()) 
    for i in range(len(destinations_list)):
        distance(destinations_list[i]) 
    print(destinationsPerCity)
    listdistance=list()
    for k,v in destinationsPerCity.items():
        listdistance.append((v[0],k))
    listdistance.sort()
    print("The 3 furthest cities from Tel-aviv are:")
    listdistance=listdistance[-3:]
    for i in listdistance:
        print(i)

def distance(distance1):
    try:
        adress="תל אביב"
        api_key="AIzaSyD_TMHjGBuLZX1jUDpNy2OOs4u8Xe7edCA"
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(adress,distance1,api_key)
        response=requests.get(url).json()
        url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(distance1,api_key)
        response2=requests.get(url2).json()
        distance = response['rows'][0]['elements'][0]['distance']['text']
        duration = response['rows'][0]['elements'][0]['duration']['text']
        latitude = response2['results'][0]['geometry']['location']['lat']
        longitude = response2['results'][0]['geometry']['location']['lng']
        detailsPerCity = (distance, duration) + (latitude, longitude) 
        destinationsPerCity[distance1] = detailsPerCity
    except:
        print("no value found" +" "+ distance1)
    
    
destinationsPerCity=dict()
places ()
    
    
 