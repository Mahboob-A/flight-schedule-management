""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 03.15 pm
21-5 Python main function and Handle Error
"""

from G_TravelAgent import TravelAgent

def main():
        travel_agent = TravelAgent('Kemal')


        trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '081122')   
        # print(f"\nAircraft Info:  --- {trip_info1[0]} \nFare: --- {trip_info1[1]} | Distance: --- {trip_info1[2]}\n")

        # trip_info3 = travel_agent.set_trip_multi_city_one_way_fixed_route('DAC', '08/11/22')

        trip_cities = ['DUB', 'LHR', 'SYD', 'JFK', 'CCU']
        trip_dates = ['08/11/22', '15/11/22', '08/11/32', '12/01/2030']  #today is 081122, Tuesday. let's see, if Allah allows me to live, I will see where I am in 08/11/32, 10 years later! 

        trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities, trip_dates)
        print("Total Fare:  ", trip_info2[1])
        print("Minimum Fare: ", trip_info2[2])
        for trip in trip_info2[0]:
                print(trip)








if __name__ == '__main__':
        main()