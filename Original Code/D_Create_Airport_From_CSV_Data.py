""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-1 Module Introduction and previous module recap
"""


# creating airports from the csv data. See C_All_Airports D part is implemented there 
# main other working is in C_ALl_Airport is done 
""" 
Mod Date: 051122, Saturday
Watch Date: 061122, Sunday, 09.15 pm
20-3 Load airport data from csv
"""

import csv 
from A_Airport import Airport

class AllAirports:

        def __init__(self) -> None:
                self.airports = None 
                self.load_airport_data('./data/airport_data.csv')
        
        def load_airport_data(self, file_path): 
                airports = {}
                with open(file_path, 'r', encoding='utf8') as file:
                        lines = csv.reader(file)
                        # creating airport objects from csv file. Making the airport code as key and the object of airport class as the value 
                        for line in lines:  
                                airports[line[4]] = Airport(line[1], line[2], line[3], line[4], line[6], line[7], 0)

                self.airports = airports 
                for airport in self.airports.values():
                        print(airport)

                               


AllAirports()

