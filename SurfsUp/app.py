# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
# reflect the tables
# Save references to each table
# Create our session (link) from Python to the DB

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/StartDate<br/>"
        f"/api/v1.0/StartDate/EndDate<br/>"
        f"Note: Change StartDate and EndDate as: yyyy-mm-dd format<br/>"
        f"Example: /api/v1.0/2016-08-24/2017-08-23"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the most recent date
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query precipitation data for the last 12 months
    precipitation_data = session.query(Measurement.date, Measurement.prcp)\
                                .filter(Measurement.date >= one_year_ago)\
                                .all()
    
    # Create a dictionary with date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    
    return jsonify(precipitation_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query and list of stations
    station_results = session.query(Station.station).all()
    stations_list = [station[0] for station in station_results]
    
    return jsonify(stations_list)

# Temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    # Get the most active station ID
    most_active_station = session.query(Measurement.station)\
                              .group_by(Measurement.station)\
                              .order_by(func.count(Measurement.station).desc())\
                              .first()[0]
    
    # Calculate the date one year ago from the most recent date
    most_recent_date = session.query(func.max(Measurement.date))\
                          .filter(Measurement.station == most_active_station)\
                          .scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query temperature observations for the last 12 months for the most active station
    temperature_data = session.query(Measurement.date, Measurement.tobs)\
                            .filter(Measurement.station == most_active_station)\
                            .filter(Measurement.date >= one_year_ago)\
                            .all()
     # Convert Row objects to dictionaries
    temperature_list = [{"date": row.date, "tobs": row.tobs} for row in temperature_data]
    
    return jsonify(temperature_list)

# Temperature statistics route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    if not end:
        end = session.query(func.max(Measurement.date)).scalar()
    
    # Query temperature statistics for the specified date range
    temperature_stats = session.query(func.min(Measurement.tobs),
                                      func.avg(Measurement.tobs),
                                      func.max(Measurement.tobs))\
                               .filter(Measurement.date >= start)\
                               .filter(Measurement.date <= end)\
                               .all()
    
    # Unpack the results
    min_temp, avg_temp, max_temp = temperature_stats[0]
    
    return jsonify({"start_date": start, "end_date": end, "TMIN": min_temp, "TAVG": avg_temp, "TMAX": max_temp})

if __name__ == "__main__":
    app.run(debug=True)