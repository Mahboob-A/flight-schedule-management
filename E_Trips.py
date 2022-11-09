"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.25 pm
E_Trips 07.10 pm 
"""

class Trip:
        def __init__(self, aircraft, start_date, trip_fare, trip_distance, trip_cities_list="") -> None:
                self.aircraft = aircraft
                self.start_date = start_date
                self.trip_fare = trip_fare
                self.trip_distance = trip_distance
                self.trip_cities_list = trip_cities_list

        def __repr__(self) -> str:
                return f'TRIP: {self.aircraft}\nStart Date: {self.start_date} | Trip Fare: {self.trip_fare} | Trip Distance: {self.trip_distance} | Trip Cities: {self.trip_cities_list}   '