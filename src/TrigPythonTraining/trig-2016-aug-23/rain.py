#!/usr/bin/env python

rain = { }

while True:
    city_name = raw_input("Enter a city: ").strip()

    if not city_name:
        break

    mm_rain = int(raw_input("Enter rain: "))

    rain[city_name] = rain.get(city_name, 0) + mm_rain

for city, rainfall in rain.items():
    print "{}: {}".format(city, rainfall)

# # Ask the user for a city name
# # If the city name is blank, exit the program

# # If the city name is not blank, as mm rain

# City: A
# Rain: 5
# City: B
# Rain: 7
# City: A
# Rain: 10
# City: [blank]

# # When we exit from the program, this report should be written
# Totals:
# A: 15
# B: 7

