# import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy
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
    avocado_json = get_avo()
    tot_tr_json = get_tot_tr()
    avo_tr_json = avo_tr_json
    bananas_json = get_bananas()
    weather_json = get_weather()
    weather_json2 = get_weather2()
    gas_json = get_gas()

    return render_template("index.html", avo_data=avo_data, avocado_json=avocado_json, bananas_json=bananas_json, tot_tr_json=tot_tr_json, avo_tr_json=avo_tr_json, gas_json=gas_json, weather_json=weather_json, weather_json2=weather_json2)

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

    #  WEATHER DATA ---
    # import SQL table as pandas dataframe
    weather_df = pd.read_sql('select * from san_diego', connection)
    weather_df2 = pd.read_sql('select * from san_diego2', connection)

    # convert pandas dataframe to json
    weather_json = json.dumps(weather_df.to_dict('records'), default=str)
    weather_json2 = json.dumps(weather_df2.to_dict('records'), default=str)

    avo_data['weather'] = weather_json
    avo_data['weather2'] = weather_json2
    # --- WEATHER DATA ---

    #  BANANA PRICES DATA ---
    # import SQL table as pandas dataframe
    bananas_df = pd.read_sql('select * from banana_prices', connection)
    
    # convert pandas dataframe to json
    bananas_json = json.dumps(bananas_df.to_dict('records'), default=str)
    
    avo_data['bananas'] = bananas_json
    # --- BANANA PRICES DATA ---

    return avo_data

@app.route("/api/v1.0/avo_prices")
def get_avo():
    
    # AVOCADO PRICES DATA ---
    # import SQL table as pandas dataframe
    avocado_df = pd.read_sql('select * from avocado', connection)
    
    # convert pandas dataframe to json
    avocado_json = json.dumps(avocado_df.to_dict('records'), default=str)

    return avocado_json

@app.route("/api/v1.0/tot_tr")
def get_tot_tr():

    # TOT TRANSPORT PRICES DATA ---
    # import SQL table as pandas dataframe
    tot_tr_df = pd.read_sql('select * from tot_transport', connection)
    
    # convert pandas dataframe to json
    tot_tr_json = json.dumps(tot_tr_df.to_dict('records'), default=str)
    
    return tot_tr_json
    
@app.route("/api/v1.0/avo_tr")
def get_avo_tr():

    #  AVO TRANSPORT PRICES DATA ---
    # import SQL table as pandas dataframe
    avo_tr_df = pd.read_sql('select * from avo_transport', connection)
    
    # convert pandas dataframe to json
    avo_tr_json = json.dumps(avo_tr_df.to_dict('records'), default=str)
    
    return avo_tr_json

@app.route("/api/v1.0/weather")
def get_weather():
    
    #  WEATHER DATA ---
    # import SQL table as pandas dataframe
    weather_df = pd.read_sql('select * from san_diego', connection)

    # convert pandas dataframe to json
    weather_json = json.dumps(weather_df.to_dict('records'), default=str)

    return weather_json
    
@app.route("/api/v1.0/weather2")
def get_weather2():   
    
    #  WEATHER DATA ---
    # import SQL table as pandas dataframe
    weather_df2 = pd.read_sql('select * from san_diego2', connection)

    # convert pandas dataframe to json
    weather_json2 = json.dumps(weather_df2.to_dict('records'), default=str)

    return weather_json2

@app.route("/api/v1.0/bananas")
def get_bananas():

    #  BANANA PRICES DATA ---
    # import SQL table as pandas dataframe
    bananas_df = pd.read_sql('select * from banana_prices', connection)
    
    # convert pandas dataframe to json
    bananas_json = json.dumps(bananas_df.to_dict('records'), default=str)
    
    return bananas_json

@app.route("/api/v1.0/gas")
def get_gas():

    # GAS PRICES DATA ---
    # import SQL table as pandas dataframe
    gas_df = pd.read_sql('select * from gas', connection)
    
    # convert pandas dataframe to json
    gas_json = json.dumps(gas_df.to_dict('records'), default=str)
    
    return gas_json

if __name__ == "__main__":
    app.run(debug = True)