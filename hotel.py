# This API For searching the hotels according to the users input

import requests


des = input("Enter your destination ")
url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":des,"locale":"en_US"}

# x-rapidapi-key should add your Key

headers = {
    'x-rapidapi-key': "e7b9bf97c4msh59fe80380ec2345p1e547fjsn1e399dc8d053", 
    'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text) 



print("*******************************************************")
# Define the No. of guest, children, min and max price, check in, check out

""" import requests

guestNumber = input("Enter the number of the guest ")
childrenNumber = input("Enter the number of the children ")
# checkOut = input("The date of checkout Year-Month-Day ")
# checkIn = input("The date of checkin Year-Month-Day ")
# priceMin = input("Enter the max price you are looking for ")
# priceMax = input("Enter the max price you are looking for ")

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"adults1":guestNumber,"pageNumber":"1","destinationId":"1506246","pageSize":"1","checkOut":"2020-01-15","checkIn":"2020-01-08","children6":childrenNumber,"priceMax":"2000","sortOrder":"PRICE","locale":"en_US","currency":"USD","priceMin":"200"}
headers = {
    'x-rapidapi-key': "e7b9bf97c4msh59fe80380ec2345p1e547fjsn1e399dc8d053",
    'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text) """