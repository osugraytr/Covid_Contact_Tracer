from geopy.geocoders import Nominatim
from functools import partial

geolocator = Nominatim(user_agent="Covid_Tracker")

def Geocode_Partial( Address ):
    geocode = partial(geolocator.geocode, language="en")
    Results = geocode(Address)

    print(Results)

    return Results


def Geocode_Location_Based_Off_City( Address, Keys ):

    Results_JSON = {  }
    Results_JSON['Error'] = "Success"
    try:
        print("Test 1 - Start Geocode")
        print( "Finding:\t" + str( Address ) )
        
        Results_JSON['Address'] = str( Address )

        location = geolocator.geocode( str( Address ) )
        print("Test 2 - After Geocode")
        #print(location.address)
        #print((location.latitude, location.longitude)) 
        Temp_Results = print(location.raw)
        
        print("Test 3 - Before Key Assignment ")
        
        """
        print("Test 3.1 - Before Key Assignment: Address ")
        Results_JSON['lat'] = location.raw[Key]
        print("Test 3.2 - Before Key Assignment: lat ")
        Results_JSON['lng'] = location.raw['longitude']
        print("Test 3.3 - Before Key Assignment: lng ")
        Results_JSON['boundingbox'] = location.raw['boundingbox']
        print("Test 3.4 - Before Key Assignment: boundingbox ")
        """
        for Key in Keys:
             Results_JSON[ Key ] = location.raw[ Key ]

        print("Test 4 - After Key Assignment ")
    except:
            Results_JSON['Error'] = "Could not find Location"

    print("Test 5 - End Geocode")
    return Results_JSON