import os
from web import create_app

#TODO add CLI parsing to have optional debugging
#TODO add CLI parsing to run in given directory
app = create_app(os.getcwd())
app.run(debug=True)
