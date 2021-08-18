#( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )
# /
#/        
#
#------------------------------------------|
#    # Imported Libraries
#------------------------------------------|

# Added functionality to the Calculations. am close to having all variables needed to crunch numbers successfully just need CAse

from flask import Flask, render_template, request
import multiprocessing

#------------------------------------------|
#    # Import other python modules
#------------------------------------------|

import scripts.Contact_Trace_Stuff.Contact_Tracing_Functions as Contact_Tracing_Functions
import scripts.Map_Stuff.Map_Functions as Map_Functions

#
#\
# \
#( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /
#/        
#
#------------------------------------------|
#    # Flask Application
#------------------------------------------|

app = Flask(__name__)

#
#\
# \
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#===========================================
# /
#/        Global Variables
#
#------------------------------------------|
#    # Color Variables
#------------------------------------------|

Colors = {
    "Primary" : "g-white",
    "Secondary" : "g-black",
    "Background_Primary" : "g-gray",
    "Background_Secondary" : "g-lightgray",
    "Button_Primary": "g-blue",
    "Button_Secondary": "g-red"
}

#
#\
# \
#===========================================

#{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }
# /
#/        
#
#------------------------------------------|
#    # Middleware WITHOUT Routes
#------------------------------------------|

def Sample_Middleware_Function(  ):
    return "Sample_Middleware_Function Return"

#
#\
# \
#{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# /
#/        # POST functions    
#

# Get Updated Freight Cost
@app.route("/Sample_Post", methods=['POST'])
def Sample_Post(  ):
    print( "---- Sample_Post( ) Start ----" )

    if request.method == "POST":
        JSON_Info = request.get_json()
        ARG_Info = request.args.to_dict()

        return JSON_Info

    return "Error"

#
#\
# \
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# /        
#/        #    Routes for Flask Application
#

#------------------------------------------|
#    # Landing Page for application
#------------------------------------------|

@app.route("/")
def Landing_Page():
    #return("Hello")
    return render_template('Landing_Page.html', title="Landing Page", Colors=Colors)

#------------------------------------------|
#    # /Sample_Route
#------------------------------------------|

# Step 1: 
@app.route("/Sample_Route")

def Sample_Route():
    
    Title = "Sample Route"

    return render_template('Sample/Sample_Route.html', Title=Title, Colors=Colors)

#\
# \
#[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# /        
#/        #    Boot up Application ( Ran on start of script )
#   
    
#------------------------------------------|
#    # Default namespace run 
#------------------------------------------|

def Start_Application( ip, port, Debug_Status ):
    app.run( host=ip, port=port, debug=Debug_Status )
    print("\nUp and Running!!!\n")

#\
# \
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

#++++++++++++++++++++++++++++++++++++++++++++++++++++
# /        
#/        #    Boot up Application ( Ran on start of script )
#   

if __name__ == "__main__":
    Application_JOBS = [  ]
          
    # Add APPLICATION to the Multiprocessor
    ip = 'localhost'
    port = 5000
    Debug = False

    # JOB: 1
    # Application
    Default_Application = multiprocessing.Process(target=Start_Application, args=( ip, port, Debug,))
    Application_JOBS.append( Default_Application )
    Default_Application.start()

#
#\
# \
#++++++++++++++++++++++++++++++++++++++++++++++++++++