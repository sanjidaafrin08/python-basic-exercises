#Develop a program that takes two speeds (in km/h and mph), converts them to the same unit, and checks which one is faster
speed_kmh = float(input("Enter speed in km/h: "))
speed_mph = float(input("Enter speed in mph: "))
speed_mph_to_kmh = speed_mph * 1.60934
if speed_kmh > speed_mph_to_kmh:
    print(speed_kmh, "km/h is faster than", speed_mph, "mph.")
elif speed_kmh < speed_mph_to_kmh:
    print(speed_mph, "mph is faster than", speed_kmh, "km/h.")
else:
    print(speed_kmh, "km/h and", speed_mph, "mph are equal in speed.")