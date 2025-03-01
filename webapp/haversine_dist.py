
import math

def distance(origin, destination):
    lat1, lon1 = origin[0],origin[1]
    lat2, lon2 = destination[0],destination[1]
    radius = 6371 # km

    lat1=float(17.4501036)
    lon1=float(78.4309667)
    lat2 = float(lat2)
    lon2 = float(lon2)

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

if __name__ == '__main__':
	origin=[17.4501036,78.4309667]
	destination=[17.465118298519194,78.42991959671778]

	print(distance(origin,destination))