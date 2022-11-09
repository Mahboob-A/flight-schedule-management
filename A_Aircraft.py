"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.00 pm 
A_Aircraft
"""

class Aircraft:
        def __init__(self, aircraft_code, aircraft_type, aircraft_manufacturer, aircraft_range) -> None:
                self.aircraft_code = aircraft_code
                self.aircraft_type = aircraft_type 
                self.aircraft_manufacturer = aircraft_manufacturer
                self.aircraft_range = int(aircraft_range)

        def __repr__(self) -> str:
                return f'AIRCRAFT: Code {self.aircraft_code} | Type: {self.aircraft_type} | Manufacturer: {self.aircraft_manufacturer} | Range: {self.aircraft_range}'