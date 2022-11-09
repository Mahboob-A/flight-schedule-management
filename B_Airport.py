"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.15 pm
B_Airpor
"""

class Airport:
        def __init__(self, airport_name, airport_code, airport_city, airport_country, airport_lat, airport_lon, currency_rate) -> None:
                self.airport_name = airport_name
                self.airport_code = airport_code
                self.airport_city = airport_city
                self.airport_country = airport_country
                self.airport_lat = float(airport_lat)
                self.airport_lon = float(airport_lon)
                self.currency_rate = currency_rate

        def __repr__(self) -> str:
                return f'AIRPORT: Code: {self.airport_code} | City: {self.airport_city} | Country: {self.airport_country} | Lat: {self.airport_lat} | Lon: {self.airport_lon}'
