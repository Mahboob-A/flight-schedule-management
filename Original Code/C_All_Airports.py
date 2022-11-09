""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-1 Module Introduction and previous module recap
"""

import csv
# importing the airport class form A_Airport file / module
from A_Airport import Airport
from math import sqrt, sin, cos, atan2, radians


class AllAirports:

        def __init__(self) -> None:
                self.airports = None
                self.load_airport_data('./data/currencyrates.csv','./data/countrycurrency.csv', './data/airport_data.csv')

        def load_airport_data(self, currencyrate_file_path, countrycurrency_file_path, airport_file_path):
                # airport code as key and Airport object as value
                Airports = {}

                # from currencyrates.csv | making the currency code as key and currency rate as value
                currencyCode_CurrencyRate = {}

                # from countrycurrency.csv | making the country name as key and currency code as value
                countryName_CurrencyCode = {}

                # makaing relation with currency code <---> currency rate
                with open(currencyrate_file_path, 'r', encoding='utf8') as file:
                        lines = csv.reader(file)

                        for line in lines:
                                # currency code as key and currency rate as value
                                currencyCode_CurrencyRate[line[1]] = line[2]

                # making relation with country name <---> currency code
                with open(countrycurrency_file_path, 'r', encoding='utf8') as file:
                        lines = csv.reader(file)
                        header = next(lines)
                        for line in lines:
                                # making the country name as key and country code as value
                                countryName_CurrencyCode[line[0]] = line[1]

                with open(airport_file_path, 'r', encoding='utf8') as file:
                        lines = csv.reader(file)
                        # handling errors with try catch
                        try:
                                # creating airport objects from csv file. Making the airport code as key and the object of airport class as the value
                                for line in lines:
                                        # getting the country name
                                        country_name = line[3]   
                                        # if country name is not found in country_currency dict, then continue 
                                        if country_name not in countryName_CurrencyCode: 
                                                print(f"CONTINUE: country_name --- {country_name} not found in airport csv file")
                                                continue   
                                        # getting the currency code
                                        country_currency_code = countryName_CurrencyCode.get(country_name, f'No Country With {country_name} Found in countryName_CurrencyCode')
                                        if country_currency_code not in currencyCode_CurrencyRate:
                                                print(f"CONTINUE: country_currency_code --- {country_currency_code} not found in CrrencyRate csv file")
                                                continue
                                        # getting the currency rate
                                        country_currency_rate = currencyCode_CurrencyRate[country_currency_code]
                                        Airports[line[4]] = Airport(line[1], line[2], line[3], line[4], line[6], line[7], country_currency_rate)
                        except KeyError as e:
                                print("KeyError Form C_All_Airports: ", e)
                self.airports = Airports

                # for airport in self.airports.values():
                #         print(airport)  # printing the airports
                # for airport in countryName_CurrencyCode.items():
                #         print(airport)  # printing the airports

        
        # see formula page for formula related informations 
        def distance_calculation(self, lat1, lon1, lat2, lon2):
                radius = 6371
                lat_diff = radians(lat2 - lat1)
                lon_diff = radians(lon2 - lon1)
                a = (sin(lat_diff / 2) * sin(lat_diff / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(lon_diff / 2) * sin(lon_diff / 2))
                arc = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = radius * arc 
                return distance 

        # passing the code of two airport 
        def distance_between_two_airports(self,airport1_code, airport2_code):
                airport1 = self.airports[airport1_code]   # getting the airport objct from self.airports dict using airport code 
                airport2 = self.airports[airport2_code]
                two_airport_distance = self.distance_calculation(airport1.lat, airport1.lon, airport2.lat, airport2.lon)
                return two_airport_distance 

        def get_ticket_price(self, airport1_code, airport2_code):
                distance = self.distance_between_two_airports(airport1_code, airport2_code)
                airport1 = self.airports[airport1_code]
                fare = distance * airport1.rate 
                return fare 

if __name__  == '__main__':
        airport_authority = AllAirports()
        fare = airport_authority.get_ticket_price('DAC', 'PRA')

        print("Fare is : ", fare)