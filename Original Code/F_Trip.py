""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-1 Module Introduction and previous module recap
"""

class Trip:
        def __init__(self, aircraft_obj, start_date, trip_fare, trip_distance, route_cities_list = '') -> None:
                self.aircraft_obj = aircraft_obj
                self.start_date = start_date
                self.trip_distance = trip_distance
                self.trip_fare = trip_fare
                self.route_cities_list = route_cities_list

        def __repr__(self) -> str:
            return f'Trip Route: {self.route_cities_list} | {self.aircraft_obj} | Start Date: {self.start_date} | Trip Fare: {self.trip_fare} | Distance: {self.trip_distance}'
        