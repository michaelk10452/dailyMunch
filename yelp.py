
#Business Search URL -- 'https://api.yelp.com/v3/businesses/search'
#Business match  URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search    URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details URL -- 'https://api.yelp.com/v3/business/{id}'
#Business Reviews URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'


#Import the modules
import os
import requests
class Yelp:

    #Define a bussiness ID
    business_id = ''

    # Define the API Key, Define the Endpoint, and define the Header
    API_KEY = os.getenv('API_KEY')
    ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'
    HEADERS = {'Authorization': 'bearer %s' % API_KEY}

    def businessSearch(param_dict):
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
        response = requests.get(url= ENDPOINT, params= param_dict, headers = Yelp.HEADERS)
        #COnvert JSON String to a dictionary
        business_data = response.json()
        return business_data

    def businessMatch(param_dict):
        ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'
        response = requests.get(url= ENDPOINT, params= param_dict, headers = Yelp.HEADERS)
        #COnvert JSON String to a dictionary
        business_data = response.json()
        return business_data

        #Print businesses
        # if business_data:
        #     for biz in business_data['businesses']:
        #         print(biz)
        # else:
        #     print("empty")




    #Define the parameters
    # PARAMETERS = {'term':'coffee',
    #               'limit': 50,
    #               'radius': 10000,
    #               'offset': 50,
    #               'location': 'San Deigo'}

    # PARAMETERS = {'name': 'Peets Coffee & Tea',
    #             'address1': '7845 Highland Village Pl',
    #             'city': 'San Diego',
    #             'state': 'CA',
    #             'country': 'US'}

    #Make a request to the yelp API

    # response = requests.get(url= ENDPOINT, params= PARAMETERS, headers = HEADERS)

    # #COnvert JSON String to a dictionary
    # business_data = response.json()

    # #print(business_data.keys())

    # for biz in business_data['businesses']:
    #     print(biz)
