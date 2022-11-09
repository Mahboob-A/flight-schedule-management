"""  
Flight Simulator : Week 06 Mod 20 and 21 
091122, 04.25 pm
D_All_Airlines 07.00 pm 
"""

from A_Aircraft import Aircraft
from csv import reader 

class AllAirlines:
        def __init__(self) -> None:
                self.air_crafts = None 
                self.load_aircraft_data('./data/aircraft.csv')

        def load_aircraft_data(self, aircraft_file_path):
                Aircrafts = {}
                with open(aircraft_file_path, 'r', encoding='utf8') as file:
                        lines = reader(file)
                        next(lines)
                        for line in lines:
                                Aircrafts[line[0]] = Aircraft(line[0], line[1], line[3], line[4])
                        
                self.air_crafts = Aircrafts

                # for aircraft in self.air_crafts.values():
                #         print(aircraft)

        def get_aircraft(self, aircraft_code):
                if aircraft_code in self.air_crafts:
                        return self.air_crafts[aircraft_code]
                else:
                        print("This {} aircraft code is invalid".format(aircraft_code))
        
        def get_aircraft_by_distance(self, distance):
                for aircraft in self.air_crafts.values():
                        if aircraft.aircraft_range > distance:
                                return aircraft
                        


if __name__ == '__main__':
        AllAirlines()










