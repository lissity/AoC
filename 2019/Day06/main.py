def count_orbits(orbit_map, key):
    if(orbit_map[key] == 'COM'):
        return 1
    return count_orbits(orbit_map, orbit_map[key]) + 1

def get_orbit_path_to_COM(orbit_map, key):
    if(orbit_map[key] == 'COM'):
        return ['COM']
    return get_orbit_path_to_COM(orbit_map, orbit_map[key]) + [orbit_map[key]]

# Obtain input
input = [line.strip().split(')') for line in open('2019/Day06/input.txt','r').readlines()]
orbit_map = {}
for inp in input:
    orbit_map[inp[1]] = inp[0]

# First star
total_orbits = sum(count_orbits(orbit_map, planet) for planet in orbit_map.keys())
print('[part1] The total number of direct and indirect orbits are {}'.format(total_orbits))

# Second star
you_path = get_orbit_path_to_COM(orbit_map, 'YOU')[::-1]
san_path = get_orbit_path_to_COM(orbit_map, 'SAN')[::-1]
first_common_planet = next((planet for planet in you_path if planet in san_path))
orbital_transfers_req = you_path.index(first_common_planet) + san_path.index(first_common_planet)
print('[part2] The number of orbital transfers required is {}'.format(orbital_transfers_req))
