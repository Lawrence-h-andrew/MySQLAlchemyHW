import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Base.classes.keys()

measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

app = Flask(__name__)
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )
@app.route("/api/v1.0/precipitation")
def precip():
    """Convert the query results to a Dictionary using date as the key and prcp as the value."""
    # Query all measurements
    results = session.query(measurement.prcp).all()

    # Convert list of tuples into dictionary
all_prcp = []
    for precip in results:
        precip_dict = {}
        precip_dict["date"] = measurement.date
        precip_dict["prcp"] = measurement.prcp
        all_prcp.append(precip_dict)
    return jsonify(all_prcp)
@app.route("/api/v1.0/stations")
def names():
    """Return a list of all station names"""
    # Query all stations
    results = session.query(station.station).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)
@app.route("/api/v1.0/tobs")
def temps():
    """Return a list of all dates and temp observations from the past year"""
    # Query all tobs
    results = session.query(measurement.tobs).all()

    # Convert list of tuples into normal list
all_tobs = []
    for tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = measurement.date
        tobs_dict["prcp"] = measurement.tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_names)   
if __name__ == '__main__':
    app.run(debug=True) 