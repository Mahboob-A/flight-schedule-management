""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-2 Create Trave Agent and multiple trip options
"""



from E_Airlines import Airlines
from C_All_Airports import AllAirports
from F_Trip import Trip
from itertools import permutations 

class TravelAgent:
        def __init__(self, name) -> None:
                self.name = name
                self.trips = None
                self.air_ports = AllAirports()
                self.air_lines = Airlines()

        def __repr__(self) -> str:
                return f'Travel Agent Name:  {self.name} | Trips: {self.trips}'

        """  ############ start_code or end_code or trip_cities or trip_info_list contains Airport Code ### 
                start_code = city code beginning (airport code)
                end_code = city code destination 
                start_date = journey date 

                return aircraft and price 
        """
        # returns an object of Trip class
        # returns Trip class object
        # one city, one way
        def set_trip_one_city_one_way(self, start_code, end_code, start_date):
                distance = self.air_ports.distance_between_two_airports(start_code, end_code)
                fare = self.air_ports.get_ticket_price(start_code, end_code)
                aircraft_by_close_distance = self.air_lines.get_aircraft_by_diatance(distance)
                new_trip = Trip(aircraft_by_close_distance, start_date, fare, distance, [start_code, end_code])
                return new_trip

        #  One City, Round Way
        # one city, return way | Taking variable as parameter
        def set_trip_one_city_round_way(self, start_code, end_code, start_date, return_date):
                trip_obj_1 = self.set_trip_one_city_one_way(start_code, end_code, start_date)
                trip_obj_2 = self.set_trip_one_city_one_way(end_code, start_code, return_date)
                return [trip_obj_1, trip_obj_2]

        """  
                trip_info_list: [city_code_1, city_code_2, city_code_3]  #taking a list 
                rerturns a list of two trip objects |
        """
        # taking list as parameter to demonstrate iterable can be taken as parameter
        def set_trip_two_city_one_way(self, trip_info_list, start_date_list):
                trip_obj_1 = self.set_trip_one_city_one_way(trip_info_list[0], trip_info_list[1], start_date_list[0])
                trip_obj_2 = self.set_trip_one_city_one_way(trip_info_list[1], trip_info_list[2], start_date_list[1])
                return [trip_obj_1, trip_obj_2]

        """  
                trip_info_list: [city_code_1, city_code_2, city_code_3, city_code_4, city_code_5] X number city code
                start_date_list: [date1, date2, date3, date4]  X-1 date list 
                returns a list of X number trip objects 
        """

        def set_trip_multi_city_one_way(self, trip_info_list, start_date_list):
                all_trips = []
                if type(trip_info_list) != list and type(start_date_list) != list:
                        print("Must contain X number cities and X-1 number start date as list")
                else:
                        for i in range(0, len(trip_info_list)-1):   # running loop until the n-2th city 
                                trip = self.set_trip_one_city_one_way(trip_info_list[i], trip_info_list[i+1], start_date_list[i])
                                all_trips.append(trip)
                        # returns a list of X trip objects
                        return all_trips

        """  
                trip_info_list: [city_code_1, city_code_2, city_code_3, city_code_4, city_code_5]  X number city code 
                start_date_list: [date1, date2, date3, date4]  X number journey date 
                Here we will not hardcode which city to go after with, for this we will use permutation 
        """
        # trip_cities and trip_dates are list 
        def set_trip_multi_city_flexible_route(self, trip_cities_list, trip_dates_list):
                start_city = trip_cities_list[0]
                remaining_cities = trip_cities_list[1:]

                # explanation 
                # # making the permutation (possible rearrangement of the cities) of the cities 
                # for city_sequence_perm in permutations(remaining_cities):
                #         print(city_sequence_perm)  # city_sequence is the permution of the remaining cities list 
                #         # making a list with the permutation tuple with the starting city 
                #         # it will join the starting city with each permutation and form a list 
                #         joined_cities = [start_city] + list(city_sequence_perm)
                #         print(joined_cities)
                #         # for i in range(0, len(city_sequence_perm)):   this will iterate the tuple city_sequence_perm and print one by one 
                #         #         print(city_sequence_perm[i])

                min_fare = float('inf')
                selected_trips = None 
                for city_sequence in permutations(remaining_cities):
                        joined_cities = [start_city] + list(city_sequence)
                        joined_sequence_trip = self.set_trip_multi_city_one_way(joined_cities, trip_dates_list)  # receives a list of trips 
                        total_fare = 0 
                        for trip in joined_sequence_trip:
                                total_fare += trip.trip_fare # calculating the total fare of each permutation list 
                                if total_fare < min_fare:   # taking only the permutation list which has minimum fare 
                                        min_fare = total_fare 
                                        selected_trips = joined_sequence_trip

                total_fare_of_selected_trip = 0 
                for trip in selected_trips:
                       total_fare_of_selected_trip += trip.trip_fare
                self.trips = selected_trips # assigning the selected trips to the TravelAgent's self.trips attribute 
                return selected_trips, total_fare_of_selected_trip, min_fare   #returns a list of trips (Trip objects) total fare, and minimum fare for all the trips from the permutation trips 
                

                        














