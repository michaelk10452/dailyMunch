from Yelp import Yelp

#List of visited Resturants
resto_list = [{'id': 'VGI5GoGLBAucTQGZq4Reww', 'alias': 'model-meals-santa-ana-3', 
'name': 'Model Meals', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Ekej2JHvh5zWFjFAE9014g/o.jpg', 'is_closed': False, 
'url': 'https://www.yelp.com/biz/model-meals-santa-ana-3?adjust_creative=QkCWE7HoAg6T9MbS75HNlQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=QkCWE7HoAg6T9MbS75HNlQ', 
'review_count': 268, 'categories': [{'alias': 'fooddeliveryservices', 'title': 'Food Delivery Services'}], 'rating': 5.0, 
'coordinates': {'latitude': 33.74832, 'longitude': -117.86623}, 'transactions': [], 'price': '$$', 
'location': {'address1': '201 E 4th St', 'address2': None, 'address3': '', 'city': 'Santa Ana', 'zip_code': '92701', 
'country': 'US', 'state': 'CA', 'display_address': ['201 E 4th St', 'Santa Ana, CA 92701']}, 'phone': '+19496100869', 
'display_phone': '(949) 610-0869', 'distance': 10269.638681410985}, {'id': 'Xf8VQK4UMbDcCErOgD__gA', 
'alias': 'world-class-pizza-mission-viejo', 'name': 'World Class Pizza', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/U_LsuW_tnz08a8f9uGcNBQ/o.jpg', 
'is_closed': False, 'url': 'https://www.yelp.com/biz/world-class-pizza-mission-viejo?adjust_creative=QkCWE7HoAg6T9MbS75HNlQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=QkCWE7HoAg6T9MbS75HNlQ', 
'review_count': 172, 'categories': [{'alias': 'pizza', 'title': 'Pizza'}, {'alias': 'salad', 'title': 'Salad'}, {'alias': 'sandwiches', 'title': 'Sandwiches'}], 'rating': 3.0, 
'coordinates': {'latitude': 33.55423, 'longitude': -117.6709118}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 
'location': {'address1': '28171 Marguerite Parkway', 'address2': 'Ste 25', 'address3': '', 'city': 'Mission Viejo', 
'zip_code': '92691', 'country': 'US', 'state': 'CA', 'display_address': ['28171 Marguerite Parkway', 'Ste 25', 'Mission Viejo, CA 92691']}, 
'phone': '+19494520388', 'display_phone': '(949) 452-0388', 'distance': 17882.479496349228}]

#Ask user for new or visited resturant
# new_old = input("Do you want to go to a new resturant or one you've visited\nPress N = New and O = Old")

# #Finding a new resturant
# if new_old == 'N':
#     param_dict = {}
#     general = input("What food, cuisine, drink, etc. are you thinking about?")
#     param_dict['term'] = general
#     location = input("What city?\n")
#     param_dict['location'] = location
#     distance_miles = int(input("How many miles are you willing to drive?(max 24)\n"))
#     distance_meters = distance_miles * 1609
#     param_dict['radius'] = distance_meters
#     price = input("How pricey from 1-4?(1 = cheapest, 4 = most expenive")
#     param_dict['price'] = price
#     param_dict['open_now'] = True
#     attributes = ""
#     trendy = input("Something trendy?(Press Y or N)\n")
#     if trendy == 'Y':
#         attributes += "hot_and_new"
#         param_dict['attributes'] = attributes
#     reservation = input("Something that needs a reservation?(Press Y or N)\n")
#     if reservation == 'Y':
#         if attributes != "":
#             attributes += ",reservation"
#             param_dict['attributes'] = attributes
#         else:
#             attributes += "reservation"
#             param_dict['attributes'] = attributes
#     pickup = input('Do you want pickup?(Press Y or N)')
#     delivery = input('Do you want delivery?(Press Y or N)')

#     results = Yelp.businessSearch(param_dict)
#     # print(results)
#     # decision = 'Y'
#     #Iterate and filter resturants that will be shown to the user to decide 
#     #Filtered resturants will be shown one by one until user decides yes("Y"), then loop will break
#     #Resturant data will be saved in user's visited resturant list
#     for result in results['businesses']:
#         if (result['id'] not in resto_list):
#             if pickup == 'Y':
#                 if 'pickup' in result['transactions']:
#                     print(result['name'], result['image_url'])
#                     decision = input('Yes or No?(Press Y or N)')
#                     if decision == 'Y':
#                         resto_list.append(result)
#                         print(resto_list)
#                         break
#                 else:
#                     continue
#             if delivery == 'Y':
#                 if 'delivery' in result['transactions']:
#                     print(result['name'], result['image_url'])
#                     decision = input('Yes or No?(Press Y or N)')
#                     if decision == 'Y':
#                         resto_list.append(result)
#                         print(resto_list)
#                         break
#                 else:
#                     continue
#             else:
#                 print(result['name'], result['image_url'])
#                 decision = input('Yes or No?(Press Y or N)')
#                 if decision == 'Y':
#                     resto_list.append(result)
#                     print(resto_list)
#                     break

