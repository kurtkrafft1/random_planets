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
print(planet_list)