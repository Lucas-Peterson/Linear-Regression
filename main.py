import datacommons_pandas as dc

usa = 'country/USA'

cities = dc.get_places_in([usa], 'City')[usa]
'''
cities_within = dc.get_places_in(cities, "State")

test = dc.get_places_in(["geoId/10"], "County")

print(test)
'''
'''
cities_value = dc.get_property_values(["geoId/10"], 'containedInPlace')

print(cities_value)
'''

cities_label = dc.get_property_labels(cities, out=True)

print(cities_label)
