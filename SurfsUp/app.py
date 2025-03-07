# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.orm import Session  
from sqlalchemy import create_engine, func
import pandas as pd
from datetime import timedelta

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurements = Base.classes.measurement
Stations = Base.classes.station

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
def home():
    """All available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (After 'start' add ?start_date=YYYY-MM-DD filled in with the date you want to use)<br/>"
        f"/api/v1.0/start_end (After 'start_end' add ?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD filled in with the date you want to use)"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # get precipitation results from the last 12 months of data
    precip_results = session.query(Measurements.date, Measurements.prcp).filter(Measurements.date >= '2016-08-23').filter(Measurements.date <= '2017-08-23').all()

    precip_data = []
    for prcp in precip_results:
        precip_dict = {}
        precip_dict["date"] = prcp[0]
        precip_dict["prcp"] = prcp[1]
        precip_data.append(precip_dict)

    return jsonify(precip_data)


@app.route("/api/v1.0/stations")
def stations():

    # Get the station names
    station_results = session.query(Stations.station).all()

    station_names = list(np.ravel(station_results))

    return jsonify(station_names)


@app.route("/api/v1.0/tobs")
def tobs():

    # find the most active station
    most_active_stations = session.query(Measurements.station, func.count(Measurements.station)).group_by(Measurements.station).order_by(func.count(Measurements.station).desc()).all()
    most_active_station_id = most_active_stations[0][0]

    # get the last 12 months of temperature data for the most active station
    results = session.query(Measurements.tobs) \
    .filter(Measurements.station == most_active_station_id) \
    .filter(Measurements.date >= '2016-08-23') \
    .all()

    temp_data = list(np.ravel(results))
    return jsonify(temp_data)

@app.route("/api/v1.0/start", methods=['GET'])
def temps_start():

    start_date = request.args.get('start_date')

    # Find the min, max and avg for temperature data after a specified start date
    results = session.query(
        func.min(Measurements.tobs),
        func.max(Measurements.tobs),
        func.avg(Measurements.tobs)
    ).filter(Measurements.date >= start_date).all()

    min, avg, max = results[0]

    return jsonify({
        "start_date": start_date,
        "MIN": min,
        "AVG": avg,
        "MAX": max
    })

@app.route('/api/v1.0/start_end', methods=['GET'])
def start_end():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Find the min, max and avg for temperature data after specified start and end dates
    results = session.query(
        func.min(Measurements.tobs),
        func.max(Measurements.tobs),
        func.avg(Measurements.tobs)
    ).filter(Measurements.date >= start_date).filter(Measurements.date <= end_date).all()

    min, avg, max = results[0]

    return jsonify({
        "start_date": start_date,
        "end_date": end_date,
        "MIN": min,
        "AVG": avg,
        "MAX": max
    })

if __name__ == "__main__":
    app.run(debug=True)
