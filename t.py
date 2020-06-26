states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

states['Georgia'] = 'GA'
states['New Jersey'] = 'NJ'

cities = {
    'CA': 'San Francisco',
    'GA': 'Atlanta',
    'NJ': 'Newark',
    'MI': 'Detroit'
}

state = states.get("Georgia")
print(state)


# print("California has " + cities['CA'])
# print('New Jersey\'s abbrev. is ' + states['New Jersey'])
# print('Michigan has: ' + cities[states['Michigan']])
# print('Michigan has: ' + cities[states['Michigan']])
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

print("\n-" * 5 + "\n")

for state, abbrev in cities.items():
    print(f"{state} has the city {abbrev}")
# def returnKeysValues():
#     for i,(k,v) in enumerate(states.items()):
#         print(i+1,k,v)

# returnKeysValues()
