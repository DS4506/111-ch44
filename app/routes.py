from flask import Flask # from the flask module import the flask class
#oop- object orinented paradigm

app = Flask (__name__) # create an instance of flask into app (now an object)

@app.get("/")# flask decorator that maps routes to view functions
def index(): # in flask, "wrapped" functions are referred to as "view functions"
    me = {   # python dictionary (key-value pairs)
        "first_name": "David",
        "last_name": "Smith",
        "hobbies": "football",
        "online": True
    }
    return me # In flask, when you return a dictionary, it is automatically converted to JSON