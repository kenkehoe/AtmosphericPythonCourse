from math import radians, cos, sin, asin, sqrt


def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the
    earth (specified in decimal degrees), returns the distance in
    kilometers.
    All arguments must be of equal length.

    Parameters
    ----------
    lon1 : float
        longitude of first place
    lat1 : float
        latitude of first place
    lon2 : float
        longitude of second place
    lat2 : float
        latitude of second place

    Returns
    -------
    distance in kilometers between the two sets of coordinates

    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2.)**2 + cos(lat1) * cos(lat2) * sin(dlon/2.)**2
    c = 2.0 * asin(sqrt(a))
    r = 6371.0  # Radius of earth in kilometers
    return c * r
