import pyowm

owm = pyowm.OWM("297c02ef6ccc603340b5a4071665604c")
observation = owm.weather_at_place("Jyväskylä,FI")
w = observation.get_weather()
wind = w.get_wind()
temperature = w.get_temperature('celsius')
print(temperature)
print(w)
print(wind)
