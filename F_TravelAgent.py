"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.25 pm
F_TravelAgent 07.10 pm 
"""



from C_All_Airports import AllAirports
from D_All_Airlines import AllAirlines
from E_Trips import Trip

class TravelAgent:
        def __init__(self, agentName) -> None:
                self.agentName = agentName
                self.agentTrips = {}    # make the agent name as key and add the trip object so that agent can keep a track of how many trips he has booked 
                self.air_ports = AllAirports()
                self.air_lines = AllAirlines()

        def set_trip_one_city_one_way(self, start_code, end_code, start_date):
                airport1 = self.air_ports.get_airport(start_code)
                airport2 = self.air_ports.get_airport(end_code)
                distance = self.air_ports.distance_calculation(start_code, end_code)
                aircraft = self.air_lines.get_aircraft_by_distance(distance)
                fare = self.air_ports.ticket_price(start_code, end_code)
                trip = Trip(aircraft, start_date, fare, distance, [airport1.airport_city, airport2.airport_city])
                return trip 

        

