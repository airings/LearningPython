report = {}
while True:
    city = raw_input("City: ").strip()

    if not city:
        break
        
    rain = int(raw_input("Rain: "))
    curRain = report.get(city, 0) # Key not exsited, get 0
    # curRain = report[city] # keyError exception
    report[city] = curRain + rain

print report