# #Asking user preferences to help filter thru iser's visited resturant list
# if new_old == 'O':
#     ranking_dict = {}
#     gen_multiplier = 5
#     location_multiplier = 5
#     rating_multiplier = 6
#     general = input("What food, cuisine, drink, etc. are you thinking about?")
#     location = input("What city?\n")
#     distance_miles = int(input("How many miles are you willing to drive?(max 25)\n"))
#     distance_meters = distance_miles * 1609
#     distance_mulitplier = int(input('On a scale of 1-5 how important is this to you?'))
#     price = input("How pricey from 1-4?(1 = cheapest, 4 = most expenive")
#     price_mulitplier = int(input('On a scale of 1-5 how important is this to you?'))
#     reservation = input("Something that needs a reservation?(Press Y or N)\n")
#     reservation_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
#     pickup = input('Do you want pickup?(Press Y or N)')
#     pickup_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
#     delivery = input('Do you want delivery?(Press Y or N)')
#     delivery_multiplier = int(input('On a scale of 1-5 how important is this to you?'))

#     #Calculate score for each resturant and store as value in dictionary {resturant:score}
#     for resto in resto_list:
#         param_dict = {'name':resto['name'], 'location':resto['location']['address1'], 'limit':1}
#         #find way around making API call
#         biz_data = Yelp.businessSearch(param_dict)
#         for biz in biz_data['businesses']:
#             score = 0
#             score += biz['rating'] * rating_multiplier * (biz['review_count'] / 100)
#             if general in biz['alias']:
#                 score += gen_multiplier
#             if location == biz['location']['city']:
#                 score += location_multiplier
#             if abs(distance_meters - biz['distance']) <= 1609:
#                 score += distance_mulitplier
#             if price == len(biz['price']):
#                 score += price_mulitplier
#             if reservation == 'Y':
#                 if 'resturant_reservation' in biz['transactions']:
#                     score += reservation_multiplier
#                 else:
#                     continue
#             if reservation == 'N':
#                 if 'resturant_reservation' not in biz['transactions']:
#                     score += reservation_multiplier
#             if pickup == 'Y':
#                 if 'pickup' in biz['transactions']:
#                     score += pickup_multiplier
#                 else:
#                     continue
#             if pickup == 'N':
#                 if 'pickup' not in biz['transactions']:
#                     score += pickup_multiplier
#             if delivery == 'Y':
#                 if 'delivery' in biz['transactions']:
#                     score += delivery_multiplier
#                 else:
#                     continue
#             if delivery == 'N':
#                 if 'delivery' not in biz['transactions']:
#                     score += delivery_multiplier
#             ranking_dict[biz['name']] = score
#     sorted_ranking_dict = dict(sorted(ranking_dict.items(), key=lambda item: item[1], reverse=True))

#     #Iterate and filter resturants that will be shown to the user to decide 
#     #Filtered resturants will be shown one by one until user decides yes("Y"), then loop will break
#     for name in sorted_ranking_dict.keys():
#         print(name)
#         decision = input('Yes or No?(Press Y or N)')
#         if decision == 'Y':
#             break
#     print(sorted_ranking_dict)
    
            
            

#             # print(biz['name'])
#             # print(biz['distance'])
#             # print(biz['is_closed'])
#             # print(biz['transactions'])




#         # biz_data = Yelp.businessMatch(param_dict)
#         # print(biz_data)

#Gathering user prefernces for a new resturant
def get_new_inputs():
    param_dict = {}
    general = input("What food, cuisine, drink, etc. are you thinking about?")
    param_dict['term'] = general
    location = input("What city?\n")
    param_dict['location'] = location
    distance_miles = int(input("How many miles are you willing to drive?(max 24)\n"))
    distance_meters = distance_miles * 1609
    param_dict['radius'] = distance_meters
    price = int(input("How pricey from 1-4?(1 = cheapest, 4 = most expenive"))
    price_str = ''
    for i in range(1, price + 1):
        if i != price:
            price_str += str(i) + ', '
        else:
            price_str += str(i)
    param_dict['price'] = price_str
    param_dict['open_now'] = True
    attributes = ""
    trendy = input("Something trendy?(Press Y or N)\n")
    if trendy == 'Y':
        attributes += "hot_and_new"
        param_dict['attributes'] = attributes
    reservation = input("Something that needs a reservation?(Press Y or N)\n")
    if reservation == 'Y':
        if attributes != "":
            attributes += ",reservation"
            param_dict['attributes'] = attributes
        else:
            attributes += "reservation"
            param_dict['attributes'] = attributes
    pickup = input('Do you want pickup?(Press Y or N)')
    param_dict['pickup'] = pickup
    delivery = input('Do you want delivery?(Press Y or N)')
    param_dict['delivery'] = delivery
    return param_dict

