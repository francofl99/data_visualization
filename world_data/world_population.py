import json
from pygal.maps.world import World


def get_country_code(country_name, codes_and_names):
    """Return the Pygal 2-digit country code for the given country."""
    
    for each_code, each_name in codes_and_names.items():
        if country_name == each_name:
            return each_code
       
    return None

def get_country_list():
    filename = 'country_list.txt'
    codes_and_names = {}
    with open(filename) as f:
        for line in f.readlines():
            code = line[0:2]
            name = line[3:len(line)].strip()
            codes_and_names[code] = name

    return codes_and_names
    
def make_world_map():
    # Load the data into a list
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)
    # Get the two digits cuntries codes
    codes_and_names = get_country_list()
    # Build a dictionary of population data
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name, codes_and_names)
            if code:
                cc_populations[code] = population
    # Make world map        
    wm = World()
    wm.title = 'World population in 2010, by Country'
    wm.add('2010', cc_populations)
    # Convert it to file 
    wm.render_to_file("world_population.svg")

make_world_map()


