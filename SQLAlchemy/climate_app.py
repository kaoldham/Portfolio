#Dependencies
from datetime import datetime, date, timedelta
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurements
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/><br/>"
        f"*Note: Enter dates in yyyy-mm-dd format.*"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a json list of temperature observations from the past year."""
    # Query all measurements from the past year
    begin_date = date.today() - timedelta(days=365)

    results = session.query(Measurement).filter(Measurement.date>=begin_date)
    # Looping through each of the records from the past
    # year and appending data to a list of results.
    precip_data = []
    for record in results:
    	precip_dict = {}
    	precip_dict['precipitation'] = record.precip
    	precip_dict['date'] = record.date
    	precip_data.append(precip_dict)

    return jsonify(precip_data)


@app.route("/api/v1.0/stations")
def stations():
    """Return a json list of stations from the dataset."""
    # Query all stations
    results = session.query(Station).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for record in results:
        station_dict = {}
        station_dict["Station ID"] = record.station_id
        station_dict["Station Name"] = record.name
        station_dict["Latitude"] = record.lat
        station_dict["Longitude"] = record.lon
        station_dict["Elevation"] = record.elev
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a json list of Temperature Observations (tobs) from the past year."""
    # Query all measurements from the past year
    begin_date = date.today() - timedelta(days=365)

    results = session.query(Measurement).filter(Measurement.date>=begin_date)
    # Looping through each of the records from the past
    # year and appending data to a list of results.
    temp_data = []
    for record in results:
    	temp_dict = {}
    	temp_dict['observed temperature'] = record.tobs
    	temp_dict['date'] = record.date
    	temp_data.append(temp_dict)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return a json list of the minimum temperature, the average temperature,
    and the max temperature past a certain start date."""
    end = datetime.strftime(date.today(), '%Y-%m-%d')

    # Using the calc_temps function to get min, avg, and max temperature.
    temp_data = calc_temps(start, end)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a json list of the minimum temperature, the average temperature,
    and the max temperature within a certain date range."""

    # Using the calc_temps function to get min, avg, and max temperature.
    temp_data = calc_temps(start, end)

    return jsonify(temp_data)

#################################################
# calc_temps function
#################################################

def calc_temps(start_date, end_date):
    
    # Convert string input into date object.
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Run a query filtering by the start and end date.
    temp_function_query = session.query(Measurement).\
            filter(Measurement.date>=start_date,
                   Measurement.date<=end_date)
        
    # Initiate empty list to hold all records' info
    temp_data = []
    temp_function_stations = []
    temp_function_date = []
    for record in temp_function_query:
        temp_data.append(record.tobs)
        # Including station ID and date if I decide to build on this
        # and return more info than just the temperatures.
        temp_function_stations.append(record.station_id)
        temp_function_date.append(record.date)
    
    # Convert lists to pandas dataframe so we can use min, max, mean functions.
    temp_function_df = pd.DataFrame(data={'station_id':temp_function_stations,
                                         'Observed Temperature':temp_data,
                                         'Date':temp_function_date})
    
    # Return a dictionary containing the min, avg, and max temps for the date range.
    return {'Minimum Temperature': temp_function_df['Observed Temperature'].min(),
            'Average Temperature': temp_function_df['Observed Temperature'].mean(),
            'Maximum Temperature': temp_function_df['Observed Temperature'].max()}

if __name__ == '__main__':
    app.run(debug=True)