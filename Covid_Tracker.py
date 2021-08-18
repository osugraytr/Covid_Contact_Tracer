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
    "Primary": "g-white",
    "Secondary": "g-black",
    "Background_Primary" : "g-gray",
    "Background_Secondary" : "g-lightgray",
    "Border_Primary": "g-border-color-Covid-Red-thicc"
}

Buttons = {
    "Button_Style": "g-btn-style",
    "Button_Primary": "g-Covid-Light-orange",
    "Button_Secondary": "g-Covid-Light-yellow",
    "Button_Primary_Text": "g-text-white",
    "Button_Secondary_Text": "g-text-black",
    "Button_Text_Size": "g-responsive-text-2"
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
    return render_template('Landing_Page.html', title="Landing Page", Buttons=Buttons, Colors=Colors)

#------------------------------------------|
#    # /Routes
#------------------------------------------|

# Report_Covid_19
@app.route("/Report_Covid_19")
def Report_Covid_19():
    
    Title = "Report Covid 19"

    return render_template('Secondary/Report_Covid_19.html', Title=Title, Buttons=Buttons, Colors=Colors)

# Covid_19 Report Map
@app.route("/Covid_19_Map")
def Covid_19_Map():
    
    Title = "Covid-19 Report Map"

    return render_template('Secondary/Covid_19_Map.html', Title=Title, Buttons=Buttons, Colors=Colors)

# Covid_19 Tracker About 
@app.route("/About_Tracker")
def About_Tracker():
    
    Title = "Covid_19 Tracker About"

    return render_template('Secondary/About_Tracker.html', Title=Title, Buttons=Buttons, Colors=Colors)

# Covid-19 Tracker Donate 
@app.route("/Donate")
def Donate():
    
    Title = "Covid-19 Tracker Donate"

    return render_template('Secondary/Donate.html', Title=Title, Buttons=Buttons, Colors=Colors)

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
    ip = '192.168.4.153'
    #ip = '127.0.0.1'
    #ip = 'localhost'
    port = 5000
    Debug = True

    if(Debug):
        app.run( host=ip, port=port, debug=Debug )
    else:
        # JOB: 1
        # Application
        Default_Application = multiprocessing.Process(target=Start_Application, args=( ip, port, Debug,))
        Application_JOBS.append( Default_Application )
        Default_Application.start()

#
#\
# \
#++++++++++++++++++++++++++++++++++++++++++++++++++++