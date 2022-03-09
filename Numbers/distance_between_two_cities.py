from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geoLocator = Nominatim(user_agent="mini_tasks")


def distance_between_two_cities(city1: str, city2: str, unit: str) -> float:
    try:
        loc1 = (geoLocator.geocode(city1).latitude, geoLocator.geocode(city1).longitude)
        loc2 = (geoLocator.geocode(city2).latitude, geoLocator.geocode(city2).longitude)
        if unit == "mile":
            return float("{:.2f}".format(geodesic(loc1, loc2).miles))
        elif unit == 'km':
            return float("{:.2f}".format(geodesic(loc1, loc2).km))
        else:
            raise AttributeError
    except Exception as e:
        raise e


