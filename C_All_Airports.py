"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.25 pm
C_All_Airports 
"""

from csv import reader
from B_Airport import Airport 
from geopy import distance

class AllAirports:
        def __init__(self) -> None:
                self.airports = None 
                self.load_airport_data('./data/countrycurrency.csv', './data/currencyrates.csv', './data/airport_data.csv')

        def load_airport_data(self, country_currency_file_path, country_rates_file_path, airport_data_file_path):
                Airports = {}
                CountryName_CurrenyCode = {}
                CurrencyCode_CurrencyRate = {}

                # getting the countryname and currency name in dict | country name as key and currency code as value 
                with open(country_currency_file_path, 'r', encoding='utf8') as file:
                        lines = reader(file)
                        next(lines)
                        for line in lines:
                                CountryName_CurrenyCode[line[0]] = line[1]

                # getting the country name and currency rate in dict | country code as key, rate as value 
                with open(country_rates_file_path, 'r', encoding='utf8') as file:
                        lines = reader(file)
                        for line in lines:
                                CurrencyCode_CurrencyRate[line[1]] = line[2]

                # getting the airport data, and creating the airport object, making the country code as key and the airport object as value to the Airports dict 
                with open(airport_data_file_path, 'r', encoding='utf8') as file:
                        lines = reader(file)

                        try:
                                for line in lines:
                                        country_name = line[3]
                                        if country_name not in CountryName_CurrenyCode:
                                                continue 
                                        currency_code = CountryName_CurrenyCode.get(country_name, 'Country Name Not Found In COUNTRYCURRENCY FILE')
                                        if currency_code not in CurrencyCode_CurrencyRate:
                                                continue 
                                        currency_rate = CurrencyCode_CurrencyRate.get(currency_code, 'Currency Code Not Found In COUNTRY RATE FILE')
                                        Airports[line[4]] = Airport(line[1], line[4], line[2], line[3], line[6], line[7], float(currency_rate)) 
                        except KeyError as e:
                                print("KeyError From C_AllAirports:  ", e)

                self.airports = Airports
                # for airport in self.airports.values():
                #         print(airport) 

        # using geopy module 
        def distance_calculation(self, airport1_code, airport2_code):
                airport1 = self.airports.get(airport1_code, 'C_ALL_AIRPORTS: Airport Code Not Found (Distance Calculation)')
                airport2 = self.airports.get(airport2_code, 'C_ALL_AIRPORTS: Airport Code Not Found (Distance Calculation)')
                the_distance = distance.distance((airport1.airport_lat, airport1.airport_lon), (airport2.airport_lat, airport2.airport_lon)).km
                return the_distance #returning distance in km 

        def ticket_price(self, airport1_code, airport2_code):
                distance = self.distance_calculation(airport1_code, airport2_code)
                airport1 = self.airports.get(airport1_code, 'C_ALL_AIRPORTS: Airport Code Not Found (Ticket Price)')
                fare = airport1.currency_rate * distance 
                return fare 

        def get_airport(self, airport_code):
                if airport_code in self.airports:
                        return self.airports[airport_code]
                else:
                        print("This {} Code is invalid".format(airport_code))




if __name__ == '__main__':
        AllAirports()
