# import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pd
import json

# import my password from config.py
from config import password

# create engine and connection to postgres
from sqlalchemy import create_engine

db_name = "avocado_db"
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/{db_name}')
connection = engine.connect()
connection

app = Flask(__name__)

@app.route("/")
def index():
    avo_data = get_data()
    return render_template("index.html", avo_data = avo_data)

@app.route("/api/v1.0/data")
def get_data():
    avo_data = {}
    
    # AVOCADO PRICES DATA ---
    # import SQL table as pandas dataframe
    avocado_df = pd.read_sql('select * from avocado', connection)
    
    # convert pandas dataframe to json
    avocado_json = json.dumps(avocado_df.to_dict('records'), default=str)
    
    avo_data['avocado_prices'] = avocado_json
    # --- AVOCADO PRICES DATA ---

    # GAS PRICES DATA ---
    # import SQL table as pandas dataframe
    gas_df = pd.read_sql('select * from gas', connection)
    
    # convert pandas dataframe to json
    gas_json = json.dumps(gas_df.to_dict('records'), default=str)
    
    avo_data['gas_prices'] = gas_json
    # --- GAS PRICES DATA ---

    # TOT TRANSPORT PRICES DATA ---
    # import SQL table as pandas dataframe
    tot_tr_df = pd.read_sql('select * from tot_transport', connection)
    
    # convert pandas dataframe to json
    tot_tr_json = json.dumps(tot_tr_df.to_dict('records'), default=str)
    
    avo_data['tot_transport'] = tot_tr_json
    # --- TOT TRANSPORT PRICES DATA ---

    #  AVO TRANSPORT PRICES DATA ---
    # import SQL table as pandas dataframe
    avo_tr_df = pd.read_sql('select * from avo_transport', connection)
    
    # convert pandas dataframe to json
    avo_tr_json = json.dumps(avo_tr_df.to_dict('records'), default=str)
    
    avo_data['avo_transport'] = avo_tr_json
    # --- AVO TRANSPORT PRICES DATA ---
    return avo_data

if __name__ == "__main__":
    app.run(debug = True)