#Gathering user prefernces for a previously visted resturant
def get_old_inputs():
    param_dict = {}
    general = input("What food, cuisine, drink, etc. are you thinking about?")
    param_dict['general'] = general
    location = input("What city?\n")
    param_dict['location'] = location
    distance_miles = int(input("How many miles are you willing to drive?(max 25)\n"))
    distance_meters = distance_miles * 1609
    param_dict['distance'] = distance_meters
    distance_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
    param_dict['distance_multiplier'] = distance_multiplier
    price = input("How pricey from 1-4?(1 = cheapest, 4 = most expenive")
    param_dict['price'] = price
    price_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
    param_dict['price_multiplier'] = price_multiplier
    reservation = input("Something that needs a reservation?(Press Y or N)\n")
    param_dict['reservation'] = reservation
    reservation_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
    param_dict['reservation_multiplier'] = reservation_multiplier
    pickup = input('Do you want pickup?(Press Y or N)')
    param_dict['pickup'] = pickup
    pickup_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
    param_dict['pickup_multiplier'] = pickup_multiplier
    delivery = input('Do you want delivery?(Press Y or N)')
    param_dict['delivery'] = delivery
    delivery_multiplier = int(input('On a scale of 1-5 how important is this to you?'))
    param_dict['delivery_multiplier'] = delivery_multiplier
    return param_dict

#Iterate through resturant results given by API call made by Yelp class to make a filtered resturant list that will be shown to the user one by one for them decide on
def find_new_restaurants(params):
    pickup = params.pop('pickup')
    delivery = params.pop('delivery')
    results = Yelp.businessSearch(params)
    for result in results['businesses'].copy():
        if result['id'] in resto_list or (pickup == 'Y' and 'pickup' not in result['transactions']) or (delivery == 'Y' and 'delivery' not in result['transactions']):
            results['businesses'].remove(result)
    return results

#Calculate score for each resturant and store as value in dictionary {resturant:score} then sort the dictionary by decending values 
def find_old_restaurants(params):
    ranking_dict = {}
    gen_multiplier = 5
    location_multiplier = 5
    rating_multiplier = 6
    for resto in resto_list:
        score = 0
        score += resto['rating'] * rating_multiplier * (resto['review_count'] / 100)
        if params['general'] in resto['alias']:
            score += gen_multiplier
        if params['location'] == resto['location']['city']:
            score += location_multiplier
        if abs(params['distance'] - resto['distance']) <= 1609:
            score += params['distance_multiplier']
        if params['price'] == len(resto['price']):
            score += params['price_multipler']
        if params['reservation'] == 'Y':
            if 'resturant_reservation' in resto['transactions']:
                score += params['reservation_multiplier']
            else:
                continue
        if params['reservation'] == 'N':
            if 'resturant_reservation' not in resto['transactions']:
                score += params['reservation_multiplier']
        if params['pickup'] == 'Y':
            if 'pickup' in resto['transactions']:
                score += params['pickup_multiplier']
            else:
                continue
        if params['pickup'] == 'N':
            if 'pickup' not in resto['transactions']:
                score += params['pickup_multiplier']
        if params['delivery'] == 'Y':
            if 'delivery' in resto['transactions']:
                score += params['delivery_multiplier']
            else:
                continue
        if params['delivery'] == 'N':
            if 'delivery' not in resto['transactions']:
                score += params['delivery_multiplier']
        ranking_dict[resto['name']] = score
    sorted_ranking_dict = dict(sorted(ranking_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_ranking_dict

#Filtered resturants will be shown one by one until user decides yes("Y"), then loop will break
#Resturant data will then be saved in user's visited resturant list
def display_new_results(results):
    for result in results['businesses']:
        print(result['name'], result['image_url'])
        decision = input('Yes or No?(Press Y or N)')
        if decision == 'Y':
            resto_list.append(result)
            print(resto_list)
            break

#Filtered resturants will be shown one by one, in the order of the sorted decending value dictionary, until user decides yes("Y"), then loop will break
def display_old_results(results):
    for name in results.keys():
        print(name)
        decision = input('Yes or No?(Press Y or N)')
        if decision == 'Y':
            break



def main():
    new_old = input("Do you want to go to a new resturant or one you've visited\nPress N = New and O = Old ")
    if new_old == 'N':
        params = get_new_inputs()
        results = find_new_restaurants(params)
        display_new_results(results)
    else:
        params = get_old_inputs()
        results = find_old_restaurants(params)
        display_old_results(results)

if __name__ == '__main__':
    main()