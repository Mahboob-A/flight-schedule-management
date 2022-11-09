""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-1 Module Introduction and previous module recap
"""

class Airport:
        def __init__(self, airport_name, airport_city, airport_country, airport_code, lat, lon,  rate) -> None:
                self.airport_name = airport_name
                self.airport_city = airport_city
                self.airport_country = airport_country
                self.airport_code = airport_code
                self.lat = float(lat)
                self.lon= float(lon)
                self.rate = float(rate)

        def __repr__(self) -> str:
                return f"Airport Name: {self.airport_name} | In City: {self.airport_city} | In Country: {self.airport_country} | Code: {self.airport_code} | Rate: {self.rate}"
