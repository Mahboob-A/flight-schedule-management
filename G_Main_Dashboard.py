"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.25 pm
G_MainDashboard 08.00 pm
"""

from F_TravelAgent import TravelAgent

class MainDashboard:
        def __init__(self) -> None:
                self.menu = TravelAgent('Kemal')

        def one_way_trip(self):
                # start_code, end_code, start_date = input("Input Airport Codes and Date:  ").split(" ")
                # trip = self.menu.set_trip_one_city_one_way(start_code, end_code, start_date)
                trip = self.menu.set_trip_one_city_one_way('DAC', 'PRA', '081122')
                print(trip)

menu = MainDashboard()
menu.one_way_trip()
                
