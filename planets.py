planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(0, 'Earth')
planet_list.insert(0, 'Venus')
#Pluto is a Planet, science is wrong!!!
planet_list.append('Pluto')
# print(planet_list)
rock_planet_list = []
rock_planet_list=planet_list[:4]
# print(rock_planet_list)

#Science will prevail!!!!!!!!!!
del planet_list[-1]
# print(planet_list)


#Challenge

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Pioneer 10", "Jupiter"),
   ("Pioneer 11", "Saturn"),
   ("Voyager", "Jupiter"),
   ("Voyager", "Saturn"),
   ("Voyager", "Uranus"),
   ("Voyager", "Neptune"),
   ("BepiColombo", "Mercury"),
   ("Messenger", "Mercury"),
   ("Venus Express", "Venus"),
   ("Magellan", "Venus"),
   ("Akatsuki", "Mars")

]

for planet in planet_list:
    missions = []
    for crafts in spacecraft:
        if crafts[1]==planet:
            missions.append(crafts[0])
    if len(missions) == 0:
        print(f'Looks like no recorded missions on {planet} yet lol we live here.')
    else:
        print(f"{planet}'s missions are: {missions}'")
