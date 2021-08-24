import json
import string
import time

JSON_Base_Path = "./static/JSON/"

# Paths
Countries_JSON_path = JSON_Base_Path + "Countries.json"
Countries_JSON_path_new = JSON_Base_Path + "Countries_new.json"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Utility Functions
#

def Open_JSON( File_Location ):
    
    with open( File_Location, "r", encoding="utf-8" ) as JSON_RAW_INFO:

        JSON_DATA = json.load( JSON_RAW_INFO )

    return JSON_DATA

def Save_JSON( JSON, filename, indent ):
    # open(filename, 'a', encoding="utf-8")

    #print(json.dump(
    #JSON))

    out_file = open( filename, "w", encoding="utf-8" ) 
    
    # print( "Before Dump" )

    if( indent == None ):
        json.dump( JSON, out_file ) 
    if( indent == 4 ):
        json.dump( JSON, out_file, indent = 4 ) 
    
    # print( "After Dump" )
 
    out_file.close()
    
    return "Success!!!"

def Get_Countries( ):
    return Countries_JSON
#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Initilization
#

# Ran at begining of the Application to initilize the objects
def Initialize_OBJS(  ):
    global Countries_JSON
    print( "\n\nPre-Initilization\n\n" )
    Countries_JSON = Open_JSON( Countries_JSON_path )
    
    print( "Initilization Done!!!" )
    # Check later!
    #global Milage_To_Vendors_JSON
    #Milage_To_Vendors_JSON = Open_JSON( Milage_To_Vendors_JSON_path )
    
    #global UPC_ITEMS_JSON 
    #UPC_ITEMS_JSON = Open_JSON( UPC_ITEMS_JSON_path )

Initialize_OBJS()
#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Use Functions / In application functions
#

def Get_Country_Names(  ):
    print( "Inside: Get_Country_Names(  )" )
    All_Countries_Names = []
    for Country in Countries_JSON['Countries']:
        All_Countries_Names.append( Country['name'] )

    return All_Countries_Names
#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Test Area
#


#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
