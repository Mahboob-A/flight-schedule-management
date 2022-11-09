""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
"""

from A_Aircraft import Aircraft
from csv import reader 

class Airlines:
        def __init__(self) -> None:
                self.air_crafts = None 
                self.load_aircrafts_data('./data/aircraft.csv')

        def load_aircrafts_data(self, aircraft_file_path):
                Aircrafts = {}
                with open(aircraft_file_path, 'r') as file:
                        lines = reader(file)
                        next(lines)
                        for line in lines:
                                Aircrafts[line[0]] = Aircraft(line[0], line[1], line[3], line[4])

                self.air_crafts = Aircrafts
                # for airplane in self.air_crafts.values():
                #         print(airplane)

        def get_aircraft(self, aircraft_code):
                if aircraft_code in self.air_crafts:
                        return self.air_crafts[aircraft_code]
                else:
                        print("The aircraft code in invalid")

        def get_aircraft_by_diatance(self, distance):
                for aircraft in self.air_crafts.values():
                        # print("E_Airlines: distance:  ", distance)
                        # print("flight_range:  ", aircraft.flight_range)
                        if aircraft.flight_range > distance:
                                # print(f"Suitable aircraft found:  flight_range = {aircraft.flight_range} | distance = {distance}")
                                return aircraft 
                        # else:
                        #         print("No suitable aircraft is found. Distance is too large for aircraft range")

if __name__ == '__main__':
        Airlines()        
        

